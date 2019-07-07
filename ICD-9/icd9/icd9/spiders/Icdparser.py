# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:38:44 2019

@author: eileenlu
"""

from icd9.items import Icd9Item
import scrapy 

class IcdSpider(scrapy.Spider):
    name = 'icdproc'
    allowed_domains = ['omaha.org.cn']
    start_urls = ['http://term.omaha.org.cn/?/icd9/0f5a185b61754d24b43caac2d869ee60']
    
    def parse(self,response):
        print('aaaaaaaaaaaa')
        base_url='http://term.omaha.org.cn/?/icd9/'
        print(response.body.decode('utf-8'))
        for catrgory_url in response.css("tbody").extract():
            print('bbbbbbb')
            print (type(catrgory_url))
#            letter_url_all=base_url+letter_url
#            yield scrapy.Request(letter_url_all,callback=self.parse1)
