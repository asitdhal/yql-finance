#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      asit
#
# Created:
# Copyright:   (c) asit
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2
import httplib
from Queue import Queue
from threading import Thread

class Fetch(object):

    def __init__(self, url, debug=False):
        self.response_data =''
        try:
            response = urllib2.urlopen(url)
            if  debug == True:
                print "Url : ", url
                print "Response : ", response
            self.response_data = response.read()
            response.close()
        except urllib2.URLError, e:
            print "URL Error >> ", str(e.reason)
        except urllib2.HTTPError, e:
            print "HTTP Error >> ", str(e.code)
        except httplib.HTTPException, e:
            print "HTTP Exception"
        except Exception:
            import traceback
            print traceback.format_exc()

    def Get(self):
        return self.response_data

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

def DoFetch(url, res_queue):
    ob = Fetch(url)
    res = ob.Get()
    res_queue.put([url, res])
    print url, " :: "#, res

def main():
    pool = ThreadPool(20)
    lis = [ 'http://www.google.com', 'http://www.yahoo.com', 'http://www.facebook.com', 'http://www.hotmail.com', 'http://www.tcs.com']
    res_queue = Queue()

    for i in lis:
        pool.add_task(DoFetch, i, res_queue)

    pool.wait_completion()

    while True:
        ele = res_queue.get()
        print ele[0], " :: ", ele[1][0:20]
        if ele is None:
            break




if __name__ == '__main__':
    main()