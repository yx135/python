'''Solution by: anas1434 
'''
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
import zlib
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))