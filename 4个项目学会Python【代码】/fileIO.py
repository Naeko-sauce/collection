#文件读写三板斧
#1.打开文件
#文本读(r)  文本写(w)  二进制读(rb)  二进制写(wb)  追加写(a)
# with open('C:/Users/alw/Desktop/test.png', 'rb') as f:
#     data = f.read()
#     with open('C:/Users/alw/Desktop/test_backup.png', 'wb') as ff:
#         ff.write(data)


class File:
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.file.close()

    def write(self, data):
        self.file.write(data)


with File('hahah.txt') as file:
    file.write('shadyYYDS')

while True:
    pass