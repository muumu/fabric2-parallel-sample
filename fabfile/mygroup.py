#-*- coding:utf-8 -*-
try:
    from invoke.vendor.six.moves.queue import Queue
except ImportError:
    from six.moves.queue import Queue

from invoke.util import ExceptionHandlingThread

from fabric.exceptions import GroupException
from fabric import Connection, ThreadingGroup, GroupResult
from getpass import getpass

def thread_worker_sudo(cxn, queue, args, kwargs):
    result = cxn.sudo(*args, **kwargs)
    queue.put((cxn, result))

class MyThreadingGroup(ThreadingGroup):
    def sudo(self, *args, **kwargs):
        if not hasattr(self, 'password'):
            self.password = getpass('Input sudo password: ')
        kwargs['password'] = self.password
        results = GroupResult()
        queue = Queue()
        threads = []
        for cxn in self:
            my_kwargs = dict(cxn=cxn, queue=queue, args=args, kwargs=kwargs)
            thread = ExceptionHandlingThread(
                target=thread_worker_sudo, kwargs=my_kwargs
            )
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        while not queue.empty():
            cxn, result = queue.get(block=False)
            results[cxn] = result
        excepted = False
        for thread in threads:
            wrapper = thread.exception()
            if wrapper is not None:
                cxn = wrapper.kwargs["kwargs"]["cxn"]
                results[cxn] = wrapper.value
                excepted = True
        if excepted:
            raise GroupException(results)
        return results

