from bottle import route, post, run, get, template, request,response,static_file
import func
import time

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='.')

@route('/')
def index():
    iss = func.get_iss()
    func.get_mappic(iss[0],iss[1])
    # res = func.get_loc(request.query['place'])
    # print(">>>",response.charset,request.query['place'],res,"<<<")
    # print(res['geocodes'][0]['city'],res['geocodes'][0]['location'])
    with open("index.html") as f:
        return template(f.read(), lat=iss[0],lon=iss[1],info_time=iss[2],query_time=time.asctime(time.localtime(time.time())))



@post('/') # or @route('/login', method='POST')
def do_login(name="user", info=''):
    username = request.forms.get('username')
    password = request.forms.get('password')
    if True:
        print(username,password)
        info = "Your login information was correct."
        return index(name, info)
    else:
        return "<p>Login failed.</p>"
        
        

run(host="0.0.0.0",port=9000)
