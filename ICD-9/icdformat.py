# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:37:41 2019

@author: eileenlu
"""

import json
data=open(r'E:\icd\icd9.json','r',encoding='utf-8')
data_new=open(r'E:\icd\icd9_new.json','w',encoding='utf-8')
#liness='{"level1":"76-84  第十六章肌肉骨骼系统手术","level2":"77  其他骨的切开术、切除术和切断术","level3":"77.5  ","level4":"77.52  ","info":{"手术操作分类代码国家临床版1.1":" 77.5200 None","手术操作分类与代码全国2017版":" 77.5200 None","北京临床版ICD-9-CM-3V6.01":" 77.52001 (足母)囊切除伴软组织矫正和关节固定术  77.52002 (足母)外翻矫形术[McBride手术] ","手术操作分类代码国家临床版1.2":" 77.5200 None","广东省ICD-9-CM-3手术与操作代码（2017）":" 77.5201 踇囊肿切除术伴软组织矫正和关节固定术 ","广东省ICD-9-CM-3手术与操作代码(2016版)":" 77.5201 踇囊肿切除术伴软组织矫正和关节固定术 ","《山东省医疗机构手术操作分类代码及级别目录(2018年1.1版试行）》":" 77.5200 None","山东省-临床版国际疾病分类ICD-9-CM-3(V6.01版)":" 77.52001 (足母)囊切除伴软组织矫正和关节固定术  77.52002 (足母)外翻矫形术[McBrⅠde手术] ","北京临床版ICD9(v4.1)":" ","北京icd9v5.0":" 77.52001 拇(足母)囊切除伴软组织矫正和关节固定术  77.52002 拇(足母)外翻矫形术 ","北京版手术操作名称v6.0":" 77.52001 (足母)囊切除伴软组织矫正和关节固定术  77.52002 (足母)外翻矫形术[McBride手术] ","北京版RC022-ICD-9手术编码":" 77.52001 拇(足母)囊切除伴软组织矫正和关节固定术  77.52002 拇(足母)外翻矫形术 ","四川省ICD手术编码":" 77.5200 None","手术操作编码ICD-9-CM-3(2017维护版)":" 77.52001 (足母)囊切除伴软组织矫正和关节固定术  77.52002 (足母)外翻矫形术[McBride手术] ","手术操作分类代码国家临床版1.0":" 77.5200 None","《TCHIA001-2017手术、操作分类与代码》团体标准":" 77.5200 None"}}'
for liness in data.readlines():
    if liness.startswith(u'\ufeff'):
        liness = liness.encode('utf8')[3:].decode('utf8') 
    info_dict=json.loads(liness)
    info=info_dict['info']
    for key in info:
        value=info[key]
        value=value.strip()
        value_list=value.split()
        value_dict=dict()
#        if(len(value_list)%2==1):
#            value_list.append('None')
        for i in range(len(value_list)):
            if(i%2==0):
                value_dict[value_list[i]]=value_list[i+1]
        info[key]=value_dict
    lines1=json.dumps(info_dict,ensure_ascii=False)
    data_new.write(lines1)
    data_new.write('\n')
data_new.close()            


###check
import json
import re
data_new=open(r'E:\icd\icd9_new.json','r',encoding='utf-8')
#liness='{"level1": "87-99  第十八章其他诊断性和治疗性操作", "level2": "99  其他非手术性操作", "level3": "99.0  输血和血液成分", "level4": "99.00  围术期自体输全血或血成分", "info": {"手术操作分类代码国家临床版1.1": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}, "手术操作分类与代码全国2017版": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}, "北京临床版ICD-9-CM-3V6.01": {"99.00001": "自体血液回收", "99.00002": "自体血回输(术中)"}, "手术操作分类代码国家临床版1.2": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}, "广东省ICD-9-CM-3手术与操作代码（2017）": {}, "广东省ICD-9-CM-3手术与操作代码(2016版)": {}, "《山东省医疗机构手术操作分类代码及级别目录(2018年1.1版试行）》": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}, "山东省-临床版国际疾病分类ICD-9-CM-3(V6.01版)": {"99.00001": "自体血液回收", "99.00002": "自体血回输(术中)"}, "北京临床版ICD9(v4.1)": {}, "北京icd9v5.0": {"99.00001": "自体血液回收"}, "北京版手术操作名称v6.0": {"99.00001": "自体血液回收", "99.00002": "自体血回输(术中)"}, "北京版RC022-ICD-9手术编码": {"99.00001": "自体血液回收"}, "四川省ICD手术编码": {"99.0001": "自体血液回输", "99.0000": "围手术期自体输全血或血成分"}, "手术操作编码ICD-9-CM-3(2017维护版)": {"99.00001": "自体血液回收", "99.00002": "自体血回输(术中)"}, "手术操作分类代码国家临床版1.0": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}, "《TCHIA001-2017手术、操作分类与代码》团体标准": {"99.0000": "围手术期自体输全血或血成分", "99.0001": "自体血液回输"}}}'
rep=re.compile(r'[a-zA-Z0-9.]+')
i=1
for liness in data_new.readlines():
    info_dict=json.loads(liness)
    info=info_dict['info']
    if(not isinstance(info,dict)):
        print('maybe error line '+str(i))
    for key in info:
        value=info[key]
        for keykey in value:
            if (rep.findall(keykey)[0].strip()!=keykey.strip()):
                print('now is the line'+ str(i))
    i=i+1
        
    
    