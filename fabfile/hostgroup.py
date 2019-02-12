#-*- coding:utf-8 -*-
from hostgroupdef import get_host_groups, get_environment_list
from component import get_component_dic

ReverseHostDic = {}

def is_hostname(name):
    global ReverseHostDic
    return name in ReverseHostDic

def get_hosts(name):
    if name in get_host_groups():
        return get_host_groups()[name]
    else:
        return [name]

def get_component(name):
    global ReverseHostDic
    component_name = name.split('.')[0]
    if component_name in get_component_dic():
        return get_component_dic()[component_name]
    elif name in ReverseHostDic:
        return ReverseHostDic[name].component
    else:
        return UnknownComponent

def get_environment(name):
    global ReverseHostDic
    if name in ReverseHostDic:
        return ReverseHostDic[name].environment
    t = name.split('.')
    if len(t) > 1:
        env = t[1]
        if env in get_environment_list():
            return env
    return 'unknown'

def init_reverse_host_dic():
    global ReverseHostDic
    for groupname, hosts in get_host_groups().items():
        for h in hosts:
            ReverseHostDic[h] = {
                'component': get_component(groupname),
                'environement': get_environment(groupname)
                }

init_reverse_host_dic()