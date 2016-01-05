# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course_helper.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

__author__ = 'Huang Xiongbiao (billo@qq.com)'
__email__ = 'billo@qq.com'
__version__ = '0.0.6(一秒十次郎)'

import time
import urllib2
import urllib
import json
import cookielib
import sys
import os
import StringIO
import Image
import time
import logging
import logging.handlers
reload(sys)
sys.setdefaultencoding("utf-8")

from PyQt4 import QtCore, QtGui, uic


LOG_FILE = 'course_helper.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter

logger = logging.getLogger('course_helper')    # 获取名为tst的logger
logger.addHandler(handler)           # 为logger添加handler
logger.setLevel(logging.DEBUG)

load_pytes = True

try:
    from pytes.pytesser import image_to_string, image_file_to_string
except Exception, e:
    logger.info(str(e))
    load_pytes = False

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

CODE_IMG_PATH = r'D:\code_img.jpg'


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(648, 432)
        self.textEdit_id = QtGui.QTextEdit(Dialog)
        self.textEdit_id.setGeometry(QtCore.QRect(200, 50, 151, 31))
        self.textEdit_id.setObjectName(_fromUtf8("textEdit_id"))
        self.textEdit_password = QtGui.QTextEdit(Dialog)
        self.textEdit_password.setGeometry(QtCore.QRect(200, 90, 151, 31))
        self.textEdit_password.setObjectName(_fromUtf8("textEdit_password"))
        self.label_id = QtGui.QLabel(Dialog)
        self.label_id.setGeometry(QtCore.QRect(140, 60, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_id.setFont(font)
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.label_password = QtGui.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(140, 100, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.fresh_code_btn = QtGui.QPushButton(Dialog)
        self.fresh_code_btn.setGeometry(QtCore.QRect(460, 130, 75, 23))
        self.fresh_code_btn.setObjectName(_fromUtf8("fresh_code_btn"))
        self.label_code = QtGui.QLabel(Dialog)
        self.label_code.setGeometry(QtCore.QRect(130, 140, 61, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_code.setFont(font)
        self.label_code.setObjectName(_fromUtf8("label_code"))
        self.code_img = QtGui.QGraphicsView(Dialog)
        self.code_img.setGeometry(QtCore.QRect(380, 130, 71, 31))
        self.code_img.setObjectName(_fromUtf8("code_img"))
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(200, 380, 75, 23))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.debtex = QtGui.QTextEdit(Dialog)
        self.debtex.setGeometry(QtCore.QRect(370, 180, 251, 191))
        self.debtex.setObjectName(_fromUtf8("debtex"))
        self.textEdit_code = QtGui.QTextEdit(Dialog)
        self.textEdit_code.setGeometry(QtCore.QRect(200, 130, 151, 31))
        self.textEdit_code.setObjectName(_fromUtf8("textEdit_code"))
        self.textEdit_course1 = QtGui.QTextEdit(Dialog)
        self.textEdit_course1.setGeometry(QtCore.QRect(200, 240, 151, 31))
        self.textEdit_course1.setObjectName(_fromUtf8("textEdit_course1"))
        self.textEdit_course2 = QtGui.QTextEdit(Dialog)
        self.textEdit_course2.setEnabled(True)
        self.textEdit_course2.setGeometry(QtCore.QRect(200, 290, 151, 31))
        self.textEdit_course2.setObjectName(_fromUtf8("textEdit_course2"))
        self.textEdit_course3 = QtGui.QTextEdit(Dialog)
        self.textEdit_course3.setGeometry(QtCore.QRect(200, 340, 151, 31))
        self.textEdit_course3.setObjectName(_fromUtf8("textEdit_course3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 239, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 289, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 400, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(400, 380, 191, 31))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.exit_btn = QtGui.QPushButton(Dialog)
        self.exit_btn.setGeometry(QtCore.QRect(300, 380, 51, 23))
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.courseNum_comboBox = QtGui.QComboBox(Dialog)
        self.courseNum_comboBox.setGeometry(QtCore.QRect(200, 190, 41, 21))
        self.courseNum_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.courseNum_comboBox.setObjectName(_fromUtf8("courseNum_comboBox"))
        self.courseNum_comboBox.addItem(_fromUtf8(""))
        self.courseNum_comboBox.addItem(_fromUtf8(""))
        self.courseNum_comboBox.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 190, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("SimSun-ExtB"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "中山大学选课助手v%s" % __version__, None))
        self.label_id.setText(_translate("Dialog", "学号", None))
        self.label_password.setText(_translate("Dialog", "密码", None))
        self.fresh_code_btn.setText(_translate("Dialog", "刷新验证码", None))
        self.label_code.setText(_translate("Dialog", "验证码", None))
        self.login_btn.setText(_translate("Dialog", "登录并选课", None))
        self.label.setText(_translate("Dialog", "课程1教学班号", None))
        self.label_2.setText(_translate("Dialog", "课程2教学班号", None))
        self.label_3.setText(_translate("Dialog", "课程3教学班号", None))
        self.label_4.setText(_translate("Dialog", "中山大学选课助手", None))
        self.label_5.setText(_translate("Dialog", "Bug反馈:billo@qq.com", None))
        self.exit_btn.setText(_translate("Dialog", "退出", None))
        self.courseNum_comboBox.setItemText(0, _translate("Dialog", "1", None))
        self.courseNum_comboBox.setItemText(1, _translate("Dialog", "2", None))
        self.courseNum_comboBox.setItemText(2, _translate("Dialog", "3", None))
        self.label_7.setText(_translate("Dialog", "选课门数", None))


class course_helper(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)

        self.course_list = []
        self.login_btn.clicked.connect(self.start)
        self.fresh_code_btn.clicked.connect(self.get_code_img)
        self.exit_btn.clicked.connect(self.quit)
        self.textEdit_course2.hide()
        self.label_2.hide()
        self.textEdit_course3.hide()
        self.label_3.hide()
        QtGui.QWidget.connect(self.courseNum_comboBox, QtCore.SIGNAL('activated(int)'), self.set_course_num)

        self.username = ""
        self.password = ""
        self.code = ""
        self.sid = False
        self.autoRestart = True
        self.restartTime = 0
        self.debugcontent = u"SYSU course helper By Bill\n注意要填的是教学班号,不是课程号！！！\n在教务系统中点击课程名称后可以看到教学班号\n"
        self.debtex.setText(self.debugcontent)

        self.pick_times = 0
        self.pick_fail = False

        self.Timer = QtCore.QTimer(self)
        self.connect(self.Timer, QtCore.SIGNAL("timeout()"), self.take_course_once)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("D:\Python\pyqtfile\course_helper\logo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        OK = QtGui.QMessageBox.information(self, u'提示', u'中山大学选课助手v%s\n防止对服务器造成过大压力,设置选课间隔为4秒\n本工具仅作学习交流之用\n由此造成的任何问题都与作者无关\n同意后方可使用\n                                                AngryBill\n                                              2015.09.08' % __version__, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if OK != QtGui.QMessageBox.Yes:
            sys.exit(0)

        # self.load_cookie()
        self.get_code_img()

    def quit(self):
        QtGui.QMessageBox.information(self, u'Bye', u'感谢使用,ByeBye:)', QtGui.QMessageBox.Yes)
        sys.exit(0)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.isfile(CODE_IMG_PATH):
            os.remove(CODE_IMG_PATH)

    # 对密码做MD5
    def md5(self, psw):
        import hashlib
        m = hashlib.md5()
        m.update(str(psw))
        md5Result = m.hexdigest().upper()
        # print psw,len(psw),type(psw)
        # print "MD5:" + md5Result
        return  md5Result

    # 根据传入的currentIndex来隐藏/显示 标签/输入框
    def set_course_num(self, currentIndex):
        if currentIndex <= 1:
            self.textEdit_course3.hide()
            self.label_3.hide()
            if currentIndex == 0:
                self.textEdit_course2.hide()
                self.label_2.hide()
            else:
                self.textEdit_course2.show()
                self.label_2.show()
        else:
            self.textEdit_course2.show()
            self.label_2.show()
            self.textEdit_course3.show()
            self.label_3.show()
        return

    # 先获得一个cookie
    def load_cookie(self):
        try:
            # 设置cookie容器
            cookie = cookielib.CookieJar()
            cookieProc = urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(cookieProc)
            urllib2.install_opener(opener)

            self.header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding' : 'gzip,deflate,sdch',
                'Accept-Language' : 'zh-CN,zh;q=0.8',
                'Cache-Control'   : 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Length'  : '80',
                'Content-Type'    : 'application/x-www-form-urlencoded',
                'Host': 'uems.sysu.edu.cn',
                'Origin'          : 'http://uems.sysu.edu.cn',
                'Referer'         : 'http//uems.sysu.edu.cn/elect/',
                'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0',
                }

            # 获取cookies
            req = urllib2.Request(
                        url = 'http://uems.sysu.edu.cn/elect/index.html',
                        headers = self.header
                    )
            res = urllib2.urlopen(req)

        except Exception, e:
            logger.info("load_cookie"+str(e))
            self.debtex.setText(self.debugcontent + str(e))

    def get_code_img(self):
        self.load_cookie()
        # 获取验证码图片
        try:
            # 下载图片
            addr = "http://uems.sysu.edu.cn/elect/login/code"

            # 读到硬盘中
            # img_name = CODE_IMG_PATH
            # open(img_name, "wb").write(urllib2.urlopen(addr).read())
            # self.img = Image.open(img_name)

            # 改为读到内存中
            code_data = StringIO.StringIO(urllib2.urlopen(addr).read())
            self.img = Image.open(StringIO.StringIO(code_data.getvalue()))
            self.processCode()

            # 设置图片
            pixmap = QtGui.QPixmap()
            # pixmap.load(CODE_IMG_PATH)
            pixmap.loadFromData(QtCore.QByteArray(code_data.getvalue()))

            scene = QtGui.QGraphicsScene(self)
            item = QtGui.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.code_img.setScene(scene)
            if os.path.isfile(CODE_IMG_PATH):
                os.remove(CODE_IMG_PATH)

        except Exception, e:
            logger.info("get_code_img"+str(e))
            if not self.autoRestart:
                self.debtex.setText(self.debugcontent + u"[Error]下载验证码失败! 原因:" + str(e))

    # 处理验证码, 识别
    def processCode(self):
        # 二值化
        pixdata = self.img.load()
        for y in xrange(self.img.size[1]):
            for x in xrange(self.img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(self.img.size[1]):
            for x in xrange(self.img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(self.img.size[1]):
            for x in xrange(self.img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        ori_w, ori_h = self.img.size
        # 裁剪边缘
        # 这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
        box = (1, 1, ori_w-1, ori_h-1)
        newIm = self.img.crop(box)
        if load_pytes:
            code = image_to_string(newIm)
            # 自动填写验证码
            self.textEdit_code.setText(code[:4])

    def login(self):
        try:
            # 登录获取ssid
            user = {
                'username' : self.username,
                'password' : self.md5(self.password),
                'j_code': self.code,
                'lt'       : '',
                '_eventId' : 'submit',
                'gateway'  : 'true'
                }

            # 登录
            user = urllib.urlencode(user)
            req = urllib2.Request(
                        url = 'http://uems.sysu.edu.cn/elect/login',
                        data = user,
                        headers = self.header
                    )
            res = urllib2.urlopen(req)

            sid = res.geturl().replace('http://uems.sysu.edu.cn/elect/s/types?sid=', '')
            if not self.restartTime:
                QtGui.QMessageBox.information(self, u'提示', u'登录成功!', QtGui.QMessageBox.Yes)
            return sid
            #print res.read()
        except Exception, e:
            logger.info("login"+str(e))
            if not self.restartTime:
                QtGui.QMessageBox.information(self, u'提示', u'登录失败 账号/密码/验证码错误??  错误原因:'+str(e), QtGui.QMessageBox.Yes)
            return None

    def take_course_once(self):
        # 如果已经选到课或者出错 则停止
        if self.pick_fail:
            self.Timer.stop()
            return
        if not self.course_list:
            QtGui.QMessageBox.information(self, u'提示', u'请输入最少一门课程', QtGui.QMessageBox.Yes)
            return
        # 清屏
        if len(self.debugcontent) > 250:
            self.debugcontent = ""

        self.pick_times += 1

        for jxbh in self.course_list:
            nowtime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
            self.debugcontent += nowtime + u"课程:" + str(jxbh) + "\n"

            try:
                data = {
                    "jxbh": jxbh,
                    "sid": self.sid
                }
                header = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding' : 'gzip,deflate,sdch',
                    'Accept-Language' : 'zh-CN,zh;q=0.8',
                    'Cache-Control'   : 'max-age=0',
                    'Connection': 'keep-alive',
                    'Content-Length'  : '60',
                    'Content-Type'    : 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Host': 'uems.sysu.edu.cn',
                    'Origin'          : 'http://uems.sysu.edu.cn',
                    'Referer'         : 'http://uems.sysu.edu.cn/elect/s/',
                    'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0',
                    'X-Requested-With': 'XMLHttpRequest'
                    }
                data = urllib.urlencode(data)
                req = urllib2.Request(
                            url = 'http://uems.sysu.edu.cn/elect/s/elect',
                            data = data,
                            headers = header
                        )
                res = urllib2.urlopen(req)
                js = json.loads(res.read())
                code = js.get('err').get('code')
                caurse = js.get('err').get('caurse')
                nowtime = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
                s = u"" + nowtime
                if caurse == None:
                    caurse = ""
                if code == 18:
                    s += u"抢不到,再试试吧。。。"
                elif code == 0:
                    QtGui.QMessageBox.information(self, u'提示', u'成功选上了！！！！结束选课。', QtGui.QMessageBox.Yes)
                    s += u"成功选上了这门课！！！！结束选课。"
                elif code == 9:
                    s += u"这门课已经选上了！不要重复选了吧。。。"
                elif code == 5:
                    s += u"选课失败：系统中没有您这个学期的报到记录，不允许选课。请联系您所在院系的教务员申请补注册。"
                elif code == 1:
                    s += u"还没开始选课呢！！"
                else:
                    s += u"未知代码" + str(code)

                self.label_6.setText(u"正在进行第" + str(self.pick_times) + u"轮选课\n")
                self.debugcontent += s + "\n"
                self.debtex.setText(self.debugcontent)

                # 选上课就退出
                if code == 0:
                    self.pick_fail = True
                    break
                logger.info("(code:%s) %s %s" % (code, caurse, s))
            except Exception, e:
                logger.info("take_course_once" + str(e))
                self.pick_fail = True
                self.Timer.stop()
                # 自动重试
                if self.autoRestart:
                    self.restart()
                    return
                else:
                    QtGui.QMessageBox.information(self, u'提示', u"出错/掉线, 请重新登录或确认输入的教学班号是否正确,错误原因:" + str(e), QtGui.QMessageBox.Yes)
                break
                # print "出错, 请重新登录或确认输入的教学班号是否正确", e
        self.Timer.start(100)

    def start(self):
        try:
            self.username = self.textEdit_id.toPlainText()
            self.password = self.textEdit_password.toPlainText()
            self.code = self.textEdit_code.toPlainText()
            self.pick_fail = False
            self.Timer.stop()

            if len(self.code) < 4 or len(self.username) != 8 or self.password == "":
                if self.autoRestart:
                    self.restart()
                else:
                    QtGui.QMessageBox.information(self, u'提示', u'请输入正确的学号/密码/验证码', QtGui.QMessageBox.Yes)
                return

            # 计算出Content-Length
            self.header['Content-Length'] = str(72+len(self.md5(self.password)))

            self.debtex.setText(self.debugcontent + u"登录中...\n")

            # 登陆
            self.sid = self.login()
            if self.sid:
                self.debugcontent += u"登录成功..Sid:" + self.sid + "\n"
                self.debtex.setText(self.debugcontent)
                # 获取教学班号列表
                self.read_course()
                # print self.course_list
                self.take_course_once()
            else:
                if self.autoRestart:
                    self.restart()
                else:
                    # 登陆失败 刷新验证码
                    self.get_code_img()
                    self.debugcontent += u"登录失败- -再试试吧\n"
                    self.debtex.setText(self.debugcontent)
        except Exception,e:
            logger.info("start" + str(e))

    def read_course(self):
        # 添加课程
        self.course_list = []
        l = [self.textEdit_course1, self.textEdit_course2, self.textEdit_course3]
        for course in l:
            if course.toPlainText() != "":
                self.course_list.append(course.toPlainText())

    def restart(self):
        self.restartTime += 1
        self.Timer.stop()
        self.get_code_img()
        self.start()


app = QtGui.QApplication(sys.argv)
window = course_helper()
window.show()
sys.exit(app.exec_())



