#-*- coding:utf-8 -*-

class UnknownComponent:
    def build(self, c):
        pass
    
    def start(self, c):
        pass
    
    def stop(self, c):
        pass
    
    def __str__(self):
        return 'unknown'