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


def test():
    conf = {
        "urltable": "xuexi111_list",  # 地址来源表
        "urlname": '地址',  # 来源表的字段
        "tablename": "xuexi111_detail",  # 结果数据存入数据表
        "group": '*/div[@class="content"]',  # 数据在网页中展示的范围 xpath
        "readtype": 'rg',
        # 网页请求数据方式方法，默认是 rg，可选 rg （request get），rp （request post），se （Selenium  开发中），ul （urlllib） 后开发多种方式执行自动选择
        # "chartset":"gb2312", # 默认是 utf8
        "columns": [  # 数据表配置项，对应结果表的字段
            {"类型": "主键",  # 系统默认类型包括 主键，不解析，本地连接，采集时间，文本，连接，图片，数组，context，list
             "名称": "主键",  # 当类型为主键时，规则 可选uuid （随机生成），md5（必须有 连接 属性） 两种
             "规则": "md5",  # 规则一般使用 xpath 规则，极个别系统配置不采用xpath 比如主键，本地连接，采集时间，不解析（规则原文本返回），
             "连接": "地址"  # 除 类型，名称，规则 三个必须的属性外，其他会有额外的一些属性辅助，
                             # 例如  主键的md5必须有链接属性（属性值对应其他字段的名称），congtext 和 list代表包含更复杂的columns
             },
            {"类型": "不解析", "名称": "网站", "规则": "学习资料库"},
            {"类型": "本地连接", "名称": "地址", "规则": "", },
            {"类型": "采集时间", "名称": "采集时间", "规则": "%Y.%m.%d %H:%M:%S", },
            {"类型": "文本", "名称": "标题", "规则": "./h1/text()"},
            {"类型": "图片", "名称": "图片", "规则": './/div[@class="cont_l"]/div[@class="cont_lt"]/img/@src'},
            {"类型": "文本", "名称": "资料共享",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[1]/span//text()'},
            {"类型": "连接", "名称": "资料共享链接",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[1]/span/a/@href'},
            {"类型": "文本", "名称": "文件大小",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[2]/span//text()'},
            {"类型": "文本", "名称": "语言要求",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[3]/span//text()'},
            {"类型": "文本", "名称": "资料类型",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[4]/span//text()'},
            {"类型": "文本", "名称": "运行环境",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[5]/span//text()'},
            {"类型": "文本", "名称": "浏览次数",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[6]/span//text()'},
            {"类型": "文本", "名称": "更新时间",
             "规则": './/div[@class="txt_info"]//div[@class="cont_l"]/div[@class="cont_lt"]/div[@class="cont_ltr"]/ul/li[7]/span//text()'},
            {
                "名称": '资料介绍',
                "类型": 'context',
                "规则": './/div[@class="download"]/div[@class="download-left"]',
                "columns": [
                    {"名称": "资料介绍", "规则": './/div[@class="info-content"]', "类型": "源代码"},
                ]
            }, {
                "名称": '下载文件',
                "类型": 'list',
                "规则": './/div[@id="download"]/table//tr',
                "columns": [
                    {"名称": "文件名", "规则": './td[1]/a/text()', "类型": "文本"},
                    {"名称": "下载地址", "规则": './td[1]/a/@href', "类型": "连接"},
                    {"名称": "离线地址", "规则": './td[1]/div[@class="lixian-jpg"]/a/@href', "类型": "连接"},
                    {"名称": "文件大小", "规则": './td[@align="center"]/text()', "类型": "文本"},
                ]
            }
        ],
        "nextPage": '' # PageList 使用翻页配置 值用xpath配置 例如 '*//div[@class='pegebar']/a[@class='next']/@href'
    }
    pageDetail = PageDetail() # 使用 from  common.RuleConf import * 导入，根据判读要采集页面的类型使用那个 PageDict（采集网站地图和列表数据使用）PageList（采集列表数据使用） PageDetail（采集详细信息页面）
    pageDetail.run(conf)      # 使用run方法即可执行采集任务，

    #pageList = PageList()
    #pageList.run(conf)

    #pageDict = PageDict()
    #pageDict.run(url=start_url, conf=conf)

if __name__ == '__main__':
    # run6vhao()
    runList6vhao()
    # test()
