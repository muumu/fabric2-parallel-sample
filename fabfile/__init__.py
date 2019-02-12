#-*- coding:utf-8 -*-
from fabric import task
from groupcontext import set_group, get_group

@task
def group(c, name):
    print(name)
    group = set_group(name)
    print('hosts: [' + ','.join(group.hosts) + ']')
    print('component: ' + str(group.component))
    print('environment: ' + group.environment)

@task
def run(c, command=None, warn=False, print_result=True):
    c = get_group()
    r = c.run(command, warn=warn)
    if print_result:
        for connection, result in r.items():
            print(connection.host + ': ' + result.stdout.strip())
    return r

@task
def build(c):
    c = get_group()
    return c.component.build(c)

@task
def start(c):
    c = get_group()
    return c.component.start(c)

@task
def stop(c):
    c = get_group()
    return c.component.stop(c)