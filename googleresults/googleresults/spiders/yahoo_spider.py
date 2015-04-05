import scrapy
import re
from googleresults.items import GoogleresultsItem
from scrapy.selector import Selector
class YahooSpider(scrapy.Spider):
    name="yahoo"
    allowed_domains=["search.yahoo.com"]
    def __init__(self, query=None, *args, **kwargs):
        super(YahooSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://search.yahoo.com/search?p='+query+"&pz=30"]   


    def parse(self, response):
        unicode(response.body.decode(response.encoding)).encode('utf-8')
        fo=0
        for sel in response.xpath('//div[contains(@class,"dd algo fst")]'):
            if(fo==1):
                break
            item = GoogleresultsItem()
            t=sel.xpath('div/div[@class="compTitle"]/h3/a').extract()
            stri=""
            for i in range(len(t)):
                stri=stri+" "+t[i]             
            item['title']=stri            
            l=sel.xpath('div/div[@class="compTitle"]/h3/a/@href').extract()
            stri=""
            for i in range(len(l)):
                stri=stri+" "+l[i] 
            p = re.compile(ur'<[^>]*>')
            t=re.sub(p,"", stri)
            p = re.compile(ur'(.*)index.html')
            gp=re.search(p, t)
            if gp:
                t = gp.group(1)            
            item['link']=t.strip()
            d=sel.xpath('div/div[@class="layoutCenter"]/div[@class="compText aAbs"]/p').extract()
            stri=""
            for i in range(len(d)):
                stri=stri+" "+d[i]
            item['desc']=stri            
            yield item
            fo+=1
            
        for sel in response.xpath('//div[contains(@class,"dd algo")]'):
            item = GoogleresultsItem()   
            t=sel.xpath('div[@class="compTitle"]/h3[@class="title"]/a').extract()
            stri=""
            for i in range(len(t)):
                stri=stri+" "+t[i]
            if(stri==""):
                continue
            item['title']=stri
            l=sel.xpath('div[@class="compTitle"]/h3[@class="title"]/a/@href').extract()
            stri=""
            for i in range(len(l)):
                stri=stri+" "+l[i] 
            p = re.compile(ur'<[^>]*>')
            t=re.sub(p,"", stri)
            p = re.compile(ur'(.*)index.html')
            gp=re.search(p, t)
            if gp:
                t = gp.group(1)            
            item['link']=t.strip()
            d=sel.xpath('div[@class="compText aAbs"]/p[@class="lh-18"]').extract()
            stri=""
            for i in range(len(d)):
                stri=stri+" "+d[i]
            item['desc']=stri
            yield item



