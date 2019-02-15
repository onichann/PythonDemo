from csv import writer, DictWriter

with open('data.csv', 'w') as csvfile:
    # delimiter 分割符
    wr = writer(csvfile, delimiter=' ')
    wr.writerow(['id', 'name', 'age'])
    wr.writerow(['1001', 'mike', '20'])
    wr.writerow(['1002', 'bob', '55'])
    wr.writerow(['1003', 'jrd', '21'])
    wr.writerows([['1004', 'jrd', '21'], ['1005', 'jrd', '21']])

with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldNames = ['id', 'name', 'age']
    wr = DictWriter(csvfile, delimiter=' ', fieldnames=fieldNames)
    wr.writerow({'id': '1006', 'name': '小米', 'age': '33'})
