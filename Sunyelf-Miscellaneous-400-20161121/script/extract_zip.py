#-*- coding:utf-8 -*-
#!/usr/bin/python
# extract_zip.py


ftm_file = open('USB flash disk.ftm', 'rb')
zip_file = open('flag.zip', 'wb')
read_pointer = 46495
offset = 132715
zip_data = ''

#循环读取56个大小为65526的包
for x in xrange(1, 57):
    ftm_file.seek(read_pointer)
    zip_data += ftm_file.read(65536)
    read_pointer += offset

#读取最后一个大小为61440的包
last_read_pointer = 7478535
ftm_file.seek(last_read_pointer)
zip_data += ftm_file.read(61440)

zip_data = zip_data[:-374]#除去尾部填充的无用字节

zip_file.write(zip_data)