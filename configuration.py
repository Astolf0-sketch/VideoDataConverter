# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(860, 430)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(860, 430))
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, 0, 41, 411))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.Button_upload_video = QtWidgets.QPushButton(self.centralwidget)
        self.Button_upload_video.setEnabled(True)
        self.Button_upload_video.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_upload_video.setFont(font)
        self.Button_upload_video.setObjectName("Button_upload_video")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 0, 281, 161))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 40, 131, 20))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.Button_save_path = QtWidgets.QPushButton(self.centralwidget)
        self.Button_save_path.setGeometry(QtCore.QRect(0, 120, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_save_path.setFont(font)
        self.Button_save_path.setObjectName("Button_save_path")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 100, 131, 20))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.Button_save_list = QtWidgets.QPushButton(self.centralwidget)
        self.Button_save_list.setGeometry(QtCore.QRect(0, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_save_list.setFont(font)
        self.Button_save_list.setObjectName("Button_save_list")
        self.lineEdit_time_between_frames = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time_between_frames.setGeometry(QtCore.QRect(50, 200, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_time_between_frames.setFont(font)
        self.lineEdit_time_between_frames.setAcceptDrops(False)
        self.lineEdit_time_between_frames.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_time_between_frames.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_time_between_frames.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time_between_frames.setObjectName("lineEdit_time_between_frames")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 160, 441, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 180, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_number_of_frames = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_of_frames.setGeometry(QtCore.QRect(200, 200, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_number_of_frames.setFont(font)
        self.lineEdit_number_of_frames.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number_of_frames.setObjectName("lineEdit_number_of_frames")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 180, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_frame_size = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frame_size.setGeometry(QtCore.QRect(340, 200, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_frame_size.setFont(font)
        self.lineEdit_frame_size.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_frame_size.setObjectName("lineEdit_frame_size")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(0, 290, 441, 20))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.Button_apply = QtWidgets.QPushButton(self.centralwidget)
        self.Button_apply.setGeometry(QtCore.QRect(40, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_apply.setFont(font)
        self.Button_apply.setObjectName("Button_apply")
        self.Button_start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start.setGeometry(QtCore.QRect(190, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName("Button_start")
        self.progressBar_single_file_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_single_file_progress.setGeometry(QtCore.QRect(10, 330, 421, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_single_file_progress.setFont(font)
        self.progressBar_single_file_progress.setProperty("value", 0)
        self.progressBar_single_file_progress.setObjectName("progressBar_single_file_progress")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.progressBar_overall_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_overall_progress.setGeometry(QtCore.QRect(10, 380, 421, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_overall_progress.setFont(font)
        self.progressBar_overall_progress.setProperty("value", 0)
        self.progressBar_overall_progress.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_overall_progress.setObjectName("progressBar_overall_progress")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 360, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.Button_stop.setGeometry(QtCore.QRect(330, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_stop.setFont(font)
        self.Button_stop.setObjectName("Button_stop")
        self.Button_directory_path = QtWidgets.QPushButton(self.centralwidget)
        self.Button_directory_path.setGeometry(QtCore.QRect(450, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_directory_path.setFont(font)
        self.Button_directory_path.setObjectName("Button_directory_path")
        self.lineEdit_directory_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_directory_path.setGeometry(QtCore.QRect(590, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_directory_path.setFont(font)
        self.lineEdit_directory_path.setObjectName("lineEdit_directory_path")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(438, 40, 431, 20))
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setMidLineWidth(1)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(438, 170, 421, 20))
        self.line_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_9.setLineWidth(2)
        self.line_9.setMidLineWidth(1)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setObjectName("line_9")
        self.checkBox_multicolor = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_multicolor.setGeometry(QtCore.QRect(460, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_multicolor.setFont(font)
        self.checkBox_multicolor.setObjectName("checkBox_multicolor")
        self.checkBox_grayscale = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_grayscale.setGeometry(QtCore.QRect(580, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_grayscale.setFont(font)
        self.checkBox_grayscale.setObjectName("checkBox_grayscale")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(438, 230, 421, 20))
        self.line_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_10.setLineWidth(2)
        self.line_10.setMidLineWidth(1)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setObjectName("line_10")
        self.Button_save_path_right = QtWidgets.QPushButton(self.centralwidget)
        self.Button_save_path_right.setGeometry(QtCore.QRect(460, 130, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_save_path_right.setFont(font)
        self.Button_save_path_right.setObjectName("Button_save_path_right")
        self.Button_apply_right = QtWidgets.QPushButton(self.centralwidget)
        self.Button_apply_right.setGeometry(QtCore.QRect(470, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_apply_right.setFont(font)
        self.Button_apply_right.setObjectName("Button_apply_right")
        self.Button_start_right = QtWidgets.QPushButton(self.centralwidget)
        self.Button_start_right.setGeometry(QtCore.QRect(600, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_start_right.setFont(font)
        self.Button_start_right.setObjectName("Button_start_right")
        self.Button_stop_right = QtWidgets.QPushButton(self.centralwidget)
        self.Button_stop_right.setGeometry(QtCore.QRect(750, 250, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_stop_right.setFont(font)
        self.Button_stop_right.setObjectName("Button_stop_right")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(438, 290, 421, 20))
        self.line_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_11.setLineWidth(2)
        self.line_11.setMidLineWidth(1)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setObjectName("line_11")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 310, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.progressBar_single_directory_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_single_directory_progress.setGeometry(QtCore.QRect(480, 330, 371, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_single_directory_progress.setFont(font)
        self.progressBar_single_directory_progress.setProperty("value", 0)
        self.progressBar_single_directory_progress.setObjectName("progressBar_single_directory_progress")
        self.progressBar_overall_progress_right = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_overall_progress_right.setGeometry(QtCore.QRect(480, 380, 371, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_overall_progress_right.setFont(font)
        self.progressBar_overall_progress_right.setProperty("value", 0)
        self.progressBar_overall_progress_right.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_overall_progress_right.setObjectName("progressBar_overall_progress_right")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 360, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_frame_size_right = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_frame_size_right.setGeometry(QtCore.QRect(480, 80, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_frame_size_right.setFont(font)
        self.lineEdit_frame_size_right.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_frame_size_right.setObjectName("lineEdit_frame_size_right")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 60, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_directory_path_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_directory_path_2.setGeometry(QtCore.QRect(580, 140, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_directory_path_2.setFont(font)
        self.lineEdit_directory_path_2.setObjectName("lineEdit_directory_path_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(312, 170, 41, 71))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(157, 170, 41, 71))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_upload_video.setText(_translate("MainWindow", "upload video"))
        self.Button_save_path.setText(_translate("MainWindow", "save path"))
        self.Button_save_list.setText(_translate("MainWindow", "save list"))
        self.label.setText(_translate("MainWindow", "time between frames"))
        self.label_2.setText(_translate("MainWindow", "number of frames"))
        self.label_3.setText(_translate("MainWindow", "frame size"))
        self.Button_apply.setText(_translate("MainWindow", "apply"))
        self.Button_start.setText(_translate("MainWindow", "start"))
        self.label_4.setText(_translate("MainWindow", "single file progress"))
        self.label_5.setText(_translate("MainWindow", "overall progress"))
        self.Button_stop.setText(_translate("MainWindow", "stop"))
        self.Button_directory_path.setText(_translate("MainWindow", "directory path"))
        self.checkBox_multicolor.setText(_translate("MainWindow", "multicolor"))
        self.checkBox_grayscale.setText(_translate("MainWindow", "grayscale"))
        self.Button_save_path_right.setText(_translate("MainWindow", "save path"))
        self.Button_apply_right.setText(_translate("MainWindow", "apply"))
        self.Button_start_right.setText(_translate("MainWindow", "start"))
        self.Button_stop_right.setText(_translate("MainWindow", "stop"))
        self.label_7.setText(_translate("MainWindow", "single directory progress"))
        self.label_8.setText(_translate("MainWindow", "overall progress"))
        self.label_9.setText(_translate("MainWindow", "frame size"))