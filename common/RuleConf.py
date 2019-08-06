#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from lxml import etree, html
from common.HtmlSource import HtmlSource
from urllib import parse

import json
import hashlib
import uuid
import time
import types
import pymysql
from common.Mysql_Utils import MyPymysqlPool


# 网页解析
class Rule:

    # 采集列表页面
    def crawler_list(self, url, conf, type_p='rp', chartset='utf8'):

        htmlSource = HtmlSource()
        # 获取网页原文
        html_context = htmlSource.get_html(url_p=url, type_p=type_p, chartset_p=chartset)
        index = 0
        while len(html_context) < 128 and index < 2:
            html_context = htmlSource.get_html(url_p=url)
            index += 1
        if len(html_context) < 128:
            raise Exception(1001, '网页访问失败，无内容！')
        # 解析原文
        tree = html.fromstring(html_context)
        result_list = tree.xpath(conf['group'])
        result_list_context = self._analysis_list(list=result_list, columns=conf['columns'], url=url)
        if 'nextPage' in conf.keys():
            next_page = tree.xpath(conf['nextPage'])
            if len(next_page) > 0:
                return result_list_context, parse.urljoin(url, next_page[0])
            else:
                return result_list_context, None
        else:
            return result_list_context, None

    # 解析列表页面
    def _analysis_list(self, list, columns, url=""):
        list_context = []
        for tree in list:
            list_context.append(self._analysis_context(tree=tree, columns=columns, url=url))
        return list_context

    def crawler_detail(self, conf, url='', type_p='rp', chartset='utf8'):
        htmlSource = HtmlSource()
        # 获取网页原文
        html_context = htmlSource.get_html(url_p=url, type_p=type_p, chartset_p=chartset)
        index = 0
        while len(html_context) < 128 and index < 2:
            html_context = htmlSource.get_html(url_p=url)
            index += 1
        if len(html_context) < 128:
            raise Exception(1001, '网页访问失败，无内容！')
        # 解析原文
        tree = html.fromstring(html_context)
        result_list = tree.xpath(conf['group'])
        result_list_context = self._analysis_context(tree=result_list[0], columns=conf['columns'], url=url)
        return result_list_context

    # 解析页面
    def _analysis_context(self, tree, columns, url=""):
        columns_context = {}
        id_flag = False
        for column in columns:
            if '主键' == column["类型"]:
                column_id = column
                id_flag = True
            else:
                # 除主键其他数据解析
                columns_context[column["名称"]] = self._analysis_(tree=tree, column=column, url=url)
        # 主键解析
        if id_flag:
            if 'md5' == column_id["规则"]:
                column_id["url"] = columns_context[column_id["连接"]]
            columns_context[column_id["名称"]] = self._analysis_(tree=tree, column=column_id, url=url)
        return columns_context

    # 解析页面
    def _analysis_(self, tree, column, url=""):
        column_context = ''
        try:
            if column["类型"] == '主键':
                # 不同的主键策略 默认使用uuid
                if ('uuid' == column["规则"]):
                    column_context = str(uuid.uuid4()).replace("-", '')
                elif ('md5' == column["规则"]):
                    myMd5 = hashlib.md5()
                    myMd5.update(column["url"].encode("utf8"))
                    myMd5_Digest = myMd5.hexdigest()
                    column_context = myMd5_Digest
                else:
                    column_context = uuid.uuid4()
            if column["类型"] == '不解析':
                # 返回填写的规则原文
                column_context = column["规则"]
            if column["类型"] == '文本':
                # 进行lxml方式解析
                text = ''
                for a in tree.xpath(column["规则"]):
                    text = text + str(a).strip()
                column_context = text
            if column["类型"] == '连接':
                # 进行lxml方式解析
                imgurl = tree.xpath(column["规则"])
                if len(imgurl) > 1:
                    imgs = []
                    for img in imgurl:
                        imgs.append(parse.urljoin(url, img))
                    column_context = imgs
                elif (len(imgurl) == 1):
                    column_context = parse.urljoin(url, imgurl[0])
                else:
                    column_context = ''
            if column["类型"] == '图片':
                # 进行lxml方式解析
                imgurl = tree.xpath(column["规则"])
                if len(imgurl) > 1:
                    imgs = []
                    for img in imgurl:
                        imgs.append(parse.urljoin(url, img))
                    column_context = imgs
                elif (len(imgurl) == 1):
                    column_context = parse.urljoin(url, imgurl[0])
                else:
                    column_context = ''
            if column["类型"] == '采集时间':
                # 系统当前时间
                rg = '%Y.%m.%d %H:%M:%S'
                if column["规则"] != '':
                    rg = column["规则"]
                column_context = time.strftime(rg, time.localtime(time.time()))
            if column["类型"] == '源代码':
                # 进行lxml方式解析
                html_context = tree.xpath(column["规则"])
                html_str = ''
                for content in html_context:
                    strs = etree.tostring(content, encoding="utf-8", pretty_print=True, method="html").decode(
                        "utf-8")  # 转为字符串
                    html_str = html_str + strs
                column_context = html_str
            if column["类型"] == '本地连接':
                # 进行lxml方式解析
                column_context = url
            if column["类型"] == '数组':
                # 进行lxml方式解析
                column_context = tree.xpath(column["规则"])
            if column["类型"] == 'list':
                # 进行lxml方式解析
                tree = tree.xpath(column["规则"])
                column_context = self._analysis_list(list=tree, columns=column['columns'], url=url)
            if column["类型"] == 'context':
                # 进行lxml方式解析
                tree = tree.xpath(column["规则"])[0]
                column_context = self._analysis_context(tree=tree, columns=column['columns'], url=url)

        except Exception as e:
            e.args

        return column_context


# 数据入库
class DatabaseInsertList:

    # 插入数据库
    def insertList(self, result='', table='', column_names=[], db_pool=None):
        columns = ''
        index = 0
        for column_name in column_names:
            if index > 0:
                columns += ","
            columns += '`' + column_name + '`'
            index += 1

        for row in result:
            index = 0
            values = ''
            for column_name in column_names:
                if index > 0:
                    values += ","
                values += "'" + str(row[column_name]).replace("\'", "\\\'").replace("\\", "\\\\") + "'"
                index += 1

            sql = "insert into `" + table + "` (" + columns + ") values(" + values + ")"
            print(sql)
            try:
                db_pool.insert(sql=sql)
                db_pool._conn.commit();
            except pymysql.err.ProgrammingError as pye:
                if 1146 == pye.args[0]:
                    createsql = """create table """ + table + """ (`采集时间` varchar(20),`主键` varchar(32) primary key)"""
                    print(createsql)
                    db_pool.update(createsql)
                    for column_name in column_names:
                        altersql = " alter table " + table + " add column `" + column_name + "` varchar(255);"
                        try:
                            db_pool.update(altersql)
                        except Exception as e:
                            if e.args[0] == 1060:
                                print(table, column_name, "字段已经存在！")
                            else:
                                print(e.args, "更新表字段")
                    db_pool.insert(sql)
                    db_pool._conn.commit();
                else:
                    pye.with_traceback()
            except pymysql.err.IntegrityError as pye:
                if 1062 == pye.args[0]:
                    updatesql = "update " + table + " set "
                    index = 0
                    for column_name in column_names:
                        if index > 0:
                            updatesql += ","
                        updatesql += "`" + column_name + "` = '" + str(row[column_name]).replace("\'", "\\\'").replace(
                            "\\", "\\\\") + "'"
                        index += 1
                    updatesql += " where `主键` = '" + row['主键'] + "'"
                    print(updatesql)
                    db_pool.update(updatesql)
                    db_pool._conn.commit();
                    print("主键重复", pye.args[1])
                else:
                    pye.with_traceback()
            except Exception as e:
                e.with_traceback()

    def readAll(self, db_pool, table=''):
        sql = """ select * from %s where statue  is null or statue =0  """ % table
        try:
            result = db_pool.getAll(sql)
        except pymysql.err.InternalError:
            altersql = " alter table `" + table + "` add column `statue` int(2)"
            db_pool.update(altersql)
            return self.readAll(db_pool=db_pool, table=table)

        return result

    def updateAllStatue(self, db_pool, table='', statue=2):
        sql = """ update %s set statue = null where statue = %d """ % (table, statue)
        db_pool.update(sql)
        db_pool._conn.commit();

    def updateStatue2(self, db_pool, table='', uuid='', statue=2):
        sql = """ update %s set statue = %d where 主键='%s' """ % (table, statue, uuid)
        db_pool.update(sql)
        db_pool._conn.commit();

    # 插入数据库
    def insertDetail(self, result='', table='', column_names=[], db_pool=None):
        columns = ''
        values = ''
        index = 0
        for column_name in column_names:
            if index > 0:
                columns += ","

                values += ","
            if isinstance(result[column_name],dict):
                values += "'" + str(json.dumps(result[column_name],ensure_ascii=False)).replace("\\", "\\\\").replace("\'", "\\\'")+ "'"
            if isinstance(result[column_name],list):
                values += "'" + str(json.dumps(result[column_name],ensure_ascii=False)).replace("\\", "\\\\").replace("\'", "\\\'") + "'"
            else:
                values += "'" + str(result[column_name]).replace("\\", "\\\\").replace("\'", "\\\'") + "'"
            columns += '`' + column_name + '`'
            index += 1

        sql = "insert into `" + table + "` (" + columns + ") values(" + values + ")"
        print(sql)
        try:
            db_pool.insert(sql=sql)
            db_pool._conn.commit();
        except pymysql.err.ProgrammingError as pye:
            if 1146 == pye.args[0]:
                createsql = """create table """ + table + """ (`采集时间` varchar(20),`主键` varchar(32) primary key)"""
                print(createsql)
                db_pool.update(createsql)
                for column_name in column_names:
                    altersql = " alter table " + table + " add column `" + column_name + "` varchar(255);"
                    try:
                        db_pool.update(altersql)
                    except Exception as e:
                        if e.args[0] == 1060:
                            print(table, column_name, "字段已经存在！")
                        else:
                            print(e.args, "更新表字段")
                db_pool.insert(sql)
                db_pool._conn.commit();
            else:
                pye.with_traceback()
        except pymysql.err.IntegrityError as pye:
            if 1062 == pye.args[0]:
                updatesql = "update " + table + " set "
                index = 0
                for column_name in column_names:
                    if index > 0:
                        updatesql += ","
                    updatesql += "`" + column_name + "` = '" + str(result[column_name]).replace("\'", "\\\'").replace(
                        "\\", "\\\\") + "'"
                    index += 1
                updatesql += " where `主键` = '" + result['主键'] + "'"
                print(updatesql)
                db_pool.update(updatesql)
                db_pool._conn.commit();
                print("主键重复", pye.args[1])
            else:
                pye.with_traceback()
        except pymysql.err.DataError as pye:
            if pye.args[0] == 1406:
                column = pye.args[1]
                column = column[column.index("'") + 1:column.rindex("'")]
                altersql = "alter table " + table + " modify column " + column + " varchar(2000)"
                db_pool.update(sql=altersql)
                self.insertDetail(result, table, column_names)
        except Exception as e:
            e.with_traceback()


# 字典或者单列表页面从配置startUrl启动任务的
class PageDict:
    # 创建全局数据连接
    db_pool = MyPymysqlPool("default")
    databaseInsertList = DatabaseInsertList()

    # 采集字典
    def run(self, url, conf):
        rule = Rule()
        type_p = 'rg'
        if 'readtype' in conf.keys():
            type_p = conf['readtype']
        chartset = "utf8"
        if 'chartset' in conf.keys():
            chartset = conf['chartset']
        result, nextPage = rule.crawler_list(url, conf, type_p, chartset)
        print(nextPage)
        dic_list = []
        for row in conf['columns']:
            dic_list.append(row['名称'])

        self.databaseInsertList.insertList(result=result, table=conf['tablename'], column_names=dic_list,
                                           db_pool=self.db_pool)
        if nextPage is not None and url != nextPage:
            self.run(url=nextPage, conf=conf)


# 多列表页面从数据中取任务的
class PageList:
    db_pool = MyPymysqlPool("default")
    databaseInsertList = DatabaseInsertList()

    def run(self, confs):
        dictable = confs[0]['urltable']
        print(dictable)
        try:
            self.databaseInsertList.updateAllStatue(db_pool=self.db_pool, table=dictable, statue=2)
            dictList = self.databaseInsertList.readAll(db_pool=self.db_pool, table=dictable)
            if dictList is not False:
                # 数据写入
                for dict in dictList:
                    self.databaseInsertList.updateStatue2(db_pool=self.db_pool, table=dictable, uuid=dict['主键'],
                                                          statue=2)
                    for conf in confs:
                        url = dict[conf['urlname']]
                        if dict['current_url'] is not None:
                            url = dict['current_url']
                        type_p = 'rg'
                        if 'readtype' in conf.keys():
                            type_p = conf['readtype']
                        chartset = "utf8"
                        if 'chartset' in conf.keys():
                            chartset = conf['chartset']
                        self.crawlerNext(conf, url=url, uuid=dict['主键'], type_p=type_p, chartset=chartset)
        except Exception as e:
            print(e.args, "runList")
            if (e.args[0] == 1054):
                try:
                    altersql = " alter table `" + dictable + "` add column `statue` int(2)"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(dictable, " statue 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
                try:
                    altersql = " alter table `" + dictable + "` add column `更新时间` timestamp on update current_timestamp"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(dictable, "更新时间 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
                try:
                    altersql = " alter table `" + dictable + "` add column `current_url` varchar(500)"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(dictable, "current_url 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
            if (e.args[0] == "更新时间"):
                try:
                    altersql = " alter table `" + dictable + "` add column `更新时间` timestamp on update current_timestamp"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(dictable, "更新时间 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
            if ('current_url' == e.args[0]):
                try:
                    altersql = " alter table `" + dictable + "` add column `current_url` varchar(500)"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(dictable, "current_url 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
            self.run(confs)

    def crawlerNext(self, conf, url='', uuid='', type_p='rg', chartset='utf8'):
        print(url, uuid, type_p, chartset)
        try:
            rule = Rule()
            result, next_page = rule.crawler_list(url, conf, type_p, chartset)
            print(next_page)
            if len(result) > 0:
                list_list = []
                for row in conf['columns']:
                    list_list.append(row['名称'])
                self.databaseInsertList.insertList(result=result, table=conf['tablename'], column_names=list_list,
                                                   db_pool=self.db_pool)
                if next_page is not None and url != next_page:
                    self.updateCurrent(db_pool=self.db_pool, table=conf['urltable'], uuid=uuid, current=next_page)
                    self.db_pool._conn.commit();
                    self.crawlerNext(conf, url=next_page, uuid=uuid, type_p=type_p, chartset=chartset)
                else:
                    self.updateStatue(db_pool=self.db_pool, table=conf['urltable'], uuid=uuid, statue=1)
                    self.db_pool._conn.commit();
        except Exception as e:
            print(e.args)
            if 1001 == e.args[0]:
                self.databaseInsertList.updateStatue2(db_pool=self.db_pool, table=conf['urltable'], uuid=uuid,
                                                      statue=-1)
                self.db_pool._conn.commit();

            if e.args[0] == 1054:
                try:
                    altersql = " alter table `" + conf[
                        'urltable'] + "` add column `更新时间` timestamp on update current_timestamp"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(conf['urltable'], "更新时间 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
                try:
                    altersql = " alter table `" + conf['urltable'] + "` add column `current_url` varchar(500)"
                    self.db_pool.update(altersql)
                except Exception as e:
                    if e.args[0] == 1060:
                        print(conf['urltable'], "current_url 字段已经存在！")
                    else:
                        print(e.args, "更新表字段")
                self.crawlerNext(conf, url, uuid)

    def readOne(self, db_pool, table=''):
        sql = """ select * from %s where statue  is null or statue =0 for update  """ % table
        return db_pool.getOne(sql)

    def updateStatue(self, db_pool, table='', uuid='', statue=1):
        sql = """ update %s set statue = %d,current_url=null where 主键='%s' """ % (table, statue, uuid)
        return db_pool.update(sql)

    def updateCurrent(self, db_pool, table='', uuid='', current=''):
        sql = """ update %s set current_url='%s' where 主键='%s' """ % (table, current, uuid)
        return db_pool.update(sql)


class PageDetail:
    db_pool = MyPymysqlPool("default")
    databaseInsertList = DatabaseInsertList()

    def run(self, conf):
        columnNames = []
        for row in conf['columns']:
            columnNames.append(row['名称'])
        listtable = conf['urltable']
        rule = Rule()
        type_p = 'rg'
        if 'readtype' in conf.keys():
            type_p = conf['readtype']
        chartset = "utf8"
        if 'chartset' in conf.keys():
            chartset = conf['chartset']
        self.databaseInsertList.updateAllStatue(self.db_pool, table=listtable, statue=2)
        listList = self.databaseInsertList.readAll(db_pool=self.db_pool, table=listtable)
        for list in listList:
            self.databaseInsertList.updateStatue2(db_pool=self.db_pool, table=listtable, uuid=list['主键'], statue=2)
            result = rule.crawler_detail(conf=conf, url=list[conf['urlname']], type_p=type_p, chartset=chartset)
            self.databaseInsertList.insertDetail(result=result, table=conf['tablename'],column_names=columnNames, db_pool=self.db_pool)
            self.databaseInsertList.updateStatue2(db_pool=self.db_pool, table=listtable, uuid=list['主键'], statue=1)
            #


if __name__ == '__main__':
    pass
