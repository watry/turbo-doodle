import urllib
import urllib.request
import urllib.parse
import json
import importlib,sys
importlib.reload(sys)
import requests


class SendUrl(object):

    def send_url(self, url, headers, data=None):
        opener = urllib.request.build_opener()
        request = urllib.request.Request(url, data=data, headers=headers)
        response = opener.open(request, timeout=10)
        js = json.loads(response.read().decode("utf-8"))
        print('位置：'+ js['content']['address_detail']['province'] + js['content']['address_detail']['city'])
        print('纬度：'+ js['content']['point']['y'])
        print('经度：'+ js['content']['point']['x'])
        return js['content']['address']

def Main(ipaddr):
    # ak 需自行注册
    ak = "Dx9tIbr9zsoDOs2ApS23softSrBcNYBf"
    sx = SendUrl()

    url = "https://api.map.baidu.com/location/ip"
    data = {"ip": ipaddr, "ak": ak, "coor": "bd09ll"}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    city = sx.send_url(url, headers, data=urllib.parse.urlencode(data).encode("utf-8"))
    city = city[3:]
    city_code_dict = {
        '北京市': '101010100', '上海市': '101020100',
        '天津市': '101030100', '重庆市': '101040100',
        '武汉市': '101200101'
    }
    url1 = 'http://www.weather.com.cn/data/sk/' + city_code_dict[city] + '.html'
    r = requests.get(url1)
    r.encoding = 'utf-8'
    print(r.json()['weatherinfo']['temp'] + '℃')
    print(r.json()['weatherinfo']['WD'])


if __name__ == '__main__':
    # 27.18.198.204
    ipaddr = input('请输入一个ip地址:')
    Main(ipaddr)