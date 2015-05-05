from CatalogCrawler.extractor import Extractor
from CatalogCrawler.catalog import Catalog
from lxml import etree
from pandas import DataFrame


class EdinburghExtractor(Extractor):
    def extract_each(self, filename):
        with open(filename) as f:
            data = f.read()
        try:
            html = etree.HTML(data)
        except:
            return Catalog()
        course_block = html.xpath('//div[@class="contentArea"]')
        course_title = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//h3//text()')
        ).strip() for e in course_block]
        course_desc = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//p[1]//text()')
        ) for e in course_block]

        d = DataFrame({'course_title': course_title, 'desc': course_desc})

        d['instructor'] = ''
        d['course_id'] = d['course_title'].apply(
            lambda x: x.encode('utf-8').split('(')[-1].strip(')').strip()
        )
        d['title'] = d['course_title'].apply(
            lambda x: '('.join(x.encode('utf-8').split('(')[:-1]).strip()
        )
        d['desc'] = d['desc'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip('"').strip())

        d['school'] = 'edinburgh'
        d['id'] = filename.strip(self.input_directory).strip('/')

        return Catalog(data=d)

extractor = EdinburghExtractor(input_directory='raw_output')
extractor.extract_all()
extractor.print_result()
extractor.to_csv()