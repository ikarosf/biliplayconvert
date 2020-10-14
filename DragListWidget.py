from PySide2.QtCore import (Qt)
from PySide2.QtWidgets import *


class DragListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def setDragTrig(self, fun):
        self.fun = fun

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.CopyAction)
            except Exception as e:
                print(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    links.append(str(url.toLocalFile()))
                self.fun(links)
            else:
                event.ignore()
        except Exception as e:
            print(e)
