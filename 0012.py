#https://github.com/Yixiaohan/show-me-the-code
'''第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'''
# coding:utf-8
i=['北京','程序员','公务员','领导','牛比','牛逼','你娘','你妈','love','sex','jiangge']#脏字库
b='北京程序员人公务员不是人呀牛，了比，牛逼，你妈，你大娘，lovesexjiangge'

def bb(b):
 y=''
 for st in i:
    if st in b:
        d = ''
        t=len(st)
        while t>0:
            d=d+'*'
            t=t-1
        y=b.replace(st,d)
 if y=='':
     return b
 else:
     return bb(y)

print(bb(b))
