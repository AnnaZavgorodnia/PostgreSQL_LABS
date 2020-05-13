import os
import lxml.etree as ET


def crawl():
    try:
        os.remove("results/petmarket.xml")
    except OSError:
        print("results/petmarket.xml not found")
    os.system("scrapy crawl petmarket -o results/petmarket.xml -t xml")


def xslt_parse():
    dom = ET.parse('results/petmarket.xml')
    xslt = ET.parse('petmarket.xslt')
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    with open('results/petmarket.html', 'wb') as f:
        f.write(ET.tostring(newdom, pretty_print=True))
    print('results/petmarket.html was created')


crawl()
xslt_parse()
