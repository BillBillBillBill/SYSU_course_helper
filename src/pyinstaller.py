#! /usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Main command-line interface to PyInstaller.
"""
# from  PyInstaller import  *
import  os

if __name__ == '__main__':
    from PyInstaller.main import run
    opts=['course_helper.py','-F','-w','--icon=D:\Python\pyqtfile\course_helper\logo.ico']
    run(opts)