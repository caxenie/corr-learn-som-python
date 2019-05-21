#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:13:24 2019

@author: amie
"""

import threading
import time
import function as fun_c

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.F = fun_c.Func()
        
    def run(self):
        print ("start a new thread： " )
        # 获取锁，用于线程同步
        threadLock = threading.Lock()
        threadLock.acquire()
        self.F.main_thread(train=True)
        # 释放锁，开启下一个线程
        threadLock.release()





