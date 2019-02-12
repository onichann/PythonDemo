import json

def retur():
    # raise RuntimeError("error")
    return True

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("Python 原始数据：", data.__str__())
print("JSON 对象：", json_str)

# with open('w.txt','w') as file_object:
#     json.dump(data,file_object)

import datetime

print(datetime.datetime.now())

import unittest

class MyTest(unittest.TestCase):
    def test_te(self):
        res=retur()
        self.assertTrue(res,True)

unittest.main()


import  pygal
import matplotlib
