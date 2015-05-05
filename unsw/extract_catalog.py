from CatalogCrawler.extractor import Extractor
from CatalogCrawler.catalog import Catalog
from lxml import etree
from pandas import DataFrame


class UnswExtractor(Extractor):
    def extract_each(self, filename):
        with open(filename) as f:
            data = f.read()
        try:
            html = etree.HTML(data)
        except:
            return Catalog()
        course_block = html.xpath('//html')
        course_title = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//div[@class="internalContentWrapper"]//h1//text()')
        ).strip() for e in course_block]
        course_desc = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//div[@class="internalContentWrapper"]//div[4]//text()')
        ) for e in course_block]

        d = DataFrame({'course_title': course_title, 'desc': course_desc})

        d['course_id'] = d['course_title'].map(lambda x: x.split('-')[-1].strip())
        d['course_title'] = d['course_title'].map(lambda x: ' '.join(x.split('-')[:-1]).strip())
        d['instructor'] = ''
        d['desc'] = d['desc'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip('"').strip())

        d['school'] = 'unsw'
        d['id'] = filename.strip(self.input_directory).strip('/')

        return Catalog(data=d)

extractor = UnswExtractor(input_directory='raw_output')
extractor.extract_all()
extractor.print_result()
extractor.to_csv()