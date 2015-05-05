from CatalogCrawler.school import HTMLSchool
from CatalogCrawler.crawler import CourseSpider
from CatalogCrawler.extractor import Extractor

info = {
    'parent_url': 'http://www.ed.ac.uk/studying/visiting-exchange/course-finder?cfsearch=&submitted=yes&showadvanced=yes&period=all&subject=all&year-taken=all&credits=all&cw_xml=http%3A%2F%2Fwww.visitingstudentoffice.apps.hss.ed.ac.uk%2Fcoursefinder%2Findex.php',
    'base_url': '',
    'item_xpath': '//table[@id="searchresults"]//tr',
    'category_xpath': 'td[3]//text()',
    'url_xpath': 'td[2]//a//@href'
}

edinburgh = HTMLSchool(info=info,
                  short_name='edinburgh')

edinburgh.to_csv(filename='edinburgh.txt')

crawl = CourseSpider(filename='edinburgh.txt', sep='\x1A', raw_output='raw_output', log='log.txt')
crawl.crawl_all()
