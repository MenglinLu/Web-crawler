# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:40:31 2019

@author: eileenlu
"""

from selenium import webdriver
import json
import time
import re
from scrapy import Selector

def get_DDD(resp):
    col=['DDD','U','Adm.R','Note']
    row=resp.xpath("//div[@class='detail-frequence']/table[@class='subContent']/tbody/tr").extract()
    if(len(row)==0):
        res=[{'DDD':'','U':'','Adm.R':'','Note':''}]
    else:
        res=[]
        for i in row:
            row_i=[jj.replace('<tr>','').replace('</td>','').replace('<td>','').replace('</tr>','') for jj in i.split('</td><td>')]
            res_i=dict()
            for k in range(len(col)):
                res_i[col[k]]=row_i[k]
            res.append(res_i)
    return res

reg = re.compile('<[^>]*>')

f=open(r'E:\atc.json','w',encoding='utf-8')

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400"')
prefs = {"profile.managed_default_content_settings.images": 2}
driver = webdriver.Chrome(
    executable_path="G:chromedriver.exe",
    options=chrome_option
)

base_url='http://term.omaha.org.cn/?/atc/'
driver.get(url='http://term.omaha.org.cn/?/atc/1')
time.sleep(3)
response=Selector(text=driver.page_source)

for elem_i_level1 in response.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract():
    elem_i_level1_all=base_url+elem_i_level1
    driver.get('https://www.baidu.com/')
    driver.get(elem_i_level1_all)
    time.sleep(3)
    response1=Selector(text=driver.page_source)
    
    level1_list = response1.xpath("//span[@class='detailName']/text()").extract()
    while(len(level1_list)==0):
        driver.get(elem_i_level1_all)
        time.sleep(3)
        response1=Selector(text=driver.page_source)
        level1_list = response1.xpath("//span[@class='detailName']/text()").extract()
    level1=level1_list[0]
    
    while(level1=='解剖学治疗学及化学分类'):
        driver.get('https://www.baidu.com/')
        driver.get(elem_i_level1_all)
        time.sleep(3)
        response1=Selector(text=driver.page_source)
        
        level1_list = response1.xpath("//span[@class='detailName']/text()").extract()
        while(len(level1_list)==0):
            driver.get(elem_i_level1_all)
            time.sleep(3)
            response1=Selector(text=driver.page_source)
            level1_list = response1.xpath("//span[@class='detailName']/text()").extract()
        level1=level1_list[0]
    
    print('level1: '+level1)
    
    level1_res=get_DDD(response1)
    elem_url_level2=response1.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
    if((''.join(list(level1_res[0].values())).strip()!='') or (''.join(list(level1_res[0].values())).strip()=='' and len(elem_url_level2)==0)):
        resinfo=dict()
        resinfo['level1']=level1
        resinfo['DDD']=level1_res
        res_str=json.dumps(resinfo,ensure_ascii=False)
        f.write(res_str)
        f.write('\n')
        
    if(len(elem_url_level2)>0):
        #####################################level2#######################################
        for elem_i_level2 in elem_url_level2:
            elem_i_level2_all=base_url+elem_i_level2
            driver.get('https://www.baidu.com/')
            driver.get(elem_i_level2_all)
            time.sleep(3)
            response2=Selector(text=driver.page_source)
            
            level2_list = response2.xpath("//span[@class='detailName']/text()").extract()
            while(len(level2_list)==0):
                driver.get(elem_i_level2_all)
                time.sleep(3)
                response2=Selector(text=driver.page_source)
                level2_list = response2.xpath("//span[@class='detailName']/text()").extract()
            level2=level2_list[0]
            
            while(level2=='解剖学治疗学及化学分类'):
                driver.get('https://www.baidu.com/')
                driver.get(elem_i_level2_all)
                time.sleep(3)
                response2=Selector(text=driver.page_source)
                
                level2_list = response2.xpath("//span[@class='detailName']/text()").extract()
                while(len(level2_list)==0):
                    driver.get(elem_i_level2_all)
                    time.sleep(3)
                    response2=Selector(text=driver.page_source)
                    level2_list = response2.xpath("//span[@class='detailName']/text()").extract()
                level2=level2_list[0]
            
            print('level2: '+level2)
            
            level2_res=get_DDD(response2)
            elem_url_level3=response2.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
            if((''.join(list(level2_res[0].values())).strip()!='') or (''.join(list(level2_res[0].values())).strip()=='' and len(elem_url_level3)==0)):
                resinfo=dict()
                resinfo['level1']=level1
                resinfo['level2']=level2
                resinfo['DDD']=level2_res
                res_str=json.dumps(resinfo,ensure_ascii=False)
                f.write(res_str)
                f.write('\n')
            if(len(elem_url_level3)>0):
                for elem_i_level3 in elem_url_level3:
                    elem_i_level3_all=base_url+elem_i_level3
                    driver.get('https://www.baidu.com/')
                    driver.get(elem_i_level3_all)
                    time.sleep(3)
                    response3=Selector(text=driver.page_source)
                    
                    level3_list = response3.xpath("//span[@class='detailName']/text()").extract()
                    while(len(level3_list)==0):
                        driver.get(elem_i_level3_all)
                        time.sleep(3)
                        response3=Selector(text=driver.page_source)
                        level3_list = response3.xpath("//span[@class='detailName']/text()").extract()
                    level3=level3_list[0]
                    
                    while(level3=='解剖学治疗学及化学分类'):
                        driver.get('https://www.baidu.com/')
                        driver.get(elem_i_level3_all)
                        time.sleep(3)
                        response3=Selector(text=driver.page_source)
                        
                        level3_list = response3.xpath("//span[@class='detailName']/text()").extract()
                        while(len(level3_list)==0):
                            driver.get(elem_i_level3_all)
                            time.sleep(3)
                            response3=Selector(text=driver.page_source)
                            level3_list = response3.xpath("//span[@class='detailName']/text()").extract()
                        level3=level3_list[0]
                    
                    print('level3: '+level3)
                    
                    level3_res=get_DDD(response3)
                    elem_url_level4=response3.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
                    if((''.join(list(level3_res[0].values())).strip()!='') or (''.join(list(level3_res[0].values())).strip()=='' and len(elem_url_level4)==0)):
                        resinfo=dict()
                        resinfo['level1']=level1
                        resinfo['level2']=level2
                        resinfo['level3']=level3
                        resinfo['DDD']=level3_res
                        res_str=json.dumps(resinfo,ensure_ascii=False)
                        f.write(res_str)
                        f.write('\n')
                    if(len(elem_url_level4)>0):
                        for elem_i_level4 in elem_url_level4:
                            elem_i_level4_all=base_url+elem_i_level4
                            driver.get('https://www.baidu.com/')
                            driver.get(elem_i_level4_all)
                            time.sleep(3)
                            response4=Selector(text=driver.page_source)
                            
                            level4_list = response4.xpath("//span[@class='detailName']/text()").extract()
                            while(len(level4_list)==0):
                                driver.get(elem_i_level4_all)
                                time.sleep(3)
                                response4=Selector(text=driver.page_source)
                                level4_list = response4.xpath("//span[@class='detailName']/text()").extract()
                            level4=level4_list[0]
                            
                            while(level4=='解剖学治疗学及化学分类'):
                                driver.get('https://www.baidu.com/')
                                driver.get(elem_i_level4_all)
                                time.sleep(3)
                                response4=Selector(text=driver.page_source)
                                
                                level4_list = response4.xpath("//span[@class='detailName']/text()").extract()
                                while(len(level4_list)==0):
                                    driver.get(elem_i_level4_all)
                                    time.sleep(3)
                                    response4=Selector(text=driver.page_source)
                                    level4_list = response4.xpath("//span[@class='detailName']/text()").extract()
                                level4=level4_list[0]
                            
                            print('level4: '+level4)
                            
                            level4_res=get_DDD(response4)
                            elem_url_level5=response4.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
                            if((''.join(list(level4_res[0].values())).strip()!='') or (''.join(list(level4_res[0].values())).strip()=='' and len(elem_url_level5)==0)):
                                resinfo=dict()
                                resinfo['level1']=level1
                                resinfo['level2']=level2
                                resinfo['level3']=level3
                                resinfo['level4']=level4
                                resinfo['DDD']=level4_res
                                res_str=json.dumps(resinfo,ensure_ascii=False)
                                f.write(res_str)
                                f.write('\n')
                            if(len(elem_url_level5)>0):
                                for elem_i_level5 in elem_url_level5:
                                    elem_i_level5_all=base_url+elem_i_level5
                                    driver.get('https://www.baidu.com/')
                                    driver.get(elem_i_level5_all)
                                    time.sleep(3)
                                    response5=Selector(text=driver.page_source)
                                    
                                    level5_list = response5.xpath("//span[@class='detailName']/text()").extract()
                                    while(len(level5_list)==0):
                                        driver.get(elem_i_level5_all)
                                        time.sleep(3)
                                        response5=Selector(text=driver.page_source)
                                        level5_list = response5.xpath("//span[@class='detailName']/text()").extract()
                                    level5=level5_list[0]
                                    
                                    while(level5=='解剖学治疗学及化学分类'):
                                        driver.get('https://www.baidu.com/')
                                        driver.get(elem_i_level5_all)
                                        time.sleep(3)
                                        response5=Selector(text=driver.page_source)
                                        
                                        level5_list = response5.xpath("//span[@class='detailName']/text()").extract()
                                        while(len(level5_list)==0):
                                            driver.get(elem_i_level5_all)
                                            time.sleep(3)
                                            response5=Selector(text=driver.page_source)
                                            level5_list = response5.xpath("//span[@class='detailName']/text()").extract()
                                        level5=level5_list[0]
                                    
                                    print('level5: '+level5)
                                    
                                    level5_res=get_DDD(response5)
                                    elem_url_level6=response5.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
                                    if((''.join(list(level5_res[0].values())).strip()!='') or (''.join(list(level5_res[0].values())).strip()=='' and len(elem_url_level6)==0)):
                                        resinfo=dict()
                                        resinfo['level1']=level1
                                        resinfo['level2']=level2
                                        resinfo['level3']=level3
                                        resinfo['level4']=level4
                                        resinfo['level5']=level5
                                        resinfo['DDD']=level5_res
                                        res_str=json.dumps(resinfo,ensure_ascii=False)
                                        f.write(res_str)
                                        f.write('\n')
                                    if(len(elem_url_level6)>0):
                                        for elem_i_level6 in elem_url_level6:
                                            elem_i_level6_all=base_url+elem_i_level6
                                            driver.get('https://www.baidu.com/')
                                            driver.get(elem_i_level6_all)
                                            time.sleep(3)
                                            response6=Selector(text=driver.page_source)
                                            
                                            level6_list = response6.xpath("//span[@class='detailName']/text()").extract()
                                            while(len(level6_list)==0):
                                                driver.get(elem_i_level6_all)
                                                time.sleep(3)
                                                response6=Selector(text=driver.page_source)
                                                level6_list = response6.xpath("//span[@class='detailName']/text()").extract()
                                            level6=level6_list[0]
                                            
                                            while(level6=='解剖学治疗学及化学分类'):
                                                driver.get('https://www.baidu.com/')
                                                driver.get(elem_i_level6_all)
                                                time.sleep(3)
                                                response6=Selector(text=driver.page_source)
                                                
                                                level6_list = response6.xpath("//span[@class='detailName']/text()").extract()
                                                while(len(level6_list)==0):
                                                    driver.get(elem_i_level6_all)
                                                    time.sleep(3)
                                                    response6=Selector(text=driver.page_source)
                                                    level6_list = response6.xpath("//span[@class='detailName']/text()").extract()
                                                level6=level6_list[0]
                                            
                                            print('level6: '+level6)
                                            
                                            level6_res=get_DDD(response6)
                                            elem_url_level7=response6.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
                                            if((''.join(list(level6_res[0].values())).strip()!='') or (''.join(list(level6_res[0].values())).strip()=='' and len(elem_url_level7)==0)):
                                                resinfo=dict()
                                                resinfo['level1']=level1
                                                resinfo['level2']=level2
                                                resinfo['level3']=level3
                                                resinfo['level4']=level4
                                                resinfo['level5']=level5
                                                resinfo['level6']=level6
                                                resinfo['DDD']=level6_res
                                                res_str=json.dumps(resinfo,ensure_ascii=False)
                                                f.write(res_str)
                                                f.write('\n')
                                            if(len(elem_url_level7)>0):
                                                for elem_i_level7 in elem_url_level7:
                                                    elem_i_level7_all=base_url+elem_i_level7
                                                    driver.get('https://www.baidu.com/')
                                                    driver.get(elem_i_level7_all)
                                                    time.sleep(3)
                                                    response7=Selector(text=driver.page_source)
                                                    
                                                    level7_list = response7.xpath("//span[@class='detailName']/text()").extract()
                                                    while(len(level7_list)==0):
                                                        driver.get(elem_i_level7_all)
                                                        time.sleep(3)
                                                        response7=Selector(text=driver.page_source)
                                                        level7_list = response7.xpath("//span[@class='detailName']/text()").extract()
                                                    level7=level7_list[0]
                                                    
                                                    while(level7=='解剖学治疗学及化学分类'):
                                                        driver.get('https://www.baidu.com/')
                                                        driver.get(elem_i_level7_all)
                                                        time.sleep(3)
                                                        response7=Selector(text=driver.page_source)
                                                        
                                                        level7_list = response7.xpath("//span[@class='detailName']/text()").extract()
                                                        while(len(level7_list)==0):
                                                            driver.get(elem_i_level7_all)
                                                            time.sleep(3)
                                                            response7=Selector(text=driver.page_source)
                                                            level7_list = response7.xpath("//span[@class='detailName']/text()").extract()
                                                        level7=level7_list[0]
                                                     
                                                    print('level7: '+level7)
                                                    
                                                    level7_res=get_DDD(response7)
                                                    elem_url_level8=response7.xpath("//div[@class='detail-subordinate' and @style='display: block;']/table[@class='subContent']/tbody/tr[@class='detailSub']/@data-num").extract()
                                                    if(True):
                                                        resinfo=dict()
                                                        resinfo['level1']=level1
                                                        resinfo['level2']=level2
                                                        resinfo['level3']=level3
                                                        resinfo['level4']=level4
                                                        resinfo['level5']=level5
                                                        resinfo['level6']=level6
                                                        resinfo['level7']=level7
                                                        resinfo['DDD']=level7_res
                                                        res_str=json.dumps(resinfo,ensure_ascii=False)
                                                        f.write(res_str)
                                                        f.write('\n')
                                                        
f.close()
        
        
    
    