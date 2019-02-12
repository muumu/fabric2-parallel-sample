#-*- coding:utf-8 -*-

from ap import Ap
from web import Web

ComponentDic = {
    'web': Web,
    'ap': Ap
}

def get_component_dic():
    global ComponentDic
    return ComponentDic