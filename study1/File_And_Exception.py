import requests

url = 'https://api.github.com/search/repositories?q=language:python&sorts=stars'
# r=requests.get(url)
# print("Status code: ",r.status_code)
# print(r.json())
# print((r.json()).keys())

# with open(r"e:\\qwer.txt") as file_object:
#     contents=file_object.read()
#     print(contents.strip())

# print(open(r'e:\\qwer.txt').read())


with open(r"e:\\qwer.txt") as file_object:
    txt = file_object.readlines()
    for line in file_object:
        print(line)

print(txt)

try:
    print("57" in '837675171')
except:
    pass
else:
    print("success")
finally:
    print("12")

print('37973283723'[:6])

with open("text.txt", "w") as file_object:
    # ori = file_object.readline()
    file_object.write(" facjiejifjgeageeeecfff")

# raise Exception("cuowu")
