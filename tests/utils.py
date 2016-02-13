import os

from PIL import Image, ImageDraw, ImageFont, ImageChops

from unittest import TestCase, SkipTest


class RenderingTestCase(TestCase):
    def assertRender(self, modulename, testname):
        with open(os.path.join(os.path.join(self.SOURCE_DIR, modulename, self.SOURCE_PATTERN % testname))) as source:
            # Load a reference file.
            reference_file = os.path.join(self.REFERENCE_DIR, modulename, '%s.png' % testname)

            if not os.path.exists(reference_file):
                raise SkipTest("No reference file provided")

            reference = Image.open(reference_file)

            # Create the output directory
            output_dir = os.path.join(self.OUTPUT_DIR, modulename)

            try:
                os.makedirs(output_dir)
            except FileExistsError:
                pass

            # Generate filenames for test artefacts
            output_file = os.path.join(output_dir, '%s.png' % testname)
            expected_file = os.path.join(output_dir, '%s.expected.png' % testname)
            diff_file = os.path.join(output_dir, '%s.diff.png' % testname)

            # Render the source file
            img = self.render(source)

            # Compare the reference image to the rendered image
            diff = ImageChops.difference(reference.convert('RGB'), img.convert('RGB'))

            # Get the bounding box of non-zero regions. If the images are identical,
            # there will *only* be zero regions, which is an indicator of success.
            if diff.getbbox() is not None:
                img.save(output_file)
                reference.save(expected_file)
                diff.save(diff_file)
                self.fail('Rendering discrepancy found; see image files for details.')
            else:
                # On test pass, clean up any test failure artefacts
                # from previous test runs.
                try:
                    os.remove(output_file)
                except OSError:
                    pass

                try:
                    os.remove(expected_file)
                except OSError:
                    pass

                try:
                    os.remove(diff_file)
                except OSError:
                    pass


class CSSWGTestCase(RenderingTestCase):
    SOURCE_DIR = 'tests/csswg/source'
    SOURCE_PATTERN = '%s.html'
    REFERENCE_DIR = 'tests/csswg/reference'
    OUTPUT_DIR = 'tests/csswg/output'

    def render(self, source):
        img = Image.new('RGBA', (800, 600), color='#ffffff')
        draw = ImageDraw.Draw(img)

        # serif_16 = ImageFont.truetype("tests/fonts/Alegreya/Alegreya-Regular.ttf", 16)
        sans_16 = ImageFont.truetype("tests/fonts/SourceSansPro/SourceSansPro-Regular.ttf", 16)
        serif_16 = ImageFont.truetype("tests/fonts/SourceSerifPro/SourceSerifPro-Regular.ttf", 16)

        # draw.line((0, 0) + img.size, fill='#ff0000')
        # draw.rectangle(((20, 20), (200, 200)), outline='#00ff00', fill='#0000ff')

        # def rectangle(draw, coords, outline='#000000', fill='#ffffff', width=1):
        #     draw.rectangle(coords, fill=fill)

        #     draw.rectangle(((coords[0][0] - width, coords[0][1] - width), (coords[1][0] + width, coords[0][1] - 1)), fill=outline)
        #     draw.rectangle(((coords[1][0] + 1, coords[0][1] - width), (coords[1][0] + width, coords[1][1] + width)), fill=outline)
        #     draw.rectangle(((coords[0][0] - width, coords[1][1] + 1), (coords[1][0] + width, coords[1][1] + width)), fill=outline)
        #     draw.rectangle(((coords[0][0] - width, coords[0][1] - width), (coords[0][0] - 1, coords[1][1] + width)), fill=outline)

        # rectangle(draw, ((300, 20), (500, 220)), outline='#00ff00', fill='#0000ff', width=10)

        # rectangle(draw, ((600, 20), (700, 220)), outline='#00ff00', fill='#0000ff', width=9)

        draw.text((30, 300), 'Hello world', font=serif_16, fill='#000000')
        draw.text((230, 300), 'Size: (%s, %s)' % serif_16.getsize('Hello world'), font=serif_16, fill='#000000')
        draw.text((30, 400), 'Hello world', font=sans_16, fill='#000000')
        draw.text((230, 400), 'Size: (%s, %s)' % sans_16.getsize('Hello world'), font=sans_16, fill='#000000')

        return img
