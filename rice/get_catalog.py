from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'https://courses.rice.edu/admweb/swkscat.main?p_action=cata',
    'base_url': 'https://courses.rice.edu',
    'item_xpath': '//*[@class="subjectList"]//tr',
    'category_xpath': 'td[@class="subjDesc"]//text()',
    'url_xpath': 'td[@class="subjCode"]//a//@href'
}

rice = HTMLSchool(info=info,
                  short_name='rice')

rice.to_csv(filename='rice.txt')

crawl = CourseSpider(filename='rice.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
