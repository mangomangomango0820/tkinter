# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/11/12 4:18 PM
# File      : b.py
# Tool      : PyCharm
# Purpose   : example 2, b.py

import threading
import time


class logic:
    def __init__(self, flag, input, output):
        self.flag = flag
        self.input = input
        self.output = output

    def main(self, x):
        '''
        block calling until timeout occurs or internal flag is set to True
        :return:
        '''
        while True:
            self.flag.wait()
            y = int(self.input)+int(x)
            self.output.insert(1.0, threading.current_thread().name + ': ' + str(y) + '\n')
            time.sleep(1)
            x += 1

    def stop(self):
        '''
        reset internal flag to False -> threading block calling wait()
        :return:
        '''
        self.flag.clear()
        self.output.insert(1.0, f'stopped? {threading.current_thread().is_alive()}' + '\n')          #

    def conti(self):
        '''
        set internal flag to True -> calling wait()
        :return:
        '''
        self.flag.set()
        self.output.insert(1.0, f'continued? {threading.current_thread().is_alive()}' + '\n')

    def event(self):
        '''main所调用的方法'''
        x = 1
        self.main(x)