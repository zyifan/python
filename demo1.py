# 打印
print ("Hello, Python!");

'''
1、 python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 
'''

if True:
    print ("True")
else:
    print ("False")

"""
2、多行语句:
    使用反斜杠(\)来实现多行语句,在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)

    如：
    total = item_one + \
        item_two + \
        item_three
"""
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

'''
3、数据类型
    python中数有四种类型：整数、长整数、浮点数和复数。

    int (整数), 如 1
    long (长整数) , 比较大的整数
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

'''
4、字符串
    python中单引号和双引号使用完全相同。
    使用三引号(\'''或""")可以指定一个多行字符串。
    转义符 '\'
    自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
    字符串是不可变的。
    按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
'''
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

print(word)

'''
5、等待用户输入
    执行下面的程序在按回车键后就会等待用户输入：
'''
input("\n\n按下 enter 键后退出。")

'''
6、同一行显示多条语句
    Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

'''
7、多个语句构成代码组
    缩进相同的一组语句构成一个代码块，我们称之代码组。

    像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

    我们将首行及后面的代码组称为一个子句(clause)。
'''
if 1+1==2 : 
   print('2')
elif 1+1>2 : 
   print('>2')
else : 
   print('<2')


'''
8、Print 输出
    print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''
x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()

'''
9、import 与 from...import
    在 python 用 import 或者 from...import 来导入相应的模块。

    将整个模块(somemodule)导入，格式为： import somemodule

    从某个模块中导入某个函数,格式为： from somemodule import somefunction

    从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

    将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

'''
    python -h
'''