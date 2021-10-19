import requests
from PIL import Image
from io import BytesIO

# import matplotlib.pyplot as plt

amap_key = '04f9a0fac9572ad6709b2d89b90990f3'
nasa_key = 'SexHZwo6Wk3pqH6vHLLcGWmioGeCWoxXQzM54ELy'
r_parameters = {
    'key':amap_key,
    'location':"123,70",
}
URL = 'https://restapi.amap.com/v3/geocode/geo'
r_URL = 'https://restapi.amap.com/v3/geocode/regeo'

import datetime


from sscws.sscws import SscWs
import datetime

def get_iss():
    ssc = SscWs()

    #  Edit the following time variable to suit your needs.
    time = ['2021-11-07T23:00:00.000Z', '2021-11-08T00:00:00.000Z']
    time = [(datetime.datetime.now() - datetime.timedelta(hours = 1)).isoformat(), datetime.datetime.now().isoformat()]

    result = ssc.get_locations(['iss'], time)

    data = result['Data'][0]
    coords = data['Coordinates'][0]
    iss_lat = coords['Latitude'][0]
    iss_lon = coords['Longitude'][0]
    iss_time = coords['LocalTime'][0]
    print(coords['Latitude'][0],coords['Longitude'][0],coords['LocalTime'][0])
    
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

def get_mappic(lat,lon):
    URL = 'https://restapi.amap.com/v3/staticmap'
    parameters = {
        'location':str(lat)+','+str(lon),
        'marker':str(lat)+','+str(lon),
        'zoom':2,
        'key':amap_key,
    }
    res = requests.get(URL, parameters)
    print(res.request.url)
    
    with open('p.png','wb') as p:
        p.write(res.content)
    # i = Image.open(BytesIO(res.content))
    # plt.imshow(i)


def get_pic(lat,lon):
    URL = 'https://api.nasa.gov/planetary/earth/imagery'
    parameters = {
        'api_key':nasa_key,
        'lat':lat,
        'lon':lon,
    }
    res = requests.get(URL, parameters)
    
    print(res.content)
    return res.json()


if __name__ == "__main__":
    name = '天安门'
    res = get_loc()
    # print(res)
    loc = res['geocodes'][0]['location']
    assert(res['geocodes'][0]['city'] == "武汉市")
    print(name + " is at " + loc)
    # get_pic(loc[0],loc[1])
    
    iss = get_iss()
    print(get_mappic(iss[0],iss[1]))
    