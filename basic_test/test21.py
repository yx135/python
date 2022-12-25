import math
class robot():
    x,y=0,0
    def left_right(self,dir,num):
        if dir=='LEFT':
            self.x=self.x-int(num)
        elif dir=='RIGHT':
            self.x=self.x+int(num)
        return self.x
    def up_down(self,dir,num):
        if dir=='UP':
            self.y=self.y+int(num)
        elif dir=='DOWN':
            self.y=self.y-int(num)
        return self.y
    def run(self,dirs,nums):
        dir=dirs
        num=nums
        if dir=='LEFT' or dir=='RIGHT':
            self.left_right(dirs,nums)
        if dir=='UP' or dir=='DOWN':
            self.up_down(dirs,nums)

roobt=robot()
while True:
    a=input().split()
    if len(a)==0:
        break
    print(a)
    print(len(a))
    roobt.run(dirs=a[0],nums=a[1])
    print(roobt.x,roobt.y)
print(roobt.x,roobt.y)
dist=round(math.sqrt(int(roobt.x)**2+int(roobt.y)**2))
print(dist)