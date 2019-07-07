# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    general_name=scrapy.Field() 
    ingredient=scrapy.Field()
    character=scrapy.Field()
    function=scrapy.Field()
    usage=scrapy.Field()
    sideaffect=scrapy.Field()
    contraindication=scrapy.Field()
    announcement=scrapy.Field()
    pregnant=scrapy.Field()
    child=scrapy.Field()
    elder=scrapy.Field()
    interaction=scrapy.Field()
    overdose=scrapy.Field()
    pharmacokinetics=scrapy.Field()
    pharmacological_action=scrapy.Field()
    storage=scrapy.Field()
    packaging=scrapy.Field()
    valid_date=scrapy.Field()
    
    brand_name=scrapy.Field()
    company=scrapy.Field()
    specification=scrapy.Field()
    dosage_form=scrapy.Field()
    approval_number=scrapy.Field()
    standard_code=scrapy.Field()
    brand_factory=scrapy.Field()
    is_cm=scrapy.Field()

