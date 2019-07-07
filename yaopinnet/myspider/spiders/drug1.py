# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:16:25 2019

@author: eileenlu
"""

import scrapy


class DrugSpider(scrapy.Spider):
    name = 'drug1'
    allowed_domains = ['www.yaopinnet.com']
    start_urls = ['http://www.yaopinnet.com/huayao/hy4549k.htm']
    
    def parse(self,response):
#        lis=response.xpath("//span[contains(./text(), '商 品 名')]/following::text()[1]").extract()[0] ##brand_name
#        lis=response.xpath("//span[contains(./text(), '批准文号')]/following::text()[1]").extract()[0] ##approval_number
#        lis=response.xpath("//span[contains(./text(), '生产单位')]/following::text()[1]").extract()[0]  ##company
#        lis=response.xpath("//span[contains(./text(), '生产地址')]/following::text()[1]").extract()[0] ##brand_factory
#        lis=response.xpath("//span[contains(./text(), '剂　　型')]/following::text()[1]").extract()[0] ##dosage_form
#        lis=response.xpath("//span[contains(./text(), '规　　格')]/following::text()[1]").extract()[0] ##specification
        base_url='http://www.yaopinnet.com/huayao/'
        more_url=response.xpath("//strong[contains(text(),'查看更多')]/following::a/@href").extract()[0]
        more_url_all=base_url+more_url
#        lis=response.xpath("//strong[contains(text(),'查看更多')]/following::a/@href").extract()[0] ##standard_code
        print('---------------------')
        print('shangpinming is '+more_url_all)
        print('---------------------')