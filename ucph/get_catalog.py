from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'http://kurser.ku.dk/search?q=&studyBlockId=null&teachingLanguage=en-GB&period=&schedules=&studyId=&openUniversity=-1&programme=&faculty=&departments=&volume=',
    'base_url': 'http://kurser.ku.dk',
    'item_xpath': '//tr',
    'category_xpath': '//td//span//text()',
    'url_xpath': '//a//@href'
}

ucph = HTMLSchool(info=info,
                  short_name='ucph')

print ucph.get_school_items()

ucph.to_csv(filename='ucph.txt')

crawl = CourseSpider(filename='ucph.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
