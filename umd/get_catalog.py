from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'https://ntst.umd.edu/soc/',
    'base_url': 'https://ntst.umd.edu/soc/',
    'item_xpath': '//div[@class="course-prefix row"]',
    'category_xpath': 'span[@class="prefix-name nine columns"]//text()',
    'url_xpath': 'a[@class="clearfix"]//@href'
}

umd = HTMLSchool(info=info,
                  short_name='umd')

umd.to_csv(filename='umd.txt')

crawl = CourseSpider(filename='umd.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
