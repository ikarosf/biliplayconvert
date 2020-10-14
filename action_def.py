# -*- coding: utf-8 -*-
from PySide2 import QtWidgets
import os
from cv2 import VideoCapture
from xml.dom import minidom


def openGetFilesPathDialog(Window, title="选择文件", start_dir=None, extension_name=None):
    fileName_choose, file_type = QtWidgets.QFileDialog.getOpenFileNames(Window,
                                                                        title,
                                                                        start_dir,  # 起始路径
                                                                        extension_name)  # 设置文件扩展名过滤,用双分号间隔
    return fileName_choose


def openGetDirPathDialog(Window, title="选择路径", start_dir=None):
    DirName_choose = QtWidgets.QFileDialog.getExistingDirectory(Window,
                                                                title,
                                                                start_dir,  # 起始路径
                                                                )
    return DirName_choose


def get_video_duration(filename):
    cap = VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num / rate
        return duration
    return -1


def get_fileSize(filename):
    u"""
    获取文件大小（M: 兆）
    """
    file_byte = os.path.getsize(filename)
    return file_byte


def get_xml_num(filename):
    domTree = minidom.parse(filename)
    rootNode = domTree.documentElement
    danmu = rootNode.getElementsByTagName("d")
    return len(danmu)


def get_xml_d_num(filename):
    count = 0
    thefile = open(filename, 'rb')
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count(b'</d>')
    thefile.close()
    return count


def text_lines_num(filename):
    count = 0
    thefile = open(filename, 'rb')
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        count += buffer.count(b'\n')
    thefile.close()
    return count
