import keyword

print(keyword.kwlist)
print("hello,python")

if True:
    print("true")
else:
    print("false")

total = "efaf" \
        "fafea" \
        "faefa" \
        "a"

sk = 'feageageage' \
     'gafa' \
     'ga' \
     'ag'
print(total)

"""""ddd"""

str = 'Runoob'

print(str[1:])

# input("按下 enter 键后退出。")


a, b, c, d = 20, 5.5, True, 4 + 3j

print(type(a), type(b), type(c), type(d))

a = [1, 2, 3, 4, 5, 6, 1]
print(a.count(1))

print(4 // 3.0)

if 1 and 3:
    print(True)

print(complex(3, 4))

varc=5+6j

print(varc)

var1 = 'hello World!'

print("已更新字符串 : ", var1[:6] + 'Runoob!')

print(var1.capitalize())

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

'''左闭合右开'''

list1.append(3)

del list1[1]

print(list1.__len__(),end=",")
print(list1.__len__())

tuple1 = ('Google', 'Runoob', 'Taobao')

print(len(tuple1))

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(dict['Name']*2)

# var = 1
# while var == 1:  # 表达式永远为 true
#     num1 = input("输入一个数字  :")
#     print("你输入的数字是: ", num1)
#
# print("Good bye!")


n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %s 之和为: %s" % (n, sum))

# flag = 1
#
# while (flag): print('欢迎访问菜鸟教程!')
#
# print("Good bye!")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


list=[1,2,3,4]

it=list.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

