#-*- coding:utf-8 -*-

class Web:
    def build(self, c):
        c.run('echo "Building web server..."')
    
    def start(self, c):
        c.run('echo "Starting web server..."')
    
    def stop(self, c):
        c.run('echo "Stopping web server..."')

    def __str__(self):
        return 'web'