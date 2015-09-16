#-*- coding: utf-8 -*-
"""OCR in Python using the Tesseract engine from Google
http://code.google.com/p/pytesser/
by Michael J.T. O'Kelly
V 0.0.1, 3/10/07"""

import Image
import subprocess

import util
import errors
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

tesseract_exe_name = r'\pytes\tesseract' # Name of executable to be called at command line
scratch_image_name = "temp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "temp" # Leave out the .txt extension
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation

def call_tesseract(input_filename, output_filename):
    """Calls external tesseract.exe on input file (restrictions on types),
    outputting output_filename+'txt'"""
    args = [tesseract_exe_name, input_filename, output_filename]
    proc = subprocess.Popen(args)
    retcode = proc.wait()
    if retcode!=0:
        errors.check_for_errors()

def image_to_string(im, cleanup = cleanup_scratch_flag):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    try:
        util.image_to_scratch(im, scratch_image_name)
        call_tesseract(scratch_image_name, scratch_text_name_root)
        text = util.retrieve_text(scratch_text_name_root)
    finally:
        if cleanup:
            util.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text

def image_file_to_string(filename, cleanup = cleanup_scratch_flag, graceful_errors=True):
    """Applies tesseract to filename; or, if image is incompatible and graceful_errors=True,
    converts to compatible format and then applies tesseract.  Fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    try:
        try:
            call_tesseract(filename, scratch_text_name_root)
            text = util.retrieve_text(scratch_text_name_root)
        except errors.Tesser_General_Exception:
            if graceful_errors:
                im = Image.open(filename)
                text = image_to_string(im, cleanup)
            else:
                raise
    finally:
        if cleanup:
            util.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text

def binary(f):
    img = Image.open(f)
    #img = img.convert('1')
    #img = img.convert("RGBA")
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img

# 裁剪图片
def cutImg(im):
    ori_w, ori_h = im.size
    #这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
    box = (1, 1, ori_w-1, ori_h-1)
    newIm = im.crop(box) 
    return newIm

# 处理图片并保存
def processImg(filename):
    im = binary(filename)
    im.save('b_'+filename, 'jpeg')
    imAfterCut = cutImg(im)
    imAfterCut.save('AfterCut'+filename, 'jpeg')
    text = image_to_string(imAfterCut)
    return text

def getCode(img):
    print img
    # binary
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    ori_w, ori_h = img.size
    #这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
    box = (1, 1, ori_w-1, ori_h-1)
    newIm = img.crop(box)
    #newIm.save(r'D:\process.jpeg', 'jpeg')
    print img
    code = image_to_string(newIm)
    print img
    print "Code:", code
    return code

if __name__ == '__main__':
    text = processImg('code.jpg')
    print text
    # text = image_file_to_string('1.jpeg', graceful_errors=True)
    # print text
    text = processImg('2.jpeg')
    print text

    text = processImg('3.jpeg')
    print text

    text = processImg('4.jpeg')
    print text

    text = processImg('5.jpeg')
    print text
    text = image_file_to_string(r'D:/process.jpeg', graceful_errors=True)
    print text