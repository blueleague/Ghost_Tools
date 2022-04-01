# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:27:27 2022

@author: 王子阳
"""

import base64
import binascii
import zlib

#print (binascii.b2a_hex(base64.b64decode("eJyFVFl2xCAMu1K3Be7CD7QzZ+D4kRhChSCdD16igG1ZMkn1/pJqvGPFVMO74LdUy+cfDj/AeA58SzV/yPkMjKXng5yPeDLmxBm5Q7F4xQH7X6newCMyl3L5feTiHmtkcB95ERPRR9sDv6J7XhPncs/DekX4cy/g+8CvjzXxw7v2x29T/1L75DzFfxtG/R2XU8uhBfLudFk8QL0gnOhX7tossayv/NAr6w6MWOrp2nnusQ+d1ZeIWurF1XztPG39a1/QsqCe6jHxVux9EauvyDvxYh/a9853nZMnc988sNkd3I1LmxGsK9zOC178/EeH5b76/Lrf9j9Y5tf8Z6zq4PlavGI77/+X867udFp06/1NnmpvfdbabLEu4vX9coZdI9xX5prxAdaU2FA=")))

flag = base64.b64decode("eJyFVFl2xCAMu1K3Be7CD7QzZ+D4kRhChSCdD16igG1ZMkn1/pJqvGPFVMO74LdUy+cfDj/AeA58SzV/yPkMjKXng5yPeDLmxBm5Q7F4xQH7X6newCMyl3L5feTiHmtkcB95ERPRR9sDv6J7XhPncs/DekX4cy/g+8CvjzXxw7v2x29T/1L75DzFfxtG/R2XU8uhBfLudFk8QL0gnOhX7tossayv/NAr6w6MWOrp2nnusQ+d1ZeIWurF1XztPG39a1/QsqCe6jHxVux9EauvyDvxYh/a9853nZMnc988sNkd3I1LmxGsK9zOC178/EeH5b76/Lrf9j9Y5tf8Z6zq4PlavGI77/+X867udFp06/1NnmpvfdbabLEu4vX9coZdI9xX5prxAdaU2FA=")
# print(flag)
result = zlib.decompress(flag)
print (result)