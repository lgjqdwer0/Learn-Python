# 1.制表符，水平制表符\t，换行符\n的运用
print("Tartaglia, I love you!")
print("\tTartaglia,\tI\tlove\tyou!")
print("\nTartaglia,\nI\nlove\nyou!")

# 2.删除空白
b = ' How are you? '
print(b.rstrip()) #去掉后面
print(b.lstrip()) #去掉前面
print(b.strip()) #去掉两端

# 3.认识函数str()，数字不能单独输入，要作为数值或字符串
h = 21
message = "Happy "+str(h)+"rd Birthday!"
print(message)
j = "21"
message_1 = "Happy "+j+"rd Birthday!"
print(message_1)
print( )

# 4.列表：是由各种不同元素排列组成的。索引从0开始，-1表示最后一个
I = ['旅行者','荧','与鹤','老婆']
you = '散兵'
love = ['忠于','信任','理解','支持']
print(love[0])
print(love[-3])
message_2 = I[2]+love[2]+'和'+love[3]+you+'~'
print(message_2)

# 综合练习~
name = ['雷电国崩','倾奇者',you,'流浪者']
names = name[0]+' '+name[1]+' '+name[2]+' '+name[3]
print( )
v = '你!'
n =['♥','♡','💋','😘']
m = ',你知道吗？'
print(n[1]+name[0]+m+I[0]+love[0]+v+n[1])
print(n[0]+name[1]+m+I[1]+love[1]+v+n[0])
print(n[1]+name[2]+m+I[2]+love[2]+v+n[1])
print(n[0]+name[3]+m+I[3]+love[3]+v+n[0]+'\n')

# 5.运用append()在原列表和空白列表后面添加元素
name.append('风散')
print(names)
gao = []
gao.append('魈')
gao.append('达达利亚')
gao.append('散兵')
print(gao)
# 运用insert()来添加任何位置的新元素
ao = ['少女','仆人','富人','木偶']
print(ao)
ao.insert(4,'公子')
print(ao)
# 6.运用del来删除任何位置的元素
del ao[3]
print(ao)

# 7.运用pop()弹出末尾的元素,前提是知道位置（跟丢到回收站一样，不会被彻底删除，而是转移）
poped = ao.pop()
print(ao)
print(poped)
# 前提知道元素的值，再进行列表弹出（删除），删除后可以在其他地方使用
e = '富人'
w = ao.remove(e)
print(e+'，真像白术啊！')
print(ao)

# 综合练习2
clip = ['nahida','Scaramouche','fugitive']
last_clip = clip.pop()
print('Next editing of '+last_clip.title()+'!')
print(clip)
print( )

# 思考：Python之禅
import this

# 今天终于解决字幕内容问题了！昨天才发现他们的英文字幕全是大写，不仅大小位置灵活，而且都是跟着画面一起动的，难怪代入感强，给我们这些人看视频带来了不一样的体验！我也要朝着这个方向好好努力！做好散宝的混剪视频！
