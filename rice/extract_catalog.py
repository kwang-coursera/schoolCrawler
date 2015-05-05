from CatalogCrawler.extractor import Extractor
from CatalogCrawler.catalog import Catalog
from lxml import etree
from pandas import DataFrame


class RiceExtractor(Extractor):
    def extract_each(self, filename):
        with open(filename) as f:
            data = f.read()
        try:
            html = etree.HTML(data)
        except:
            return Catalog()
        course_block = html.xpath('//div[@class="course"]')
        course_title = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//div[@class="title"]//text()')
        ).strip() for e in course_block]
        course_desc = [' '.join(
            etree.HTML(etree.tostring(e)).xpath('//div[position()=6]//text()')
        ) for e in course_block]

        d = DataFrame({'course_title': course_title, 'desc': course_desc})

        d['instructor'] = ''
        d['course_id'] = d['course_title'].apply(
            lambda x: x.encode('utf-8').split('-')[0].strip()
        )
        d['title'] = d['course_title'].apply(
            lambda x: x.encode('utf-8').split('-')[1].strip()
        )
        d['desc'] = d['desc'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' ').strip('"').strip())

        d['school'] = 'rice'
        d['id'] = filename.strip(self.input_directory).strip('/')

        return Catalog(data=d)

extractor = RiceExtractor(input_directory='raw_output')
extractor.extract_all()
extractor.print_result()
extractor.to_csv()