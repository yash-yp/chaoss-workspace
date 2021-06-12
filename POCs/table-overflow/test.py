
import pypandoc

def func1():
    output = pypandoc.convert_file("lvl1.tex", 'pdf', outputfile="lvl1.pdf", extra_args=['-f', 'latex',
                                                                                                '--pdf-engine=xelatex',
                                                                                                 '-H', 'header.tex',
                                                                                                 '--highlight-style','zenburn',                                                                                            '-V',
                                                                                                 'geometry:margin=0.8in',
                                                                                                 '-V', 'monofont:DejaVuSansMono.ttf',
                                                                                                 '-V', 'mathfont:texgyredejavu-math.otf',
                                                                                                 '-V', 'geometry:a4paper',
                                                                                                 '-V', 'colorlinks=true',
                                                                                                 '-V', 'linkcolour:blue',
                                                                                                 '-V', 'fontsize=12pt',
                                                                                                 '--toc', '--toc-depth= 1',
 #                                                                                               '--columns=20', '--wrap=preserve'
                                                                                                ])
def func2():

    output = pypandoc.convert_file("table.tex", 'html', outputfile="table-test.html", extra_args=['-s','-f', 'latex'])
    assert output == ""

func2()

