# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:40:31 2019

@author: eileenlu
"""

from selenium import webdriver
from scrapy.selector import Selector
import json
import time
import re

reg = re.compile('<[^>]*>')

chrome_option = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
driver = webdriver.Chrome(
    executable_path="G:\\chromedriver.exe",
    options=chrome_option
)

driver.get(url='http://term.omaha.org.cn/?/icd/b53d58a75ecc4987a989a970b67317e4')
response=Selector(text=driver.page_source)
f=open(r'E:\res_icd10.json','w',encoding='utf-8')
base_url='http://term.omaha.org.cn/?/icd/'
for level1url in response.xpath('//tr[@class="detailSub"]/@data-num').extract():
    level1url_all=base_url+level1url
    driver.get(url=level1url_all)
    time.sleep(3)
    response1=Selector(text=driver.page_source)
    level1=response1.xpath("//span[@class='detailName']/text()").extract()[0]
    print(level1)
    version_list2=dict()
    text_version2=response1.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
    text_version_text2=response1.xpath("//tbody[contains(@class,'version')]").extract()
    
    for i in text_version_text2:
        print(str(i))
        break
    break
    
    
    text_version_text2=[reg.sub(' ',i) for i in text_version_text2]
    for i in range(len(text_version2)):
        text_version_i=text_version_text2[i]
        version_list2[text_version2[i]]=text_version_i
    text_version_all2=''.join(text_version_text2).strip()
    if(text_version_all2.strip()!=""):
        resinfo=dict()
        resinfo['level1']=level1
        resinfo['info']=version_list2
        res_str=json.dumps(resinfo,ensure_ascii=False)
        f.write(res_str)
        f.write('\n')
    if(text_version_all2.strip()=="" and len(response1.xpath('//tr[@class="detailSub"]/@data-num').extract()) == 0):
        resinfo=dict()
        resinfo['level1']=level1
        resinfo['info']=""
        res_str=json.dumps(resinfo,ensure_ascii=False)
        f.write(res_str)
        f.write('\n')
    if(len(response1.xpath('//tr[@class="detailSub"]/@data-num').extract())>0):
        for level2url in response1.xpath('//tr[@class="detailSub"]/@data-num').extract():
            level2url_all=base_url+level2url
            driver.get(url='https://www.baidu.com/')
            driver.get(url=level2url_all)
            time.sleep(3)
            response2=Selector(text=driver.page_source)
            level2=response2.xpath("//span[@class='detailName']/text()").extract()[0]
            print(level2)
            version_list3=dict()
            text_version3=response2.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
            text_version_text3=response2.xpath("//tbody[contains(@class,'version')]").extract()
            text_version_text3=[reg.sub(' ',i) for i in text_version_text3]
            for i in range(len(text_version3)):
                text_version_i=text_version_text3[i]
                version_list3[text_version3[i]]=text_version_i
            text_version_all3=''.join(text_version_text3).strip() 
            if(text_version_all3.strip()!=""):
                resinfo=dict()
                resinfo['level1']=level1
                resinfo['level2']=level2
                resinfo['info']=version_list3
                res_str=json.dumps(resinfo,ensure_ascii=False)
                f.write(res_str)
                f.write('\n')
            if(text_version_all3.strip()=="" and len(response2.xpath('//tr[@class="detailSub"]/@data-num').extract()) == 0):
                resinfo=dict()
                resinfo['level1']=level1
                resinfo['level2']=level2
                resinfo['info']=""
                res_str=json.dumps(resinfo,ensure_ascii=False)
                f.write(res_str)
                f.write('\n')
            if(len(response2.xpath('//tr[@class="detailSub"]/@data-num').extract())>0):
                for level3url in response2.xpath('//tr[@class="detailSub"]/@data-num').extract():
                    level3url_all=base_url+level3url
                    driver.get(url='https://www.baidu.com/')
                    driver.get(url=level3url_all)
                    time.sleep(3)
                    response3=Selector(text=driver.page_source)
                    level3=response3.xpath("//span[@class='detailName']/text()").extract()[0]
                    print(level3)
                    version_list4=dict()
                    text_version4=response3.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                    text_version_text4=response3.xpath("//tbody[contains(@class,'version')]").extract()
                    text_version_text4=[reg.sub(' ',i) for i in text_version_text4]
                    for i in range(len(text_version4)):
                        text_version_i=text_version_text4[i]
                        version_list4[text_version4[i]]=text_version_i
                        text_version_all4=''.join(text_version_text4).strip()   
                    if(text_version_all4.strip()!=""):
                        resinfo=dict()
                        resinfo['level1']=level1
                        resinfo['level2']=level2
                        resinfo['level3']=level3
                        resinfo['info']=version_list4
                        res_str=json.dumps(resinfo,ensure_ascii=False)
                        f.write(res_str)
                        f.write('\n')
                    if(text_version_all4.strip()=="" and len(response3.xpath('//tr[@class="detailSub"]/@data-num').extract()) == 0):
                        resinfo=dict()
                        resinfo['level1']=level1
                        resinfo['level2']=level2
                        resinfo['level3']=level3
                        resinfo['info']=""
                        res_str=json.dumps(resinfo,ensure_ascii=False)
                        f.write(res_str)
                        f.write('\n')
                    if(len(response3.xpath('//tr[@class="detailSub"]/@data-num').extract())>0):
                        for level4url in response3.xpath('//tr[@class="detailSub"]/@data-num').extract():
                            level4url_all=base_url+level4url
                            driver.get(url='https://www.baidu.com/')
                            driver.get(url=level4url_all)
                            time.sleep(3)
                            response4=Selector(text=driver.page_source)
                            level4=response4.xpath("//span[@class='detailName']/text()").extract()[0]
                            print(level4)
                            version_list5=dict()
                            text_version5=response4.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                            text_version_text5=response4.xpath("//tbody[contains(@class,'version')]").extract()
                            text_version_text5=[reg.sub(' ',i) for i in text_version_text5]
                            for i in range(len(text_version5)):
                                text_version_i=text_version_text5[i]
                                version_list5[text_version5[i]]=text_version_i
                            text_version_all5=''.join(text_version_text5).strip()  
                            if(text_version_all5.strip()!=""):
                                resinfo=dict()
                                resinfo['level1']=level1
                                resinfo['level2']=level2
                                resinfo['level3']=level3
                                resinfo['level4']=level4
                                resinfo['info']=version_list5
                                res_str=json.dumps(resinfo,ensure_ascii=False)
                                f.write(res_str)
                                f.write('\n')
                            if(text_version_all5.strip()=="" and len(response4.xpath('//tr[@class="detailSub"]/@data-num').extract()) == 0):
                                resinfo=dict()
                                resinfo['level1']=level1
                                resinfo['level2']=level2
                                resinfo['level3']=level3
                                resinfo['level4']=level4
                                resinfo['info']=""
                                res_str=json.dumps(resinfo,ensure_ascii=False)
                                f.write(res_str)
                                f.write('\n')
                            if(len(response4.xpath('//tr[@class="detailSub"]/@data-num').extract())>0):
                                for level5url in response4.xpath('//tr[@class="detailSub"]/@data-num').extract():
                                    level5url_all=base_url+level5url
                                    driver.get(url='https://www.baidu.com/')
                                    driver.get(url=level5url_all)
                                    time.sleep(3)
                                    response5=Selector(text=driver.page_source)
                                    level5=response5.xpath("//span[@class='detailName']/text()").extract()[0]
                                    print(level5)
                                    version_list6=dict()
                                    text_version6=response5.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                                    text_version_text6=response5.xpath("//tbody[contains(@class,'version')]").extract()
                                    text_version_text6=[reg.sub(' ',i) for i in text_version_text6]
                                    for i in range(len(text_version6)):
                                        text_version_i=text_version_text6[i]
                                        version_list6[text_version6[i]]=text_version_i
                                    text_version_all6=''.join(text_version_text6).strip()   
                                    if(text_version_all6.strip()!=""):
                                        resinfo=dict()
                                        resinfo['level1']=level1
                                        resinfo['level2']=level2
                                        resinfo['level3']=level3
                                        resinfo['level4']=level4
                                        resinfo['level5']=level5
                                        resinfo['info']=version_list6
                                        res_str=json.dumps(resinfo,ensure_ascii=False)
                                        f.write(res_str)
                                        f.write('\n')
                                    else:
                                        resinfo=dict()
                                        resinfo['level1']=level1
                                        resinfo['level2']=level2
                                        resinfo['level3']=level3
                                        resinfo['level4']=level4
                                        resinfo['level5']=level5
                                        resinfo['info']=""
                                        res_str=json.dumps(resinfo,ensure_ascii=False)
                                        f.write(res_str)
                                        f.write('\n')
f.close()