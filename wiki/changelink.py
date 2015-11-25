#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: deleteline.py

import os
import sys

reload(sys) 
#sys.setdefaultencoding('utf8')

def ChangeLineInFile(infile,isOverwrite):
    isOverwrite = isOverwrite.upper()

    _dir = os.path.dirname(infile)
    oldbasename = os.path.basename(infile)
    newbasename = oldbasename + '-new'
    extname = os.path.splitext(infile)[1]
    if extname != ".md":
        return
    outfile = _dir+'/' + newbasename + extname
                
    infp = open(infile, "rb")
    outfp = open(outfile, "wb")
    lines = infp.readlines()
    title = None
    for line in lines:
        #print type(line)
        if (line.find("# ") > -1):
            line2 = line.replace("# ", "## ")
            outfp.writelines(line2)
        elif (line.find("## ") > -1):
            line2 = line.replace("## ", "### ")
            outfp.writelines(line2)
        elif (line.find("![](/assets/img/") > -1):
            line2 = line.replace("![](/assets/img/", "![](../assets/img/")
            outfp.writelines(line2)
        else:
            #print line
            outfp.writelines(line)
        
    infp.close()
    outfp.close()
    
    if isOverwrite == 'Y':
        #print 'remove',infile
        os.remove(infile)
        os.rename(outfile, infile)
        outfile = infile
    
    #print 'read %s'%infile, 'and save as %s'%outfile
    print 'read %s and save as %s'%(infile, outfile)

def DelLineInFile(infile,isOverwrite):
    isOverwrite = isOverwrite.upper()

    _dir = os.path.dirname(infile)
    oldbasename = os.path.basename(infile)
    newbasename = oldbasename + '-new'
    extname = os.path.splitext(infile)[1]
    if extname != ".md":
        return
    outfile = _dir+'/' + newbasename + extname
                
    infp = open(infile, "rb")
    outfp = open(outfile, "wb")
    lines = infp.readlines()
    title = None
    for line in lines:
        #print type(line)
        if (line.find("---") > -1):
            pass
        elif (line.find("layout:") > -1):
            pass
        elif line.find("title:") > -1:
            title = line.replace("title:","")
            print "title"+title
        elif line.find("{{ page.title }}") > -1:
            if title != None:
                line2 = line.replace("{{ page.title }}", title)
                outfp.writelines(line2)
        else:
            #print line
            outfp.writelines(line)
        
    infp.close()
    outfp.close()
    
    if isOverwrite == 'Y':
        #print 'remove',infile
        os.remove(infile)
        os.rename(outfile, infile)
        outfile = infile
    
    #print 'read %s'%infile, 'and save as %s'%outfile
    print 'read %s and save as %s'%(infile, outfile)
    
def ChangeLineInFolders():
    string = u'请输入目标文件夹路径====>'
    inpath = raw_input(string.encode('utf8'))
    string = u'您输入是：' + inpath
    print string
    
    string = u'是否覆盖源文件(Y/N)'
    isOverwrite = raw_input(string.encode('utf8'))
    isOverwrite = isOverwrite.upper()
    string = u'您的选择是：' + isOverwrite
    print string
        
    for (path,dirs,files) in os.walk(inpath):
        for f in files:            
            infile = os.path.join(path, f)
            #print infile
            ChangeLineInFile(infile,isOverwrite)
            
if __name__ == "__main__":
    string = u'1   修改指定目录下所有文.md件(包括子目录)'
    print string
    string = u'2   修改指定md文件 '
    print string    
    string = u'请输入数字编号====>'
    index = int(raw_input(string.encode('utf8')))

    if index == 1:
        ChangeLineInFolders()
    elif index ==2:
        string = u'请输入目标文件路径====>'
        infile = raw_input(string.encode('utf8'))
        string = u'您输入是：' + infile
        print string
        
        string = u'是否覆盖源文件(Y/N)'
        isOverwrite = raw_input(string.encode('utf8'))
        string = u'您的选择是：' + isOverwrite.upper()
        print string
                
        DelLineInFile(infile, isOverwrite)
    else:
        string = u'编号输入错误,程序退出'
        print string
        sys.exit()
        
    raw_input("press Enter to exit")
    sys.exit()
