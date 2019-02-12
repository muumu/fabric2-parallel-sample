#-*- coding:utf-8 -*-

class Ap:
    def build(self, c):
        c.run('echo "Building application server..."')
    
    def start(self, c):
        c.run('echo "Starting application server..."')
    
    def stop(self, c):
        c.run('echo "Stopping application server..."')
    
    def __str__(self):
        return 'ap'