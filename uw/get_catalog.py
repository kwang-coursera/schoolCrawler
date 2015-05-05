from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'http://www.washington.edu/students/crscat/',
    'base_url': 'http://www.washington.edu/students/crscat/',
    'item_xpath': '//body/ul//li//a',
    'category_xpath': '//text()',
    'url_xpath': '//@href'
}

uw = HTMLSchool(info=info,
                  short_name='uw')

print uw.get_school_items()

uw.to_csv(filename='uw.txt')

crawl = CourseSpider(filename='uw.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
