import itertools

ids=[1,4,3,3,4,2,3,3,5,6,1]
ids.sort()
it=itertools.groupby(ids)
for k,v in it:
    print(k,v)