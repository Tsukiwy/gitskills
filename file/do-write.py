# -*- coding: UTF-8 -*-
'''
在 write 内容后，直接 read 文件输出会为空，是因为指针已经在内容末尾。
两种解决方式: 其一，先 close 文件，open 后再读取，其二，可以设置指针回到文件最初后再 read
'''
import os;

document = open("testfile.txt", "w+");
print "文件名: ", document.name;
document.write("这是我创建的第一个测试文件！\nwelcome!");
print document.tell();
#输出当前指针位置
document.seek(os.SEEK_SET);
#设置指针回到文件最初
context = document.read();
print context;
document.close();