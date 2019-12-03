import xlrd
import numpy as np
from CountingSort import count
class excel_read:
    def __init__(self, excel_path=r'D:\研一资料\\选课名单.xls', encoding='utf-8', index=0):
        self.data = xlrd.open_workbook(excel_path)  ##获取文本对象
        self.table = self.data.sheets()[index]  ###根据index获取某个sheet
        self.rows = self.table.nrows  ##3获取当前sheet页面的总行数,把每一行数据作为list放到 list

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)  ##获取每一列数据
            #           print(col)
            result.append(col)
        #       print(result)
        return result
A = []
if __name__ == '__main__':
    A = excel_read().get_data()
data1 = np.array(A)
B = data1[:, 4]
C = B.tolist()
C.pop(0)
C.pop(len(C) - 1)
results = list(map(int, C))#通过A，B,C将Excel中的电话号码以list形式存至results

D = []
for i in range(len(results)):
    D.append(0)#初始化D，D用来存放每个位

for i in range(11):
    for j in range(len(results)):
        D[j] = results[j] // (10 ** i) % 10
    D=count(D)

    for k in range(len(D)):
        for m in range(k, len(D)):
            if D[k] == results[m] // (10 ** i) % 10:
                a = m
                while a > k:
                    results[a], results[a - 1] = results[a - 1], results[a]
                    a -= 1
                break

print(results)
