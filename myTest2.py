import requests


# url='http://17.16.8.74:8999/file/11.pdf'
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
# }
# resp=requests.get(url)
# with open('a.pdf','wb') as file_object:
#     file_object.write(resp.content)



if __name__ == '__main__':
    values = ','.join(['%s'] * 5)
    print(values)

    print(3 if False else 4)
