import os
from shutil import copy as s_copy
import json
import random

from PySide2.QtCore import QThread, Signal

import global_env, action_def

newlines = ['\n', '\r\n', '\r']


class AnsyWorker(QThread):
    append_signal = Signal(str)
    status_signal = Signal(str)
    end_signal = Signal()

    def __init__(self, parent, audiopathlist, xmlpathlist, titlelist, maindir, name):
        super().__init__(parent)
        self.audiopathlist = audiopathlist
        self.xmlpathlist = xmlpathlist
        self.titlelist = titlelist
        self.maindir = maindir
        self.name = name

        global_env.MainWindow.tipstextBrowser.setText("")
        global_env.MainWindow.ableAllButton(False)
        self.append_signal.connect(append_signal_do)
        self.status_signal.connect(status_signal_do)
        self.end_signal.connect(end_signal_do)

    def log_append(self, text):
        self.append_signal.emit(text)

    def run(self):
        try:
            name_id = random.randint(100000000000, 999999999999)
            infoList = []
            mainNameDir = os.path.join(self.maindir, str(name_id))

            self.log_append("开始获取视频信息")
            for i in range(len(self.audiopathlist)):
                audiopath = self.audiopathlist[i]
                xmlpath = self.xmlpathlist[i]
                title = self.titlelist[i]

                try:
                    video_duration = action_def.get_video_duration(audiopath)
                    if video_duration <= 0:
                        raise Exception("无法获取视频时长")
                    video_duration = int(1000 * video_duration)
                except Exception as e:
                    self.log_append("未获取到" + audiopath + "的时长")
                    self.log_append(str(e))
                    video_duration = 1440000

                try:
                    video_size = action_def.get_fileSize(audiopath)
                    if video_size <= 0:
                        raise Exception("无法获取视频大小")
                except Exception as e:
                    self.log_append("未获取到" + audiopath + "的大小")
                    self.log_append(str(e))
                    video_size = 391106180

                try:
                    danmu_len = action_def.get_xml_d_num(xmlpath)
                except Exception as e:
                    self.log_append("未获取到" + xmlpath + "的弹幕数量")
                    self.log_append(str(e))
                    danmu_len = 0

                print(video_duration)
                print(video_size)
                print(danmu_len)
                info_dict = {}
                info_dict["page"] = i + 1
                info_dict["audiopath"] = audiopath
                info_dict["xmlpath"] = xmlpath
                info_dict["title"] = title
                info_dict["video_duration"] = video_duration
                info_dict["video_size"] = video_size
                info_dict["danmu_len"] = danmu_len
                info_dict["cid"] = name_id + i

                infoList.append(info_dict)

            self.log_append("视频信息获取完毕")
            self.log_append("开始写入配置文件")
            os.makedirs(mainNameDir)
            for i in infoList:
                temp_json = json.loads(global_env.temp_json_text)
                temp_json["avid"] = name_id
                temp_json["downloaded_bytes"] = i["video_size"]
                temp_json["total_bytes"] = i["video_size"]
                temp_json["danmaku_count"] = i["danmu_len"]
                temp_json["title"] = self.name
                temp_json["total_time_milli"] = i["video_duration"]
                # temp_json["type_tag"] = i[]
                temp_json["page_data"]["cid"] = i["cid"]
                temp_json["page_data"]["page"] = i["page"]
                temp_json["page_data"]["part"] = i["title"]

                os.makedirs(os.path.join(mainNameDir, str(i["page"])))
                with open(os.path.join(mainNameDir, str(i["page"]), "entry.json"), "w", encoding='utf-8') as f:
                    json.dump(temp_json, f, ensure_ascii=False)

            self.log_append("写入配置文件完成")
            self.log_append("开始移入视频、弹幕")
            for i in infoList:
                self.log_append(i["audiopath"])
                s_copy(i["audiopath"], os.path.join(mainNameDir, str(i["page"]), "lua.flv.bapi.2_remux.mp4"))
                s_copy(i["xmlpath"], os.path.join(mainNameDir, str(i["page"]), "danmaku.xml"))
            self.log_append("移入视频、弹幕完成")

            self.log_append("成功!")

        except Exception as e:
            print(e.args)
            print(str(e))
            print(repr(e))
            self.log_append(str(e))

        self.end_signal.emit()


def status_signal_do(text):
    global_env.mainWin.statusbar.showMessage(text)


def append_signal_do(text):
    textBrowser = global_env.MainWindow.tipstextBrowser
    textBrowser.insertPlainText(text + "\n")
    textBrowser.moveCursor(textBrowser.textCursor().End)


def end_signal_do():
    global_env.MainWindow.ableAllButton(True)
