# -*- coding: utf-8 -*-
import os
from os import path, mkdir
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import threading
import numpy as np
import configuration


class ExampleApp(QtWidgets.QMainWindow, configuration.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False
        self.flag_right = False

        self.list_path_to_video_file = []
        self.list_of_file_names = []
        self.save_path_matrix_data = []
        self.data = []
        self.label = []

        self.class_saving_path = ""
        self.class_saving_path_right = ""

        self.time_between_frames = float(0.0)
        self.number_of_frames = int(0)
        self.frame_size = int(0)
        self.frame_size_right = int(0)

        self.task = None  # threading.Thread(target=self.start)
        self.task_2 = None  # threading.Thread(target=self.start_right)

        self.Button_upload_video.clicked.connect(self.upload_video)
        self.Button_save_list.clicked.connect(self.save_list)
        self.Button_save_path.clicked.connect(self.save_path)
        self.Button_apply.clicked.connect(self.apply)
        self.Button_start.clicked.connect(self.startON)
        self.Button_stop.clicked.connect(self.stop)
        self.Button_directory_path.clicked.connect(self.directory_path)
        self.Button_apply_right.clicked.connect(self.apply_right)
        self.Button_save_path_right.clicked.connect(self.save_path_right)
        self.Button_start_right.clicked.connect(self.startONright)
        self.Button_stop_right.clicked.connect(self.stop_right)

        self.checkBox_grayscale.clicked.connect(self.grayscale)
        self.checkBox_multicolor.clicked.connect(self.multicolor)

    def grayscale(self):
        pass

    def multicolor(self):
        pass

    def upload_video(self):
        self.Button_upload_video.setStyleSheet('QPushButton {background-color:; color: black;}')
        self.textEdit.clear()
        self.list_path_to_video_file = []
        self.list_of_file_names = []
        position = 0
        self.list_path_to_video_file, ok = QFileDialog.getOpenFileNames(self,
                                                                        'Выберите несколько файлов',
                                                                        ".",
                                                                        "All Files(*.*)")
        for path_ in self.list_path_to_video_file:
            self.list_of_file_names.append(path.basename(path_))
        for name in self.list_of_file_names:
            line_item_and_name = "[" + str(position) + "]" + " - " + name
            self.textEdit.append(line_item_and_name)
            position += 1

    def save_list(self):
        filename, filetype = QFileDialog.getSaveFileName(self, "Сохранить как", ".", "Text Files(*.txt)")
        save_path = ("{}".format(filename, filetype))
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(self.textEdit.toPlainText())

    def save_path(self):
        self.Button_save_path.setStyleSheet('QPushButton {background-color:; color: black;}')
        self.class_saving_path = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.lineEdit_directory_path.clear()
        self.lineEdit_directory_path.setText(self.class_saving_path)

    def apply(self):
        trigger = 0
        self.time_between_frames = float(0.0)
        self.number_of_frames = int(0)
        self.frame_size = int(0)
        try:
            trigger += 1
            self.time_between_frames = float(self.lineEdit_time_between_frames.text())
            self.lineEdit_time_between_frames.setStyleSheet('QLineEdit {background-color: white;}')
        except:
            self.lineEdit_time_between_frames.setStyleSheet('QLineEdit {background-color: red;}')
            trigger -= 1
        try:
            trigger += 1
            self.number_of_frames = int(self.lineEdit_number_of_frames.text())
            self.lineEdit_number_of_frames.setStyleSheet('QLineEdit {background-color: white;}')
        except:
            self.lineEdit_number_of_frames.setStyleSheet('QLineEdit {background-color: red;}')
            trigger -= 1
        try:
            trigger += 1
            self.frame_size = int(self.lineEdit_frame_size.text())
            self.lineEdit_frame_size.setStyleSheet('QLineEdit {background-color: white;}')
        except:
            self.lineEdit_frame_size.setStyleSheet('QLineEdit {background-color: red;}')
            trigger -= 1
        if len(self.list_path_to_video_file) != 0:
            trigger += 1
        else:
            self.Button_upload_video.setStyleSheet('QPushButton {background-color: red; color: white;}')
        if self.class_saving_path != "":
            trigger += 1
        else:
            self.Button_save_path.setStyleSheet('QPushButton {background-color: red; color: white;}')
        if trigger == 5:
            self.flag = True
        else:
            self.flag = False

    def startON(self):
        if self.flag:
            self.task = threading.Thread(target=self.start)
            self.task.start()

        else:
            pass

    def startONright(self):
        if self.flag_right:
            self.task_2 = threading.Thread(target=self.start_right)
            self.task_2.start()

        else:
            pass

    def start(self):
        try:
            self.progressBar_single_file_progress.setMaximum(self.number_of_frames)
            self.progressBar_overall_progress.setMaximum(len(self.list_path_to_video_file))
            flag = True
            self.time_between_frames *= 1000
            timer = self.time_between_frames
            catalog_number = 0
            for _ in range(
                    self.number_of_frames * len(self.list_path_to_video_file) + len(self.list_path_to_video_file)):
                if flag:
                    cont = 0
                    vidcap = cv2.VideoCapture(self.list_path_to_video_file[catalog_number])
                    full_path = self.class_saving_path + "\\" + str(catalog_number)
                    mkdir(full_path)
                    catalog_number += 1
                    flag = False
                else:
                    vidcap.set(cv2.CAP_PROP_POS_MSEC, self.time_between_frames)
                    fuse, image = vidcap.read()
                    if fuse and self.flag:
                        cont += 1
                        image = cv2.resize(image, (self.frame_size, self.frame_size))
                        cv2.imwrite(full_path + "\\" + str(cont) + " " + "_frame.jpg", image)
                        self.time_between_frames += timer
                        self.progressBar_single_file_progress.setValue(cont)
                        if cont == self.number_of_frames:
                            flag = True
                            self.time_between_frames = timer
                            self.progressBar_overall_progress.setValue(catalog_number)
                    else:
                        break
            self.flag = False
        except:
            print("ОШИБКА!")

    def stop(self):
        try:
            self.flag = False
            self.task.join()
            self.progressBar_single_file_progress.setValue(0)
            self.progressBar_overall_progress.setValue(0)
            self.task = None  # threading.Thread(target=self.start)
        except:
            pass

    def stop_right(self):
        try:
            self.flag_right = False
            self.task_2.join()
            self.progressBar_overall_progress_right.setValue(0)
            self.progressBar_single_directory_progress.setValue(0)
            self.task_2 = None  # threading.Thread(target=self.start_right)
        except:
            pass

    def directory_path(self):
        self.Button_directory_path.setStyleSheet('QPushButton {background-color:; color: black;}')
        class_saving_path_right = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.lineEdit_directory_path.clear()
        self.lineEdit_directory_path.setText(class_saving_path_right)

    def save_path_right(self):
        self.Button_save_path_right.setStyleSheet('QPushButton {background-color:; color: black;}')
        save_path_matrix_data = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.lineEdit_directory_path_2.clear()
        self.lineEdit_directory_path_2.setText(save_path_matrix_data)

    def apply_right(self):
        trigger = 0
        self.class_saving_path_right = self.lineEdit_directory_path.text()
        self.save_path_matrix_data = self.lineEdit_directory_path_2.text()
        try:
            trigger += 1
            self.frame_size_right = int(self.lineEdit_frame_size_right.text())
            self.lineEdit_frame_size_right.setStyleSheet('QLineEdit {background-color: white;}')
        except:
            self.lineEdit_frame_size_right.setStyleSheet('QLineEdit {background-color: red;}')
            trigger -= 1
        if self.class_saving_path_right != "":
            trigger += 1
        else:
            self.Button_directory_path.setStyleSheet('QPushButton {background-color: red; color: white;}')
        if len(self.save_path_matrix_data) != 0:
            trigger += 1
        else:
            self.Button_save_path_right.setStyleSheet('QPushButton {background-color: red; color: white;}')
        if trigger == 3:
            self.flag_right = True
        else:
            self.flag_right = False
        print(self.flag_right)

    def start_right(self):
        contDir = 0
        tree = [x[0] for x in os.walk(self.class_saving_path_right)]
        self.progressBar_overall_progress_right.setMaximum(len(tree) - 1)
        for i in range(len(tree) - 1):
            if self.flag_right:
                contDir += 1
                cont = 0
                element = [0 for _ in range(len(tree) - 1)]
                files = os.listdir(tree[i + 1])
                self.progressBar_single_directory_progress.setMaximum(len(files))
                element[i] = 1
                for l in files:
                    if self.flag_right:
                        cont += 1
                        image = cv2.imread(tree[i + 1] + "\\" + l)
                        image = cv2.resize(image, (self.frame_size_right, self.frame_size_right))
                        self.data.append(image)
                        self.label.append(element)
                        self.progressBar_single_directory_progress.setValue(cont)
                    else:
                        break
                self.progressBar_overall_progress_right.setValue(contDir)
            else:
                break
        data = np.array(self.data, dtype="float") / 255.0
        np.save(self.save_path_matrix_data + "\\X_data_multicolor", data)
        np.save(self.save_path_matrix_data + "\\Y_label", self.label)
        self.flag_right = False
