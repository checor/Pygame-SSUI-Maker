#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2014 Sergio I. Urbina <checor@gmail.com>
#  
  
import threading, os, time

import screen
import config
import glob

def main():
    
    scr = screen.Screen()
    scr_t = threading.Thread(target=scr.run, args=('test.xml',))
    scr_t.start()
    
    #Test
    glob.set_variable('venta', 0)
    while True:
        time.sleep(.001)
        glob.var_sum('venta', .01)
        if glob.get_variable('venta') >= 30:
            break
    return 0

if __name__ == '__main__':
    main()
