# -*- coding: utf-8 -*-

import os
import sys

from PySide2.QtWidgets import QApplication

import global_env
from TopWindow import MainWindow

# 打包exe文件用，编程时请注释
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join('.', 'plugins')

if __name__ == '__main__':
    # logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    #                     datefmt="%Y/%d/%m %H:%M:%S",
    #                     level=logging.CRITICAL)
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    global_env.MainWindow = MainWindow
    MainWindow.show()
    sys.exit(app.exec_())
