import os
import binascii
import struct

#必须修改图片的实际位置，及图片实际CRC
crcbp = open("bronya.png", "rb").read()    #打开图片，图片的实际位置
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + \
            struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        ###图片当前CRC，根据图片实际修改
        if(crc32 == 0x5DEB74BB):    ###图片当前CRC，根据图片实际修改
            print(i, j)
            print('hex:', hex(i), hex(j))

