#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def run():
    tmpStr_Unicode=input("Input Unicode:").replace('\r','').replace('\n','')
    tmpStr_Normal=tmpStr_Unicode.decode('unicode_escape').encode('gb2312')
    print(tmpStr_Normal)

if __name__=="__main__":
    run()