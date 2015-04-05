import scrapy
import re
from googleresults.items import GoogleresultsItem
from scrapy.selector import Selector
class YahooSpider(scrapy.Spider):
    name="yahoo"
    allowed_domains=["search.yahoo.com"]
    start_urls=[
        "https://search.yahoo.com/search?p=jaguar&pz=40"
    ]


    def parse(self, response):
        #unicode(response.body.decode(response.encoding)).encode('utf-8')
        unicode(response.body.decode(response.encoding)).encode('utf-8')
        for sel in response.xpath('//div[contains(@class,"dd algo")]'):
            item = GoogleresultsItem()
            t=sel.xpath('div[@class="compTitle"]/h3[@class="title"]/a/text()').extract()
                       
            item['title']=t
            l=sel.xpath('div[@class="compTitle"]/div/span').extract()
            l=[x.encode('utf-8') for x in l]
            p = re.compile(ur'<[^>]*>')
            # Error here .Python expects string here but p is a non utf8 string.
            t=re.sub(str(p),"", l)
            t= "http://"+t
            p = re.compile(ur'(.*)index.html')
            gp=re.search(p, t)
            if gp:
                t = gp.group(1)            
            item['link']=t
            d=sel.xpath('div[@class="compText aAbs"]/p[@class="lh-18"]/text()').extract()
            
            item['desc']=d
            yield item
        """
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
            """



