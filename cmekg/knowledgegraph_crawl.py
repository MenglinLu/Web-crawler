# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:18:25 2019

@author: Jolin
"""
import urllib
import json
import collections
from urllib.parse import quote

def parser(url,level1,pattern=1):
    response=urllib.request.urlopen(url)
    rrr=response.read()
    json_rrr=json.loads(rrr)
    categories=json_rrr['categories']
    dict_category={}
    for i in range(len(categories)):
        dict_category[i]=categories[i]['name']
    
    res_dict=collections.OrderedDict()
    if(pattern==1):
        res_dict['class']=level1
    node=json_rrr['node']
    for key, value in dict_category.items():
        value=value.strip()
        if(value=='中心词'):
            for i in node:
                category_i=dict_category[i['category']]
                if(category_i=='中心词'):
                    res_dict['中心词']=i['label']
                    break
        if(value=='关系'):
            continue
        if(value!='中心词' and value!='关系'):
            ress=[]
            for i in node:
                category_i=dict_category[i['category']]
                if(category_i==value):
                    ress.append(i['label'])
            res_dict[value]=ress
    jsons = json.dumps(res_dict,ensure_ascii=False)
    return jsons

import pandas as pd
from tqdm import tqdm
import time
##疾病
f=open(r'E:/crawl_graph/disease.json','a',encoding='utf-8')
df=pd.read_csv(r'E:/crawl_graph/disease.csv',header=0)
for i in tqdm(range(len(df))[1020:]):
    if(i%60==0):
        time.sleep(2)
    name_i=df.iloc[i,0]
    class_i=df.iloc[i,1]
    base_url='http://zstp.pcl.ac.cn:8002/knowledge?name='
    url=base_url+quote(name_i,encoding='utf-8')+'&tree_type='+quote('疾病',encoding='utf-8') 
    str_i=parser(url,class_i,1)
    f.write(str_i+'\n')
f.close()
##药物
f=open(r'E:/crawl_graph/drug.json','w',encoding='utf-8')
df=pd.read_csv(r'E:/crawl_graph/drug.csv',header=0)
for i in tqdm(range(len(df))):
    name_i=df.iloc[i,0]
    class_i=df.iloc[i,1]
    base_url='http://zstp.pcl.ac.cn:8002/knowledge?name='
    url=base_url+quote(name_i,encoding='utf-8')+'&tree_type='+quote('药物',encoding='utf-8') 
    str_i=parser(url,class_i,1)
    f.write(str_i+'\n')
f.close()
##症状
f=open(r'E:/crawl_graph/symptom.json','a',encoding='utf-8')
df=pd.read_csv(r'E:/crawl_graph/symptom.csv',header=0)
for i in tqdm(range(len(df))[1015:]):
    if(i%60==0):
        time.sleep(2)
    name_i=df.iloc[i,0]
    class_i=df.iloc[i,1]
    base_url='http://zstp.pcl.ac.cn:8002/knowledge?name='
    url=base_url+quote(name_i,encoding='utf-8')+'&tree_type='+quote('症状',encoding='utf-8') 
    str_i=parser(url,class_i,0)
    f.write(str_i+'\n')
f.close()
##诊疗
f=open(r'E:/crawl_graph/treatment.json','a',encoding='utf-8')
df=pd.read_csv(r'E:/crawl_graph/treat.csv',header=0)
for i in tqdm(range(len(df))[2082:]):
    name_i=df.iloc[i,0]
    if(i%60==0):
        time.sleep(2)
    class_i=df.iloc[i,1]
    base_url='http://zstp.pcl.ac.cn:8002/knowledge?name='
    url=base_url+quote(name_i,encoding='utf-8')+'&tree_type='+quote('检查诊疗技术',encoding='utf-8') 
    str_i=parser(url,class_i,0)
    f.write(str_i+'\n')
f.close()
    


   
        
            
        
    
    
    