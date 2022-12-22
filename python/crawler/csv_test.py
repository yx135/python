import csv

r_list=[('我不是药神','徐峥,周一围,王传君','2018-07-05')]

with open('D:\\data\\python\\crawler\\csvtest.csv','a',newline='',encoding="utf-8") as f:
            #生成csv操作对象
            fieldnames = ['title', 'time','other']

            writers = csv.DictWriter(f,fieldnames=fieldnames)
            writers.writeheader()
            writer = csv.writer(f)
            #整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                # 上映时间：2018-07-05
                # 切片截取时间
                time = r[2].strip()[5:15]
                L = [name,star,time]
                # 写入csv文件
                writer.writerow(L)
                print(name,time,star)
            