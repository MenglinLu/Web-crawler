# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem


class DrugSpider(scrapy.Spider):
    name = 'drug'
    allowed_domains = ['www.yaopinnet.com']
    start_urls = ['http://www.yaopinnet.com/tools/sms.asp']
    
    def parse(self,response):
        base_url='http://www.yaopinnet.com'
        for letter_url in response.xpath("//div[@id='huayao_mulu_nav']/a[contains(@href,'zhongyao')]/@href").extract()[:1]:
            letter_url_all=base_url+letter_url
            yield scrapy.Request(letter_url_all,callback=self.parse1)
            
    def parse1(self, response):
        base_url='www.yaopinnet.com/zhongyao1/'
        now_url=response.url
        now_letter=list(now_url)[-6]
        num_page=len(response.xpath("//div[@id='sms_page']/a").extract())
        for i in range(num_page+1)[:2]:
            page_url='http://'+base_url+str(now_letter)+str(i+1)+'.htm'
            yield scrapy.Request(page_url,callback=self.parse2)
            
    def parse2(self,response):
        base_url='http://www.yaopinnet.com'
        for drug_url in response.xpath("//ul/li/a/@href").extract()[:5]:
            drug_url_all=base_url+drug_url
            yield scrapy.Request(drug_url_all,callback=self.parse3)
            
    def parse3(self,response):
        drug_item=MyspiderItem()
        ####
        general_name=str(response.xpath("//li[contains(text(),'【药品名称】')]/text()")[1].extract()).replace('通用名称：','').replace('[','').replace(']','').replace("'",'')
        drug_item['general_name']=general_name
        ####
        ingredient=response.xpath("//li[contains(text(),'【成份】')]/text()").extract()
        if (len(ingredient)==0):
            drug_item['ingredient']='NULL'
        else:
            drug_item['ingredient']=' '.join(ingredient).replace('【成份】','').replace('[','').replace(']','').replace("'",'')
        ####
        character=response.xpath("//li[contains(text(),'【性状】')]/text()").extract()
        if (len(character)==0):
            drug_item['character']='NULL'
        else:
            drug_item['character']=' '.join(character).replace('【性状】','').replace('[','').replace(']','').replace("'",'')
        ####
        function=response.xpath("//li[contains(text(),'【适应症】')]/text()").extract()
        if (len(function)==0):
            drug_item['function']='NULL'
        else:
            drug_item['function']=' '.join(function).replace('【适应症】','').replace('[','').replace(']','').replace("'",'')
        ####
        usage=response.xpath("//li[contains(text(),'【用法用量】')]/text()").extract()
        if (len(usage)>=1):
            drug_item['usage']=' '.join(usage).replace('【用法用量】','').replace('[','').replace(']','').replace("'",'').replace('【用法与用量】','')
        if (len(usage)==0):
            drug_item['usage']='NULL'
        ####
        sideaffect=response.xpath("//li[contains(text(),'【不良反应】')]/text()").extract()
        if (len(sideaffect)>=1):
            drug_item['sideaffect']=' '.join(sideaffect).replace('【不良反应】','').replace('[','').replace(']','').replace("'",'')
        if (len(sideaffect)==0):
            drug_item['sideaffect']='NULL'
        ####
        contraindication=response.xpath("//li[contains(text(),'【禁忌】')]/text()").extract()
        if (len(contraindication)>=1):
            drug_item['contraindication']=' '.join(contraindication).replace('【禁忌】','').replace('[','').replace(']','').replace("'",'')
        if (len(contraindication)==0):
            drug_item['contraindication']='NULL'
        ####
        announcement=response.xpath("//li[contains(text(),'【注意事项】')]/text()").extract()
        if (len(announcement)==0):
            drug_item['announcement']='NULL'
        else:
            drug_item['announcement']=' '.join(announcement).replace('【注意事项】','').replace('[','').replace(']','').replace("'",'')
        ####
        pregnant=response.xpath("//li[contains(text(),'【孕妇及哺乳期妇女用药】')]/text()").extract()
        if (len(pregnant)>=1):
            drug_item['pregnant']=' '.join(pregnant).replace('【孕妇及哺乳期妇女用药】','').replace('[','').replace(']','').replace("'",'')
        if (len(pregnant)==0):
            drug_item['pregnant']='NULL'
        ####
        child=response.xpath("//li[contains(text(),'【儿童用药】')]/text()").extract()
        if (len(child)>=1):
            drug_item['child']=' '.join(child).replace('【儿童用药】','').replace('[','').replace(']','').replace("'",'')
        if (len(child)==0):
            drug_item['child']='NULL'
        ####
        elder=response.xpath("//li[contains(text(),'【老年用药】')]/text()").extract()
        if (len(elder)>=1):
            drug_item['elder']=' '.join(elder).replace('【老年用药】','').replace('[','').replace(']','').replace("'",'')
        if (len(elder)==0):
            drug_item['elder']='NULL'
        ####
        interaction=response.xpath("//li[contains(text(),'【药物相互作用】')]/text()").extract()
        if (len(interaction)>=1):
            drug_item['interaction']=' '.join(interaction).replace('【药物相互作用】','').replace('[','').replace(']','').replace("'",'')
        if (len(interaction)==0):
            drug_item['interaction']='NULL'
        ####
        overdose=response.xpath("//li[contains(text(),'【药物过量】')]/text()").extract()
        if (len(overdose)>=1):
            drug_item['overdose']=' '.join(overdose).replace('【药物过量】','').replace('[','').replace(']','').replace("'",'')
        if (len(overdose)==0):
            drug_item['overdose']='NULL'
        ####
        pharmacokinetics=response.xpath("//li[contains(text(),'【药理毒理】')]/text()").extract()
        if (len(pharmacokinetics)>=1):
            drug_item['pharmacokinetics']=' '.join(pharmacokinetics).replace('【药理毒理】','').replace('[','').replace(']','').replace("'",'')
        if (len(pharmacokinetics)==0):
            drug_item['pharmacokinetics']='NULL'
        ####
        pharmacological_action=response.xpath("//li[contains(text(),'【药代动力学】')]/text()").extract()
        if (len(pharmacological_action)>=1):
            drug_item['pharmacological_action']=' '.join(pharmacological_action).replace('【药代动力学】','').replace('[','').replace(']','').replace("'",'')
        if (len(pharmacological_action)==0):
            drug_item['pharmacological_action']='NULL'
        ####
        storage=response.xpath("//li[contains(text(),'【贮藏】')]/text()").extract()
        if (len(storage)>=1):
            drug_item['storage']=' '.join(storage).replace('【贮藏】','').replace('[','').replace(']','').replace("'",'')
        if (len(storage)==0):
            drug_item['storage']='NULL'
        ####
        packaging=response.xpath("//li[contains(text(),'【包装】')]/text()").extract()
        if (len(packaging)>=1):
            drug_item['packaging']=' '.join(packaging).replace('【包装】','').replace('[','').replace(']','').replace("'",'')
        if (len(packaging)==0):
            drug_item['packaging']='NULL'
        ####
        valid_date=response.xpath("//li[contains(text(),'【有效期】')]/text()").extract()
        if (len(valid_date)>=1):
            drug_item['valid_date']=' '.join(valid_date).replace('【有效期】','').replace('[','').replace(']','').replace("'",'')
        if (len(valid_date)==0):
            drug_item['valid_date']='NULL'
            
        drug_item['is_cm']='1'
        ####
#        execute_standard=response.xpath("//li[contains(text(),'执行标准')]/text()").extract()
#        if (len(execute_standard)>=1):
#            drug_item['execute_standard']=str(execute_standard).replace('【执行标准】','')
#        if (len(execute_standard)==0):
#            drug_item['execute_standard']='NULL'
        
        print('----------------------------------------------')
        print('药品名:'+str(drug_item['general_name']))
        
        if len(response.xpath("//div[@id='changjia_content']/div").extract())==0:
            drug_item['brand_name']='NULL-None records'
            drug_item['company']='NULL-None records'
            drug_item['specification']='NULL-None records'
            drug_item['dosage_form']='NULL-None records'
            drug_item['approval_number']='NULL-None records'
            drug_item['standard_code']='NULL-None records'
            drug_item['brand_factory']='NULL-None records'
            yield drug_item
            
        if len(response.xpath("//strong[contains(text(),'查看更多')]").extract())==0:
            base_url='http://www.yaopinnet.com'
            for everydrug in response.xpath("//div[@id='changjia_content']/div/a[@class='wenhao']/@href").extract():
                everydrugurl=base_url+everydrug
                yield scrapy.Request(everydrugurl,callback=self.parse_4_1,meta={'item':drug_item}) 
            
        else:
            base_url='http://www.yaopinnet.com/zhongyao/'
            more_url=response.xpath("//strong[contains(text(),'查看更多')]/following::a/@href").extract()[0]
            more_url_all=base_url+more_url
            yield scrapy.Request(more_url_all,callback=self.parse_4_2,meta={'item':drug_item})
        
    def parse_4_1(self,response):
        drug_item = response.meta['item']
        drug_item['brand_name']=response.xpath("//span[contains(./text(), '商 品 名')]/following::text()[1]").extract()[0]
        drug_item['approval_number']=response.xpath("//span[contains(./text(), '批准文号')]/following::text()[1]").extract()[0]
        drug_item['company']=response.xpath("//span[contains(./text(), '生产单位')]/following::text()[1]").extract()[0]
        drug_item['brand_factory']=response.xpath("//span[contains(./text(), '生产地址')]/following::text()[1]").extract()[0]
        drug_item['dosage_form']=response.xpath("//span[contains(./text(), '剂　　型')]/following::text()[1]").extract()[0]
        drug_item['specification']=response.xpath("//span[contains(./text(), '规　　格')]/following::text()[1]").extract()[0]
        drug_item['standard_code']=response.xpath("//span[contains(./text(), '药品本位码')]/following::text()[1]").extract()[0]
        yield drug_item
    
    def parse_4_2(self,response):
        drug_item=response.meta['item']
        base_url='http://www.yaopinnet.com'
        for everydrug in response.xpath("//a[@class='wenhao']/@href").extract():
            everydrugurl=base_url+everydrug
            yield scrapy.Request(everydrugurl,callback=self.parse_4_2_1,meta={'item':drug_item})
        
    def parse_4_2_1(self,response):
        drug_item=response.meta['item']
        drug_item['brand_name']=response.xpath("//span[contains(./text(), '商 品 名')]/following::text()[1]").extract()[0]
        drug_item['approval_number']=response.xpath("//span[contains(./text(), '批准文号')]/following::text()[1]").extract()[0]
        drug_item['company']=response.xpath("//span[contains(./text(), '生产单位')]/following::text()[1]").extract()[0]
        drug_item['brand_factory']=response.xpath("//span[contains(./text(), '生产地址')]/following::text()[1]").extract()[0]
        drug_item['dosage_form']=response.xpath("//span[contains(./text(), '剂　　型')]/following::text()[1]").extract()[0]
        drug_item['specification']=response.xpath("//span[contains(./text(), '规　　格')]/following::text()[1]").extract()[0]
        drug_item['standard_code']=response.xpath("//span[contains(./text(), '药品本位码')]/following::text()[1]").extract()[0]
        yield drug_item
    
        
            
        
