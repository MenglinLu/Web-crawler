# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:32:53 2019

@author: eileenlu
"""

import pymysql
import json

host='10.93.149.53'
user='kg_intern'
psd='kg_intern'
db='kg_intern'
port=3306
        
con=pymysql.connect(host=host,user=user,passwd=psd,db=db,port=port)

print('mysql connet success')
i=0;
f=open(r'E:\drugs_json_zhongyao1.json','r',encoding='utf-8')
all_rows_num=len(f.readlines())
for lines in f.readlines():
    print(lines)
    if(lines.strip()!=""):
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,port=port)
        drug_dict=json.loads(lines)
        general_name="'"+drug_dict['general_name'].strip().strip(',')+"'"
        brand_name="'"+drug_dict['brand_name'].strip().strip(',')+"'"
        approval_number="'"+drug_dict['approval_number'].strip().strip(',')+"'"
        standard_code="'"+drug_dict['standard_code'].strip().strip(',')+"'"
        company="'"+drug_dict['company'].strip().strip(',')+"'"
        brand_factory="'"+drug_dict['brand_factory'].strip().strip(',')+"'"
        is_cm="'"+drug_dict['is_cm'].strip().strip(',')+"'"
        ingredient="'"+drug_dict['ingredient'].strip().strip(',')+"'"
        character="'"+drug_dict['character'].strip().strip(',')+"'"
        function="'"+drug_dict['function'].strip().strip(',')+"'"
        specification="'"+drug_dict['specification'].strip().strip(',')+"'"
        dosage_form="'"+drug_dict['dosage_form'].strip().strip(',')+"'"
        usage="'"+drug_dict['usage'].strip().strip(',')+"'"
        sideaffect="'"+drug_dict['sideaffect'].strip().strip(',')+"'"
        contraindication="'"+drug_dict['contraindication'].strip().strip(',')+"'"
        announcement="'"+drug_dict['announcement'].strip().strip(',')+"'"
        pregnant="'"+drug_dict['pregnant'].strip().strip(',')+"'"
        child="'"+drug_dict['child'].strip().strip(',')+"'"
        elder="'"+drug_dict['elder'].strip().strip(',')+"'"
        interaction="'"+drug_dict['interaction'].strip().strip(',')+"'"
        overdose="'"+drug_dict['overdose'].strip().strip(',')+"'"
        pharmacological_action="'"+drug_dict['pharmacological_action'].strip().strip(',')+"'"
        pharmacokinetics="'"+drug_dict['pharmacokinetics'].strip().strip(',')+"'"
        storage="'"+drug_dict['storage'].strip().strip(',')+"'"
        packaging="'"+drug_dict['packaging'].strip().strip(',')+"'"
        valid_date="'"+drug_dict['valid_date'].strip().strip(',')+"'"
        cue=con.cursor()
        sqlstr="insert into kg_intern.medicine_new (general_name,brand_name,isbn,standard_code,company,production_address,is_cm,ingredient,character1,function1,specification,dosage_form,usage1,sideaffect,contraindication,announcement,pregnant,child,elder,interaction,overdose,pharmacological_action,pharmacokinetics,storage,packaging,valid_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (general_name,brand_name,approval_number,standard_code,company,brand_factory,is_cm,ingredient,character,function,specification,dosage_form,usage,sideaffect,contraindication,announcement,pregnant,child,elder,interaction,overdose,pharmacological_action,pharmacokinetics,storage,packaging,valid_date)
        print(sqlstr)
        #print(sqlstr)
        cue.execute(sqlstr)
        con.commit()
        i=i+1;
        if (i%1==0):
            print('insert success '+str(i)+' records')
            print('now percent '+str(i*1.0/all_rows_num))
            print('insert success: '+general_name)

            
con.close()  
    
        
    