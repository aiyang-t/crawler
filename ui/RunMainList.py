# -*- coding: utf-8 -*-

import sys
from ui.mainList import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QHBoxLayout,QWidget,QPushButton,QTableWidgetItem
from common.HtmlSource import HtmlSource
from common.RuleConf import Rule
from common.inc_file import File_file
from lxml import html

import uuid
import time

class RunMainList(QWidget, Ui_Form):
    html_context = ""
    conf = {
        "url": '',
        "body_content_xpath": "",
        "columns": [],
        "nextpage": ""
    }
    body_content_list = []

    # 初始化信息
    def __init__(self):
        super(RunMainList, self).__init__()
        try:
            self.setupUi(self)

            # 隐藏表格
            self.tableView.setVisible(False)
            self.tableWidget.setVisible(False)

            # 设置测试数据
            self.urlLineEdit.setText("http://www.xuexi111.org/yingyv/")
            # url 测试
            self.urlbutton.clicked.connect(self.openUrl)
            # body_content_xpath 测试
            self.pushButton.clicked.connect(self.testBody)
            # 列表配置测试
            self.pushButton_2.clicked.connect(self.testColumn)
            # 添加配置
            self.pushButton_3.clicked.connect(self.addColumn)
            # 测试下一页
            self.pushButton_4.clicked.connect(self.testNextPage)
            # 测试爬虫
            self.nextPage.clicked.connect(self.testCrawler)

            # 保存配置
            self.saveConfButton.clicked.connect(self.saveConf)
            #self.saveConf.setVisible(False)

        except BaseException:
            print(BaseException.args)

    # 定义槽函数 获取html页面
    def openUrl(self):
        self.textBrowser.setVisible(True)
        self.tableView.setVisible(False)

        self.conf["url"] = self.urlLineEdit.text()
        # 加载外部页面，调用
        # self.webEngineView.setUrl(QtCore.QUrl(url))
        # print(self.conf["url"])
        htmlSource = HtmlSource()
        self.html_context = htmlSource.get_html(url_p=self.conf["url"], type_p='rg')
        self.textBrowser.setText(self.html_context)
        self.lineEdit.setText("//div[@class =\"padd w645\"]/div[@class=\"list_left\"]/div[@class=\"topic-list\"]/ul/li")
        self.lineEdit_4.setText(
            "//div[@class =\"padd w645\"]/div[@class=\"list_left\"]/div[@class=\"show-page\"]/a[@class=\"next\"]/@href")

    # 定义槽函数 body 信息
    def testBody(self):
        self.conf["body_content_xpath"] = self.lineEdit.text()
        tree = html.fromstring(self.html_context)
        result_list = tree.xpath(self.conf['body_content_xpath'])
        if (len(result_list) > 0):
            self.body_content_list = result_list
            self.lineEdit_3.setText('')
            self.lineEdit_2.setText('')
            # 其他按钮允许点击
            # 定义一个字段的读取配置
            self.column = {
                "uuid": uuid.uuid4(),
                "名称": '',  # 必须
                "规则": '',  # 必须
                "类型": '',  # 必须
                "c_append_befor": '',
                "c_append_after": '',
                "c_strart_index": '',
                "c_end_len": '',
                "c_replace_char": ''
            }
            self.lineEdit_2.setText('标题')
            self.lineEdit_3.setText('./h3/a/text()')

    # 定义槽函数 列测试信息
    def testColumn(self):
        self.textBrowser.setVisible(True)
        self.tableView.setVisible(False)

        self.column["名称"] = self.lineEdit_2.text()
        self.column["规则"] = self.lineEdit_3.text()
        self.column["类型"] = self.comboBox.currentText()

        strlist = ""
        rule = Rule()
        for row in self.body_content_list:
            column_text = rule._analysis_(tree=row, column=self.column)
            strlist += column_text + "\r\n"
        self.textBrowser.setText(strlist)

    # 定义槽函数 列添加配置信息
    def addColumn(self):
        # 判断填写规则不为空
        if (self.column['规则'] == ""):
            return
        # 判断列名称 不为空
        if (self.column['名称'] == ""):
            return

        flag = True
        for t_column in self.conf["columns"]:
            if (t_column['uuid'] == self.column['uuid']):
                flag = False
                t_column = self.column
            elif (t_column['名称'] == self.column['名称']):
                # 同名不同id 的应该给出提示
                flag = False
                t_column = self.column
        if (flag == True):
            self.conf['columns'].append(self.column)

            # 初始化配置
            self.lineEdit_3.setText('')
            self.lineEdit_2.setText('')
            self.column = {
                "uuid": str(uuid.uuid4()),
                "名称": '',  # 必须
                "规则": '',  # 必须
                "类型": '',  # 必须
                "c_append_befor": '',
                "c_append_after": '',
                "c_strart_index": '',
                "c_end_len": '',
                "c_replace_char": ''
            }
            self.lineEdit_2.setText('连接')
            self.lineEdit_3.setText('./h3/a/@href')
            self.comboBox.setCurrentText("连接")

        # 动态展示添加好的列配置，并绑定删除 TODO

        # 更新配置展示
        self.showColumns()

        # 更新表格数据
        self.showTable()

    # 展示配置信息
    def showColumns(self):

        self.tableWidget.setVisible(True)

        title = ["名称", "规则", "类型", "操作"]

        # 设置数据层次结构，4行4列
        self.tableWidget.setRowCount(len(self.conf["columns"]))  # 行下标最大值
        self.tableWidget.setColumnCount(len(title))  # 列

        # 设置水平方向四个头标签文本内容
        self.tableWidget.setHorizontalHeaderLabels(title)

        for row in range(len(self.conf["columns"])):
            for column in range(len(title)):
                if (title[column] == "操作"):
                    button = self.buttonForRow(str(self.conf["columns"][row]["uuid"]))
                    # 设置每个位置的按钮
                    self.tableWidget.setCellWidget(row, column, button)
                else:
                    item = QTableWidgetItem(self.conf["columns"][row][title[column]])
                    # 设置每个位置的文本值
                    self.tableWidget.setItem(row, column, item)
        # 实例化表格视图，设置模型为自定义的模型
        # self.tableWidget(self.tableWidget.model)

    # 列表内添加按钮
    def buttonForRow(self, id):

        widget = QWidget()
        # 修改
        updateBtn = QPushButton('修改')
        updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')
        updateBtn.clicked.connect(lambda: self.updateConfig(id))

        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def updateConfig(self, id):

        print("1")

    # 测试下一页的配置
    def testNextPage(self):
        self.conf["nextpage"] = self.lineEdit_4.text()
        tree = html.fromstring(self.html_context)
        nextpageurl = tree.xpath(self.conf['nextpage'])
        if (len(nextpageurl) > 0):
            self.textBrowser.setVisible(True)
            self.tableView.setVisible(False)
            self.textBrowser.setText(nextpageurl[0])

    # 测试爬虫整体配置
    def testCrawler(self):
        # 传入下一页url
        self.crawler(self.conf['url'], times=1)
        # 获取页面
        # 获取列表区域信息
        # 解析字段
        # 输出结果
        # 解析下一页url

    # 爬虫预览
    def crawler(self, nextPageUrl='', times=1):
        if (times > 5):
            return
        times = times + 1
        # 表格头信息
        title = []
        for column in self.conf['columns']:
            title.append(column['名称'])
        # 输出表格头 TODO
        print(1)

        self.textBrowser.setVisible(True)
        self.tableView.setVisible(False)

        htmlSource = HtmlSource()
        html_context = htmlSource.get_html(url_p=nextPageUrl, type_p='rg')
        self.textBrowser.setText(html_context)
        time.sleep(1)
        tree = html.fromstring(html_context)
        result_list = tree.xpath(self.conf['body_content_xpath'])
        if (len(result_list) > 0):
            # 表格数据
            rule = Rule()
            list = rule._analysis_list(list=result_list, columns=self.conf["columns"])
            # TODO 输出数据
            print(list)

            # 设置数据层次结构，4行4列
            self.tableView.model = QStandardItemModel(len(list), len(self.conf['columns']))
            # 设置水平方向四个头标签文本内容
            self.tableView.model.setHorizontalHeaderLabels(title)

            for row in range(len(list)):
                for column in range(len(title)):
                    item = QStandardItem(list[row][title[column]])
                    # 设置每个位置的文本值
                    self.tableView.model.setItem(row, column, item)
            # 实例化表格视图，设置模型为自定义的模型
            self.tableView.setModel(self.tableView.model)
            # 展示表格
            self.textBrowser.setVisible(False)
            self.tableView.setVisible(True)
            time.sleep(1)
        # 下一页url
        nextpageurl = tree.xpath(self.conf['nextpage'])
        # 递归调用
        if (len(nextpageurl) > 0):
            print(nextpageurl[0])
            self.crawler(nextPageUrl=nextpageurl[0], times=times)

    # 预览信息
    def showTable(self):
        # 表格头信息
        title = []
        for column in self.conf['columns']:
            title.append(column['名称'])
        # 表格数据
        rule = Rule()
        list = rule._analysis_list(list=self.body_content_list, columns=self.conf["columns"])

        # 设置数据层次结构，4行4列
        self.tableView.model = QStandardItemModel(len(list), len(self.conf['columns']))
        # 设置水平方向四个头标签文本内容
        self.tableView.model.setHorizontalHeaderLabels(title)

        for row in range(len(list)):
            for column in range(len(title)):
                item = QStandardItem(list[row][title[column]])
                # 设置每个位置的文本值
                self.tableView.model.setItem(row, column, item)
        # 实例化表格视图，设置模型为自定义的模型
        self.tableView.setModel(self.tableView.model)
        # 展示表格
        self.textBrowser.setVisible(False)
        self.tableView.setVisible(True)

    # 实例化配置信息到管理中心
    def saveConf(self):
        # TODO 上传到服务器、保存数据到数据库提供监控查询点
        # 弹窗输入配置的名称，配置执行控制的条件、定时配置等等信息录入到数据库
        filename = "testxuexi111.json"
        # 保存配置
        file = File_file()
        file.save_source(path="./configs", file=filename, all_the_text=str(self.conf))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RunMainList()

    # ui.setWindowOpacity(0.98) # 窗口透明
    window.show()
    sys.exit(app.exec_())

