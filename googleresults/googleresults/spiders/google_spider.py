import scrapy
from googleresults.items import GoogleresultsItem
from scrapy.selector import Selector
import re
import html2text
class GoogleSpider(scrapy.Spider):
    name="google"
    allowed_domains=["google.com"]
    start_urls=[
        "https://www.google.com/search?q=jaguar&num=50&gws_rd=ssl,cr&fg=1"
    ]
    
        
    def parse(self, response):
        temp=0
        #unicode(response.body.decode(response.encoding)).encode('utf-8')
        item = GoogleresultsItem()
        sel = Selector(response)
        ts=sel.xpath('//h3[@class="r"]/a/text()').extract()
        ls=sel.xpath('//h3[@class="r"]/a/@href').extract()
        ds=sel.xpath('//span[@class="st"]').extract()
        for t,l,d in zip(ts,ls,ds):
            if temp==30:
                break
            item['title'] = t
            
            item['desc'] = d  
           
            p = re.compile(ur'(https?://.*)&sa')
            match=re.search(p, l)
            if match:
                item['link'] = match.group(1)
            else:
                item['link'] = l
            
            p = re.compile(ur'^/[s|i]')
            match2=re.search(p, l)
            if match2:
                continue
            
            yield item     
            temp+=1
            
              
        
        