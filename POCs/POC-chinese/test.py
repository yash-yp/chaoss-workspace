
import pypandoc

def func1():
    output = pypandoc.convert_file("lvl1.tex", 'pdf', outputfile="file4.pdf", extra_args=['-f', 'latex',
                                                                                                '--pdf-engine=xelatex',
                                                                                                '-H', 'header.tex',
                                                                                                '--highlight-style','zenburn',
                                                                                                '-V', 'toc-title:内容',
                                                                                                '-V', 'geometry:margin=0.8in',
                                                                                                '-V', 'geometry:a4paper',
                                                                                                '-V', 'colorlinks=true',
                                                                                                '-V', 'linkcolour:blue',
                                                                                                '-V', 'fontsize=12pt',
                                                                                                '--toc', '--toc-depth= 1'
                                                                                                ])
    assert output == ""

def func2():

    output = pypandoc.convert_file("chinese-2.md", 'latex', outputfile="2.tex", extra_args=['-f', 'markdown_github'])

    assert output == ""

#'-V', 'mainfont:DejaVuSerif',
#'-V', 'sansfont:DejaVuSans','-V', 'monofont:DejaVuSansMono',
# '-V', mathfont:TeXGyreDejaVuMath-Regular'
# for table overflow use markdown_github format inplace of gfm


func1()