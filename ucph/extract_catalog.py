from CatalogCrawler.extractor import Extractor
from CatalogCrawler.catalog import Catalog
from lxml import etree
from pandas import DataFrame


class UcphExtractor(Extractor):
    def extract_each(self, filename):
        with open(filename) as f:
            data = f.read()
        try:
            html = etree.HTML(data)
        except:
            return Catalog()
        course_block = html.xpath('//div[@id="CourseDescriptionDiv"]')
        course_title = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//h1[@class="CourseTitle"]/text()')
        ).strip() for e in course_block]
        course_desc = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//table[@class="courseDescription"][2]//text()')
        ).replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').strip() for e in course_block]

        course_instructor = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//ul[@class="valueList"]//li/text()')
        ) for e in course_block]


        d = DataFrame({'course_title': course_title, 'desc': course_desc, 'instructor': course_instructor})

        d['course_id'] = d['course_title'].map(lambda x: ' '.join(x.encode('utf-8').split(u'\xa0'.encode('utf-8'))[:-1]).strip())
        d['course_title'] = d['course_title'].map(lambda x: x.encode('utf-8').split(u'\xa0'.encode('utf-8'))[-1].strip())
        d['desc'] = d['desc'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip('"').strip())

        d['school'] = 'ucph'
        d['id'] = filename.strip(self.input_directory).strip('/')

        return Catalog(data=d)

extractor = UcphExtractor(input_directory='raw_output')
extractor.extract_all()
extractor.print_result()
extractor.to_csv()