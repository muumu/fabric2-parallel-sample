#-*- coding:utf-8 -*-
from functools import wraps
from fabric import task, ThreadingGroup
from hostgroup import get_hosts, get_component, get_environment

group = None

def set_group(name):
    global group
    hosts = get_hosts(name)
    group = ThreadingGroup(*hosts)
    group.hosts = hosts
    group.component = get_component(name)()
    group.environment = get_environment(name)
    return group

def get_group():
    global group
    return group
