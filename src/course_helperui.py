# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'course_helper.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

