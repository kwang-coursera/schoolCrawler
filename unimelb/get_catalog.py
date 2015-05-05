from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'http://coursesearch.unimelb.edu.au/undergrad',
    'base_url': 'http://coursesearch.unimelb.edu.au',
    'item_xpath': '//div[@class="search-item type-major search-match"]//a[@class="stack"]',
    'category_xpath': 'h3//text()',
    'url_xpath': '@href'
}

unimelb = HTMLSchool(info=info,
                  short_name='unimelb')

unimelb.to_csv(filename='unimelb.txt')

crawl = CourseSpider(filename='unimelb.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
