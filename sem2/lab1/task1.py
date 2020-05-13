import os
from lxml import etree

os.system("scrapy crawl golosua")
root = None
with open('results/golosua.xml', 'r') as file:
    root = etree.parse(file)

pagesCount = root.xpath('count(//page)')
textFragmentsCount = root.xpath('count(//fragment[@type="text"])')
print('Average count of text fragments per page %f' % (textFragmentsCount / pagesCount))
