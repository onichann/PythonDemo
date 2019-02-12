from functools import reduce
import json
import study1.dog1
from study1.dog1 import dog as imdog
from collections import OrderedDict
from encodings import utf_8

import doctest

print(imdog().name)

def say(mes="s"):
    """this is say method"""
    print(mes)


say("hello world".title())
say()

# 关键字实参
say(mes="ddd")

print(list(set([1,2,3]+[2,3,4])))

# json.dumps()

a=None

print(study1.dog1.dog().getDog())


class Mydog(study1.dog1.dog):
    def __init__(self):
        super().__init__()
        self.age="12"

    def getDog(self):
        return self.name+","+self.age

    def getDog1(self,*location):
        return self.name+","+self.age+"|".join(location.__str__())

print(Mydog().getDog1(2,231,212,12))

dict=OrderedDict()

print(utf_8.encode("我们"))

doctest.testmod()