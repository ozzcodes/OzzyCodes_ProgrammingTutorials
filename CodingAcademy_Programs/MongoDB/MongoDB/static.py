from bottle import route, run

@route('/hello/')
@route('/hello')
def hello():
    return "<h1>Hi to you too!<h1>"

@route('<mypath:path>')
def doSomething(mypath):
    print mypath
    return "Your URL is %s but it does not exist!" % mypath
 
run(host='localhost', port=1234, debug=True)
