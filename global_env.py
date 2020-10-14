# -*- coding: utf-8 -*-
MainWindow = None
recent_audio_path = None
recent_xml_path = None
recent_output_path = None


def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        str1 = 'global ' + key
        exec(str1)
        val = eval(key)
        return val
    except KeyError:
        return defValue


temp_json_text = r'''{"avid":114514114514,"downloaded_bytes":391106180,"guessed_total_bytes":0,"danmaku_count":3000,
"is_completed":true,"page_data":{"cid": 114514114514,"downloadable": true,"has_alias": false,"page": 1,"part": "第一集",
"raw_vid": "","tid": 32,"type": "letv","vid": "0"},"prefered_video_quality":400,"seasion_id":0,"spid":0,
"title":"ikarosf","total_bytes":391106180,"total_time_milli":3521988,"type_tag":"lua.flv.bapi.2"} '''
