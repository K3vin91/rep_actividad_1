# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:16:12 2021

@author: KEVIN
"""

import os


arch_cru = []

cwd = os.getcwd()

ext = '.AS'

def listar(cwd):
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if os.path.splitext(file)[1] == ext:
                arch_cru.append(file)
                #print(file)
             
listar(cwd)

def convert(arch_cru):
    for file in arch_cru:
        new_name = file.split('.')[0] + '.o'
        print(new_name)
        type(file)
        os.system('teqc -O.dec 30 +obs' + new_name + file)    

convert(arch_cru)    