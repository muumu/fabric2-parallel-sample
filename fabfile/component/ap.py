#-*- coding:utf-8 -*-

class Ap:
    def build(self, c):
        return c.sudo('echo "Building application server..."')

    def start(self, c):
        return c.run('echo "Starting application server..."')

    def stop(self, c):
        return c.run('echo "Stopping application server..."')

    def __str__(self):
        return 'ap'