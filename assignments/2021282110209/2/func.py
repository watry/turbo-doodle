import requests
from sscws.sscws import SscWs
import datetime
import keys

amap_key = keys.get_amap_key()
nasa_key = keys.get_nasa_key()

URL = 'https://restapi.amap.com/v3/geocode/geo'


def get_iss():
    ssc = SscWs()

    #  Edit the following time variable to suit your needs.
    # time = ['2021-11-07T23:00:00.000Z', '2021-11-08T00:00:00.000Z']
    time = [(datetime.datetime.now() - datetime.timedelta(hours = 1)).isoformat(), datetime.datetime.now().isoformat()]

    result = ssc.get_locations(['iss'], time)
    data = result['Data'][0]
    
    coords = data['Coordinates'][0]
    iss_lat = round(coords['Latitude'][0],2)
    iss_lon = round(coords['Longitude'][0],2)
    iss_time = coords['LocalTime'][0]
    
    print("ISS is at ",iss_lat, iss_lon, iss_time)
    return [iss_lat, iss_lon, iss_time]


def get_loc(name="水果湖"):
    URL = 'https://restapi.amap.com/v3/geocode/geo'
    parameters = {
        'key':amap_key,
        'address':name,
        'output':'json',
    }
    res = requests.get(URL, parameters)
    return res.json()

def get_mappic(lat=40,lon=40):
    URL = 'https://restapi.amap.com/v3/staticmap'
    parameters = {
        'location':str(lon)+','+str(lat),
        'markers':"mid,0xFFA500,I:"+str(lon)+','+str(lat),
        'zoom':2,
        'key':amap_key,
    }
    res = requests.get(URL, parameters)
    print(res.request.url)
    
    with open('p.png','wb') as p:
        p.write(res.content)


if __name__ == "__main__":
    # 测试
    name = '汉口'
    res = get_loc(name)
    loc = res['geocodes'][0]['location']
    print(res['geocodes'][0]['city'] )
    assert(res['geocodes'][0]['city'] == "武汉市")
    print(name + " is at " + loc)
    
    iss = get_iss()
    get_mappic(iss[0],iss[1])
    