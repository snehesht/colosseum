import argparse
import shutil
import os


def generate(source, output, existing):
    os.makedirs(output)
    with open(os.path.join(output, '__init__.py'), 'w') as initfile:
        initfile.write('\n')

    for path, dirs, filenames in os.walk(os.path.abspath(source)):
        for filename in filenames:
            if filename == 'implementation-report-TEMPLATE.data':
                module_name = 'test_' + ''.join(s.title() for s in os.path.basename(path)[:-4].split('-'))
                print ("Adding test module %s..." % module_name)
                if existing:
                    decorators = {}
                    with open(os.path.join(existing, "%s.py" % module_name)) as existingfile:
                        decorator = None
                        for line in existingfile:
                            if line.startswith('    def test_'):
                                test_name = line[13:-8]
                                if decorator:
                                    decorators[test_name] = decorator
                                decorator = None
                            elif line.startswith('    @'):
                                decorator = line
                            else:
                                decorator = None
                else:
                    decorators = {}

                with open(os.path.join(output, "%s.py" % module_name), 'w') as testfile:

                    # Create the directory for test input HTML
                    test_input_dir = os.path.join(os.path.abspath(output), 'source', module_name)
                    os.makedirs(test_input_dir)

                    # Copy the test support files
                    try:
                        shutil.copytree(
                            os.path.join(os.path.abspath(source), os.path.basename(path), 'html', 'support'),
                            os.path.join(test_input_dir, 'support')
                        )
                    except FileNotFoundError as e:
                        pass

                    # Create the directory for reference images
                    test_ref_dir = os.path.join(output, 'reference', module_name)
                    os.makedirs(test_ref_dir)

                    # Create the test case code.
                    with open(os.path.join(path, filename)) as data:
                        count = 0
                        testfile.write('from unittest import expectedFailure')
                        testfile.write('\n')
                        testfile.write('from .. utils import CSSWGTestCase')
                        testfile.write('\n')
                        testfile.write('\n')
                        testfile.write('class %s(CSSWGTestCase):\n' % module_name)
                        for line in data:
                            if line.startswith('html/') or line.startswith('html4'):
                                test_name = os.path.splitext(line.split('\t')[0].split('/')[1])[0].replace('-', '_').replace('.', '_')
                                try:
                                    testfile.write(decorators[test_name])
                                except KeyError:
                                    pass

                                testfile.write('    def test_%s(self):\n' % test_name)
                                testfile.write("        self.assertRender('%s', '%s')\n" % (module_name, test_name))
                                testfile.write('\n')

                                shutil.copyfile(
                                    os.path.join(os.path.abspath(source), os.path.basename(path), line.split('\t')[0]),
                                    os.path.join(test_input_dir, '%s.html' % test_name)
                                )

                                count += 1
                        if count == 0:
                            testfile.write('    pass\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Generate test suite from W3C CSS Working Group originals sources.

The `source` is the path to a checkout of the generated W3C CSS test
directory:

    https://github.com/jgraham/css-test-built.git

        """
    )

    parser.add_argument(
        '-o', '--output',
        help='The directory where test class files should be output.',
        default='csswg'
    )
    parser.add_argument(
        '-x', '--existing',
        help='The directory where existng class files can be found.',
    )
    parser.add_argument(
        'source',
        help='The root directory of the csswg-tests checkout'
    )

    args = parser.parse_args()

    generate(args.source, args.output, args.existing)
