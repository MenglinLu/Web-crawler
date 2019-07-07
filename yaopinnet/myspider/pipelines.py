# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

import json
import codecs

class JsonMyspiderPipeline(object):
    def __init__(self):
        self.file=codecs.open('drugs_json_zhongyao.json','w',encoding='utf-8')
    
    def process_item(self,item,spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()

class MyspiderPipeline(object):
    
    def process_item(self, item, spider):
        host=settings['MYSQL_HOSTS']
        user=settings['MYSQL_USER']
        psd=settings['MYSQL_PASSWORD']
        db=settings['MYSQL_DB']
#        c=settings['CHARSET']
        port=settings['MYSQL_PORT']
        
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,port=port)
        cue=con.cursor()
        print('mysql connet success')
        
        try:
            general_name="'"+item['general_name'].replace(' ','').strip(',').strip()+"'"
            brand_name="'"+item['brand_name'].replace(' ','').strip(',').strip()+"'"
            approval_number="'"+item['approval_number'].replace(' ','').strip(',').strip()+"'"
            standard_code="'"+item['standard_code'].replace(' ','').strip(',').strip()+"'"
            company="'"+item['company'].replace(' ','').strip(',').strip()+"'"
            brand_factory="'"+item['brand_factory'].replace(' ','').strip(',').strip()+"'"
            is_cm="'"+item['is_cm'].replace(' ','').strip(',').strip()+"'"
            ingredient="'"+item['ingredient'].replace(' ','').strip(',').strip()+"'"
            character="'"+item['character'].replace(' ','').strip(',').strip()+"'"
            function="'"+item['function'].replace(' ','').strip(',').strip()+"'"
            specification="'"+item['specification'].replace(' ','').strip(',').strip()+"'"
            dosage_form="'"+item['dosage_form'].replace(' ','').strip(',').strip()+"'"
            usage="'"+item['usage'].replace(' ','').strip(',').strip()+"'"
            sideaffect="'"+item['sideaffect'].replace(' ','').strip(',').strip()+"'"
            contraindication="'"+item['contraindication'].replace(' ','').strip(',').strip()+"'"
            announcement="'"+item['announcement'].replace(' ','').strip(',').strip()+"'"
            pregnant="'"+item['pregnant'].replace(' ','').strip(',').strip()+"'"
            child="'"+item['child'].replace(' ','').strip(',').strip()+"'"
            elder="'"+item['elder'].replace(' ','').strip(',').strip()+"'"
            interaction="'"+item['interaction'].replace(' ','').strip(',').strip()+"'"
            overdose="'"+item['overdose'].replace(' ','').strip(',').strip()+"'"
            pharmacological_action="'"+item['pharmacological_action'].replace(' ','').strip(',').strip()+"'"
            pharmacokinetics="'"+item['pharmacokinetics'].replace(' ','').strip(',').strip()+"'"
            storage="'"+item['storage'].replace(' ','').strip(',').strip()+"'"
            packaging="'"+item['packaging'].replace(' ','').strip(',').strip()+"'"
            valid_date="'"+item['valid_date'].replace(' ','').strip(',').strip()+"'"
            sqlstr="insert into kg_intern.medicine_new (general_name,brand_name,isbn,standard_code,company,production_address,is_cm,ingredient,character1,function1,specification,dosage_form,usage1,sideaffect,contraindication,announcement,pregnant,child,elder,interaction,overdose,pharmacological_action,pharmacokinetics,storage,packaging,valid_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (general_name,brand_name,approval_number,standard_code,company,brand_factory,is_cm,ingredient,character,function,specification,dosage_form,usage,sideaffect,contraindication,announcement,pregnant,child,elder,interaction,overdose,pharmacological_action,pharmacokinetics,storage,packaging,valid_date)
            print(sqlstr)
            cue.execute(sqlstr)
            print('insert success')
            
        except Exception as e:
            print('Inset error occured:',e)
            con.rollback()
            
        else:
            con.commit()
            
        con.close()      
        return item


    
    
