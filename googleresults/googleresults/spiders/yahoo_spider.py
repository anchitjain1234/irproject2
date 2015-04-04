import scrapy
import re
from googleresults.items import GoogleresultsItem
from scrapy.selector import Selector
class YahooSpider(scrapy.Spider):
    name="yahoo"
    allowed_domains=["search.yahoo.com"]
    start_urls=[
        "https://search.yahoo.com/search?p=jaguar&pz=30"
    ]


    def parse(self, response):
        #unicode(response.body.decode(response.encoding)).encode('utf-8')
        item = GoogleresultsItem()
        sel = Selector(response)
        ts=sel.xpath('//h3[@class="title"]/a/text()').extract()
        ls=sel.xpath('//h3[@class="title"]/a/@href').extract()
        ds=sel.xpath('//p[@class="lh-18"]').extract()
        for t,l,d in zip(ts,ls,ds):
            item['title'] = t  
            item['desc'] = d
            item['link'] = l 
            p = re.compile(ur'(.*)index.html')
            gp=re.search(p, l)
            if gp:
                item['link'] = gp.group(1)
            yield item              



