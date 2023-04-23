# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class InterproPipeline:
    def __init__(self):
        store_file ='./sunburst.csv'
        self.file = open(store_file, 'a+', encoding="utf-8", newline='')
        self.writer = csv.writer(self.file, dialect="excel")


    def process_item(self, items, spider):
        line = [items['key'], items['sunburst']]
        self.writer.writerow(line)
        
        return items      
    

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()