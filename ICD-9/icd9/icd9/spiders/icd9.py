# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:01:46 2019

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
    executable_path=r"E:\药物数据库\chromedriver.exe",
    chrome_options=chrome_option
)

driver.get(url='http://term.omaha.org.cn/?/icd9/0f5a185b61754d24b43caac2d869ee60')
response=Selector(text=driver.page_source)
f=open('E:\\res.json','w',encoding='utf-8')
base_url='http://term.omaha.org.cn/?/icd9/'
resinfo=dict()
for level1url in response.xpath('//tr[@class="detailSub"]/@data-num').extract()[4:]:
    level1url_all=base_url+level1url
    driver.get(url=level1url_all)
    time.sleep(3)
    response1=Selector(text=driver.page_source)
    resinfo['level1']=response1.xpath("//span[@class='detailName']/text()").extract()[0]
    print(resinfo['level1']+' ')
    for level2url in response1.xpath('//tr[@class="detailSub"]/@data-num').extract():
        level2url_all=base_url+level2url
        driver.get(url='https://www.baidu.com/')
        driver.get(url=level2url_all)
        time.sleep(3)
        response2=Selector(text=driver.page_source)
        resinfo['level2']=response2.xpath("//span[@class='detailName']/text()").extract()[0]
        print(resinfo['level2'])
        print('\n')
        ######
        version_list2=dict()
        text_version2=response2.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
        text_version_text2=response2.xpath("//tbody[contains(@class,'version')]").extract()
        text_version_text2=[reg.sub(' ',i) for i in text_version_text2]
        for i in range(len(text_version2)):
            text_version_i=text_version_text2[i]
            version_list2[text_version2[i]]=text_version_i
        text_version_all2=''.join(text_version_text2).strip()   
        ######
        if(text_version_all2.strip()!=""):
            resinfo['info']=version_list2
            res_str=json.dumps(resinfo,ensure_ascii=False)
            f.write(res_str)
            f.write('\n')
        if(len(response2.xpath('//tr[@class="detailSub"]/@data-num').extract())<0):
            del resinfo
            break
        else:
            for level3url in response2.xpath('//tr[@class="detailSub"]/@data-num').extract():
                level3url_all=base_url+level3url
                driver.get(url='https://www.baidu.com/')
                driver.get(url=level3url_all)
                time.sleep(3)
#                time.sleep(3)
                response3=Selector(text=driver.page_source)
                resinfo['level3']=response3.xpath("//span[@class='detailName']/text()").extract()[0]
                ######
                version_list3=dict()
                text_version3=response3.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                text_version_text3=response3.xpath("//tbody[contains(@class,'version')]").extract()
                text_version_text3=[reg.sub(' ',i) for i in text_version_text3]
                for i in range(len(text_version3)):
                    text_version_i=text_version_text3[i]
                    version_list3[text_version3[i]]=text_version_i
                text_version_all3=''.join(text_version_text3).strip()   
                ######
                if(text_version_all3.strip()!=""):
                    resinfo['info']=version_list3
                    res_str=json.dumps(resinfo,ensure_ascii=False)
                    f.write(res_str)
                    f.write('\n')
                if(len(response3.xpath('//tr[@class="detailSub"]/@data-num').extract())>0):
                    del resinfo
                    break
                else: 
                    for level4url in response3.xpath('//tr[@class="detailSub"]/@data-num').extract():
                        level4url_all=base_url+level4url
                        driver.get(url='https://www.baidu.com/')
                        driver.get(url=level4url_all)
                        time.sleep(3)
                        response4=Selector(text=driver.page_source)
                        resinfo['level4']=response4.xpath("//span[@class='detailName']/text()").extract()[0]
                        ######
                        version_list4=dict()
                        text_version4=response4.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                        text_version_text4=response4.xpath("//tbody[contains(@class,'version')]").extract()
                        text_version_text4=[reg.sub(' ',i) for i in text_version_text4]
                        for i in range(len(text_version4)):
                            text_version_i=text_version_text4[i]
                            version_list4[text_version4[i]]=text_version_i
                        text_version_all4=''.join(text_version_text4).strip()  
                        ######
                        if(text_version_all4.strip()!=""):
                            resinfo['info']=version_list4
                            res_str=json.dumps(resinfo,ensure_ascii=False)
                            f.write(res_str)
                            f.write('\n')
                        if(len(response4.xpath('//tr[@class="detailSub"]/@data-num').extract())<0):
                            del resinfo
                            break
                        else:
                            for level5url in response4.xpath('//tr[@class="detailSub"]/@data-num').extract():
                                level5url_all=base_url+level5url
                                driver.get(url='https://www.baidu.com/')
                                driver.get(url=level5url_all)
                                time.sleep(3)
                                response5=Selector(text=driver.page_source)
                                resinfo['level5']=response5.xpath("//span[@class='detailName']/text()")
                                ######
                                version_list5=dict()
                                text_version5=response5.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                                text_version_text5=response5.xpath("//tbody[contains(@class,'version')]").extract()
                                text_version_text5=[reg.sub(' ',i) for i in text_version_text5]
                                for i in range(len(text_version5)):
                                    text_version_i=text_version_text5[i]
                                    version_list5[text_version5[i]]=text_version_i
                                text_version_all5=''.join(text_version_text5).strip()  
                                ######
                                if(text_version_all5.strip()!=""):
                                    resinfo['info']=version_list5
                                    res_str=json.dumps(resinfo,ensure_ascii=False)
                                    f.write(res_str)
                                    f.write('\n')
                                if(len(response5.xpath('//tr[@class="detailSub"]/@data-num').extract())<0):
                                    del resinfo
                                    break
                                else:
                                    for level6url in response5.xpath('//tr[@class="detailSub"]/@data-num').extract():
                                        level6url_all=base_url+level6url
                                        driver.get(url='https://www.baidu.com/')
                                        driver.get(url=level6url_all)
                                        time.sleep(3)
                                        response6=Selector(text=driver.page_source)
                                        resinfo['level6']=response6.xpath("//span[@class='detailName']/text()")
                                        ######
                                        version_list6=dict()
                                        text_version6=response6.xpath("//div[@class='detail-version']/div/div/span/text()").extract()
                                        text_version_text6=response6.xpath("//tbody[contains(@class,'version')]").extract()
                                        text_version_text6=[reg.sub(' ',i) for i in text_version_text6]
                                        for i in range(len(text_version6)):
                                            text_version_i=text_version_text6[i]
                                            version_list6[text_version6[i]]=text_version_i
                                        text_version_all6=''.join(text_version_text6).strip()  
                                        ######
                                        if(text_version_all6.strip()!=""):
                                            resinfo['info']=version_list6
                                            res_str=json.dumps(resinfo,ensure_ascii=False)
                                            f.write(res_str)
                                            f.write('\n')   
f.close()
driver.close()
                                

                
#            
#        
#a=response.xpath('//tr[@class="detailSub"]/@data-num')
#print(a)
#f=open('E:\\res.txt','w',encoding='utf-8')
#f.write(driver.page_source)
#f.close()
#
#
#
#
#
##driver.set_page_load_timeout(100)
## url = "http://qy1.sfda.gov.cn/datasearch/face3/dir.html"
#res=dict()
#f=open('E:\drug_guochan2.json','a')
#for k in range(10001,11127):#86
#    driver.get(url='http://app1.sfda.gov.cn/datasearch/face3/search.jsp?tableId=25&bcId=124356560303886909015737447882&curstart=%d' % k)
#    response = Selector(text=driver.page_source)
#    datas = response.css('a::text').extract()
#    for drug in datas:
#        idd=drug.split('.')[0]
#        info=drug.encode('utf-8').replace(idd.encode('utf-8')+'.','').decode('utf-8')
#        res['info']=info.split(' (')[1]
#        res['genenral_name']=info.split(' (')[0]
#        res_str=json.dumps(res,ensure_ascii=False)
#        a=res_str.encode('utf-8')
#        a=a.replace(')','')
#        f.write(a)
#        f.write('\n')
#        
#    if(k%100==0):
#        print('now is the '+str(k)+' page')
##    time.sleep(0.5)
#f.close()
#driver.close()