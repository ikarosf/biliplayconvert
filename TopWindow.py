import os

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox, QAbstractItemView

from ansyrun import AnsyWorker
from bpcMainWindow import Ui_MainWindow
import action_def
import global_env


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setWindowIcon(QtGui.QIcon(':/favicon.ico'))
        self.setButtonAction()
        self.audiopathlistWidget.setDragTrig(self.addaudiopathfromdrag)
        self.xmlpathlistWidget.setDragTrig(self.addxmlpathfromdrag)
        self.testlist()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.audiopathlistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.xmlpathlistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tipstextBrowser.setText(
            '''按顺序选择视频和对应的弹幕，并且填写每集的标题和合集名称
            名称尽量不要用符号，避免引起错误
            视频最好使用mp4、flv格式，易于识别
            弹幕需要是b站的，其他网站的b站可能播不出来
            完成后将文件夹移入手机目录/Android/data/tv.danmaku.bili/download/
                                                                  ——ikarosf
            ''')

    def setButtonAction(self):
        self.addaudiopathpushButton.clicked.connect(lambda: self.addaudiopathfun())
        self.delaudiopathpushButton.clicked.connect(lambda: self.delaudiopathfun())
        self.addxmlpathpushButton.clicked.connect(lambda: self.addxmlpathfun())
        self.delxmlpathpushButton.clicked.connect(lambda: self.delxmlpathfun())
        self.runpushButton.clicked.connect(lambda: self.runfun())

    def addaudiopathfun(self):
        pathList = action_def.openGetFilesPathDialog(self, start_dir=global_env.recent_audio_path)
        if len(pathList) > 0:
            global_env.recent_audio_path = os.path.dirname(pathList[0])
        self.audiopathlistWidget.addItems(pathList)

    def addaudiopathfromdrag(self, pathList):
        self.audiopathlistWidget.addItems(pathList)

    def delaudiopathfun(self):
        selectedItemslist = self.audiopathlistWidget.selectedItems()
        for i in selectedItemslist:
            row = self.audiopathlistWidget.row(i)
            self.audiopathlistWidget.takeItem(row)

    def addxmlpathfun(self):
        pathList = action_def.openGetFilesPathDialog(self, "选择弹幕", start_dir=global_env.recent_xml_path,
                                                     extension_name="弹幕文件 (*.xml)")
        if len(pathList) > 0:
            global_env.recent_xml_path = os.path.dirname(pathList[0])
        self.xmlpathlistWidget.addItems(pathList)

    def addxmlpathfromdrag(self, pathList):
        for i in pathList:
            if not i.lower().endswith(".xml"):
                QMessageBox.critical(self, "错误", "只能选择xml文件")
                return
        self.xmlpathlistWidget.addItems(pathList)

    def delxmlpathfun(self):
        selectedItemslist = self.xmlpathlistWidget.selectedItems()
        for i in selectedItemslist:
            row = self.xmlpathlistWidget.row(i)
            self.xmlpathlistWidget.takeItem(row)

    def runfun(self):
        result, message = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message)
            return

        recent_output_path = action_def.openGetDirPathDialog(self, "选择输出保存路径", global_env.recent_output_path)
        if recent_output_path == "":
            return
        global_env.recent_output_path = recent_output_path
        audiopathlist = []
        xmlpathlist = []
        for i in range(self.audiopathlistWidget.count()):
            audiopathlist.append(self.audiopathlistWidget.item(i).text())
        for i in range(self.xmlpathlistWidget.count()):
            xmlpathlist.append(self.xmlpathlistWidget.item(i).text())
        titlelist = self.titlesplainTextEdit.toPlainText().split("\n")
        name = self.namelineEdit.text()
        mythread = AnsyWorker(self, audiopathlist, xmlpathlist, titlelist, recent_output_path, name)
        mythread.start()

    def ableCheck(self):
        audio_num = self.audiopathlistWidget.count()
        xml_num = self.xmlpathlistWidget.count()
        if audio_num != xml_num:
            return False, "视频与弹幕数量不匹配"
        plainText = self.titlesplainTextEdit.toPlainText()
        if plainText == "":
            title_num = 0
        else:
            title_num = len(plainText.split("\n"))
        if audio_num != title_num:
            return False, "视频与标题数量不匹配"
        if audio_num == 0:
            return False, "没有选择"

        for i in range(xml_num):
            item = self.xmlpathlistWidget.item(i)
            if os.path.splitext(item.text())[1] != ".xml":
                return False, "弹幕文件" + os.path.splitext(item.text())[1] + "的后缀必须是.xml"

        name = self.namelineEdit.text()
        if name == "":
            return False, "合集名称不能为空"
        # for i in range(audio_num):
        #     item = self.audiopathlistWidget.item(i)
        #     time = action_def.get_video_duration(item.text())
        #     print(time)

        return True, "无错误"

    def ableAllButton(self, flag):
        self.addaudiopathpushButton.setEnabled(flag)
        self.addxmlpathpushButton.setEnabled(flag)
        self.delaudiopathpushButton.setEnabled(flag)
        self.delxmlpathpushButton.setEnabled(flag)
        self.runpushButton.setEnabled(flag)

    def testlist(self):
        # audiolist = [r'H:\动漫\3330550\4\lua.mp4.bapi.2_remux.mp4', r'H:\动漫\3330550\5\lua.mp4.bapi.2_remux.mp4',
        #              r'H:\动漫\114515\6\lua.flv.bapi.2_remux.mp4']
        # xmllist = [r'H:\动漫\3330550\4\danmaku.xml', r'H:\动漫\3330550\5\danmaku.xml',
        #            r'H:\动漫\114515\6\danmaku.xml']
        titletext = '''一
二
三
四
五
六
七
八
九
十
十一
十二
十三
十四
十五
十六
十七
十八
十九
二十
二一
二二
二三
二四'''
        # self.audiopathlistWidget.addItems(audiolist)
        # self.xmlpathlistWidget.addItems(xmllist)
        self.titlesplainTextEdit.setPlainText(titletext)
        # self.namelineEdit.setText("合集名称")
        self.namelineEdit.setPlaceholderText("请填写合集名称")
    # def wheelEvent(self, event):
    #     super()
    #
    #     angle=event.angleDelta() / 108                                           # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
    #     angleX=angle.x()  # 水平滚过的距离(此处用不上)
    #     angleY=angle.y()  # 竖直滚过的距离
    #     if angleY > 0:
    #         action_def.previous_page()
    #         print("鼠标滚轮上滚")  # 响应测试语句
    #     else:                                                                  # 滚轮下滚
    #         action_def.next_page()
    #         print("鼠标滚轮下滚")  # 响应测试语句


'''
    def closeEvent(self, event):
        if not global_env.data_saved:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '将关闭程序',
                                                   "是否保存？",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
                                                   QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Yes:
                global_env.keep_data_store()
                event.accept()
            elif reply == QtWidgets.QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(QtCore.Qt.CopyAction)
            except Exception as e:
                logging.debug(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(QtCore.Qt.CopyAction)
                event.accept()
                for url in event.mimeData().urls():
                    link = str(url.toLocalFile())
                    break
                action_def.sc_load_file(link)
            else:
                event.ignore()
        except Exception as e:
            print(e)
'''
