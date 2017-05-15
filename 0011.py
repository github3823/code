#https://github.com/Yixiaohan/show-me-the-code
'''第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge'''
# coding:utf-8
i=['北京','程序员','公务员','领导','牛比','牛逼','你娘','你妈','love','sex','jiangge']#
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
