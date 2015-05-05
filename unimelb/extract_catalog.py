from CatalogCrawler.extractor import Extractor
from CatalogCrawler.catalog import Catalog
from lxml import etree
from pandas import DataFrame


class UnimelbExtractor(Extractor):
    def extract_each(self, filename):
        with open(filename) as f:
            data = f.read()
        try:
            html = etree.HTML(data)
        except:
            return Catalog()
        course_block = html.xpath('//li')
        course_title = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//a[@class="no-stack more-info-btn"]//text()')
        ).strip() for e in course_block]
        course_desc = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//p//text()')
        ) for e in course_block]

        course_id = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//a[@class="no-stack more-info-btn"]//@href')
        ) for e in course_block]

        d = DataFrame({'course_title': course_title, 'desc': course_desc, 'course_id': course_id})

        d['course_id'] = d['course_id'].map(lambda x: x.split('/')[-1])

        d['instructor'] = ''

        d['desc'] = d['desc'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip('"').strip())

        d['school'] = 'unimelb'
        d['id'] = filename.strip(self.input_directory).strip('/')

        return Catalog(data=d)

extractor = UnimelbExtractor(input_directory='raw_output')
extractor.extract_all()
extractor.print_result()
extractor.to_csv()