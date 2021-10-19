from bottle import route, post, run, get, template, request,response
import test



@route('/')
def index(name='user', info=''):
    res = test.get_loc(request.query['place'])
    print(">>>",response.charset,request.query['place'],res,"<<<")
    print(res['geocodes'][0]['city'],res['geocodes'][0]['location'])
    with open("index.html") as f:
        return template(f.read(), name=name, info=info)



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
        
        

run(host='localhost', port=9000)
