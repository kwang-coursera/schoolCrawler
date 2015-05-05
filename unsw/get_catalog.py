from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'http://www.handbook.unsw.edu.au/vbook2015/brCoursesByAtoZ.jsp?StudyLevel=Undergraduate&descr=All',
    'base_url': '',
    'item_xpath': '//tr/td/a',
    'category_xpath': 'text()',
    'url_xpath': '@href'
}

unsw = HTMLSchool(info=info,
                  short_name='unsw')

print unsw.get_school_items()

unsw.to_csv(filename='unsw.txt')

crawl = CourseSpider(filename='unsw.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
