#-*- coding:utf-8 -*-

class Web:
    def build(self, c):
        return c.sudo('echo "Building web server..."')

    def start(self, c):
        return c.run('echo "Starting web server..."')

    def stop(self, c):
        return c.run('echo "Stopping web server..."')

    def __str__(self):
        return 'web'