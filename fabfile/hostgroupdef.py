#-*- coding:utf-8 -*-

# <component_name>.<environment>[.<group_number>]
HostGroups = {
    'web.dev': ['web.dev.example.com'],
    'ap.dev': ['ap.dev.example.com'],
    'web.prod.1': ['web001.example.com'],
    'web.prod.2': ['web{:03d}.example.com'.format(n) for n in range(2,4)],
    'web.prod.3': ['web{:03d}.example.com'.format(n) for n in range(4,6)],
    'ap.prod.1': ['ap001.example.com'],
    'ap.prod.2': ['ap{:03d}.example.com'.format(n) for n in range(2,4)],
    'ap.prod.3': ['ap{:03d}.example.com'.format(n) for n in range(4,6)]
}

def get_environment_list():
    return ['dev', 'prod']

def get_host_groups():
    global HostGroups
    return HostGroups