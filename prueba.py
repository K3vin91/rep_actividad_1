# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:19:21 2021

@author: KEVIN
"""

import os

cwd = os.getcwd()

def convert(cwd):
    
    os.system('teqc -O.dec 30 +obs CRNO20201201.o CRNO20201201_000000.AS')

convert(cwd)