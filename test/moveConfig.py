#!/usr/bin/env python
# -*- coding: UTF-8 -*-

###############################
#   这里是电影采集配置
#
#
#
###############################

from test import *

# http://www.6vhao.tv/mj/
# 6v电影网
from common.RuleConf import *


def run6vhao():
    start_url = "http://www.6vhao.tv/mj/"
    conf = {
        "group": '*//div[@class="menutv"]//a',
        "tablename": '6v电影网_dict',
        "columns": [
            {"名称": "主键", "规则": "md5", "类型": "主键", "连接": "地址"},
            {"名称": "网站", "规则": "6v电影网", "类型": "不解析"},
            {"名称": "类别", "规则": ".//text()", "类型": "文本"},
            {"名称": "地址", "规则": "./@href", "类型": "连接"},
            {"名称": "采集时间", "规则": "%Y.%m.%d %H:%M:%S", "类型": "采集时间"},
        ],
    }
    pageDict = PageDict()
    pageDict.run(url=start_url, conf=conf)


def runList6vhao():
    confs = [{
        "urltable": "6v电影网_dict",
        "urlname": '地址',
        "tablename": "6v电影网_list",
        "group": '*//div[@class="listBox"]/ul/li',
        # "chartset":"gb2312",
        "columns": [
            {"名称": "主键", "规则": "md5", "类型": "主键", "连接": "地址"},
            {"名称": "网站", "规则": "6v电影网", "类型": "不解析"},
            {"名称": "资料名称", "规则": './div[@class="listInfo"]/h3/a/text()', "类型": "文本"},
            {"名称": "地址", "规则": './div[@class="listInfo"]/h3/a/@href', "类型": "连接"},
            {"名称": "图片", "规则": './div[@class="listimg"]/a/img/@src', "类型": "图片"},
            {"名称": "分类", "规则": './div[@class="listInfo"]/p[2]//text()', "类型": "文本"},
            {"名称": "时间", "规则": './div[@class="listInfo"]/p[3]//text()', "类型": "文本"},
            {"名称": "采集时间", "规则": "%Y.%m.%d %H:%M:%S", "类型": "采集时间"},
        ],
        "nextPage": '*//div[@class="pagebox"]/a[contains(text(),"下一页")]/@href'
    }]
    pageList = PageList()
    pageList.runMulity(confs)


def runList6vhao():
    conf = {
        "urltable": "6v电影网_dict",
        "urlname": '地址',
        "tablename": "6v电影网_list",
        "group": '*//div[@class="listBox"]/ul/li',
        # "chartset":"gb2312",
        "columns": [
            {"名称": "主键", "规则": "md5", "类型": "主键", "连接": "地址"},
            {"名称": "网站", "规则": "6v电影网", "类型": "不解析"},
            {"名称": "资料名称", "规则": './div[@class="listInfo"]/h3/a/text()', "类型": "文本"},
            {"名称": "地址", "规则": './div[@class="listInfo"]/h3/a/@href', "类型": "连接"},
            {"名称": "图片", "规则": './div[@class="listimg"]/a/img/@src', "类型": "图片"},
            {"名称": "分类", "规则": './div[@class="listInfo"]/p[2]//text()', "类型": "文本"},
            {"名称": "时间", "规则": './div[@class="listInfo"]/p[3]//text()', "类型": "文本"},
            {"名称": "采集时间", "规则": "%Y.%m.%d %H:%M:%S", "类型": "采集时间"},
        ],
        "nextPage": '*//div[@class="pagebox"]/a[contains(text(),"下一页")]/@href'
    }
    pageList = PageList()
    pageList.run(conf)
    # pageList.runMulity(confs)

def ailian():
    confs = {
        "urltable": "爱恋动漫BT下载_dict",
        "urlname": '地址',
        "tablename": "爱恋动漫BT下载_list",
        "group": '*//table[@id="listTable"]/tbody/tr',
        "columns": [
            {"名称": "主键", "规则": "md5", "类型": "主键", "连接": "地址"},
            {"名称": "网站", "规则": "爱恋动漫BT下载", "类型": "不解析"},
            {"名称": "资料名称", "规则": './td[3]/a[1]/text()', "类型": "文本"},
            {"名称": "地址", "规则": './td[3]/a[1]/@href', "类型": "连接"},
            {"名称": "发表时间", "规则": './td[1]/text()', "类型": "文本"},
            {"名称": "类别", "规则": './td[2]//text()', "类型": "文本"},
            {"名称": "大小", "规则": './td[4]//text()', "类型": "文本"},
            {"名称": "种子", "规则": './td[5]//text()', "类型": "文本"},
            {"名称": "下载", "规则": './td[6]//text()', "类型": "文本"},
            {"名称": "完成", "规则": './td[7]//text()', "类型": "文本"},
            {"名称": "UP主_代号", "规则": './td[8]//text()', "类型": "文本"},
            {"名称": "采集时间", "规则": "%Y.%m.%d %H:%M:%S", "类型": "采集时间"},
        ],
        "nextPage": '*//div[@class="pages clear"]//a[contains(text(),"〉")]/@href'
    }
    pageDict = PageList()
    pageDict.runProcess(confs)



if __name__ == '__main__':
    # run6vhao()
    #runList6vhao()
    # test()
    ailian()
