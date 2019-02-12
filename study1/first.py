for val in range(1, 5):
    print(val)

print(list(range(7)))

squarts = []
for value in range(1, 10):
    squarts.append(value ** 2)
print(squarts)

print(sum(squarts))

print([value ** 2 for value in range(10)])

foots = squarts.copy()
print(foots)
print(foots[:])

cars = ['audi', 'bmw', 'subaru', 'toyota']
print("我们")

for car in cars:
    if (car == "bmw"):
        print(car.upper())
    else:
        print(car.title())

t = '1'

if t == '1':
    print(1)

print(cars.__contains__('audi'))

try:
    print('audi' in cars)
except:
    print("s")
finally:
    print("s")
print()

k = False
if not k:
    print("qd")

print(cars.__len__() > 0)
print(len(cars))

# for it in iter(cars):
#     print(it, end="")
# pass

dicts = {"color": "red"}
print(type(dicts["color"]))
print(dicts)
dicts['name'] = "xiaogang"
print(dicts)
# del dicts['color']
# print(dicts)

print("sjifejaoigjoa;jgi" +
      ""
      ""
      "eajfieaj"
      "igj")

for keys,value in dicts.items():
    print(keys)
    print(value)
    print(type(keys))

print("--------------")
for item in dicts.values():
    print(item)

print("------------")

for item2 in iter(dicts):
    print(item2)

print('color' in dicts.keys())

lists = [{'name': 'a', "age": 1}, {'name': 'a1', "age": 11}]
print([value for value in lists].__str__())
print(type([value for value in lists].__str__()))
for val in lists:
    print(val)


# message=input("请输入....")
# if(message=="1"):
#     print("yes")
# else:
#     print(message)

# message=""
# while message!="quit":
#     message=input("输入：")
#     if message=="quit":
#         break
#     print(message)
#
#
# while True:
#     print("s")

input("what's name?")
input("age?")