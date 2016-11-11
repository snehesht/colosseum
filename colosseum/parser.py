"""
CSS stylesheet parser


Parse stylesheet written in CSS and wrap then in colosseum.CSS object and pass
to the style attribute.

----------------------
<<< main.css >>>

.button1 {
    width: 100px;
    height: 30px;
    margin: 10px 5px;
    padding: 10px;
}

<<< EOF >>>

----------------------

<<< somefile.py >>>

from colosseum import Parser

#css = Parser('main.css')
css = Parser(
'''
.button {
    width: 100px;
    height: 40px;
    padding: 10px;
    margin: 10px 10px 30px 10px;
}

''' )


box(style=css.button1)

<<< EOF >>>

----------------------


"""
