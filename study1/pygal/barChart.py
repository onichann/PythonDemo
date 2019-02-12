import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from collections import OrderedDict


def getdata():
    returnList = {}
    try:
        with open('python.json', mode='r') as txt_object:
            returnList = json.loads(txt_object.read())
    except:
        url = 'https://api.github.com/search/repositories?q=language:python&sorts=stars'
        response = requests.get(url)
        data = response.json()
        with open("python.json", 'w') as json_object:
            json_object.write(json.dumps(data))
        returnList = data
    finally:
        return returnList


def main():
    data = getdata()
    print(data)
    names, values = [], []
    for item in data['items'][:10]:
        names.append(item['name'])
        values.append({'value': item['stargazers_count'], 'label': item['description'], 'xlink': item['html_url']})
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False, title_font_size=24, label_font_size=24,
                      major_label_font_size=18, truncate_label=15, show_y_guides=False, width=1000)
    chart.title = 'yoyo 是个大笨蛋'
    chart.x_labels = names
    values.sort(key= lambda mysort:mysort['value'],reverse=True)
    chart.add('', values)
    chart.render_to_file('bar_chart.svg')
    # chart.render_to_png('bar_chart.png')


if __name__ == '__main__':
    main()
