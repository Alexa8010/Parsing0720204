import scrapy


class ImpactfactorSpiderSpider(scrapy.Spider):
    name = "impact_spider"
    allowed_domains = ["scimagojr.com"]
    start_urls = ["https://scimagojr.com/journalrank.php?category=2705&area=2700&country=Western%20Europe&order=sjr&ord=asc"]

    def parse(self, response):
        # 
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            title = row.xpath(".//td[2]/a/text()").get()
            type = row.xpath('.//td[3]/text()').get()
            JCR_impact = float(row.xpath('.//td[4]/text()').get())
            quartile = row.xpath('td[4]/span/text()').get()
            h_index = float(row.xpath('.//td[5]/text()').get())
            total_cites = float(row.xpath('.//td[9]/text()').get())
            link = row.xpath(".//td[2]/a//@href").get() 
            yield response.follow(url=link if link else "journalsearch.php?q=144769&tip=sid&clean=0", callback=self.parse_impact,  meta={
                                      'title': title,
                                      'type' : type,
                                      'JCR_impact': JCR_impact,
                                      'quartile' : quartile,
                                      'h_index' : h_index,
                                      'total_cites' : total_cites,
                                      })
            
            
    def parse_impact(self, response):
        rows = response.xpath('//body/div[contains (@class, "background")][1]')
        for row in rows:
            title = response.request.meta['title']
            country = response.xpath('//div[contains (@class, "journalgrid")]/p/a/text()').get()
            type = response.request.meta['type'] 
            JCR_impact = response.request.meta['JCR_impact']
            quartile = response.request.meta['quartile']
            h_index = response.request.meta['h_index']
            total_cites = response.request.meta['total_cites']
            yield {
                'title': title.strip() if title else '',
                'country' : country.strip() if country else '',
                'type': type.strip() if type else '',
                'JCR_impact': JCR_impact if JCR_impact else '',
                'quartile': quartile if quartile else '',
                'h_index': h_index if h_index else '',
                'total_cites': total_cites if total_cites else ''
            }   
