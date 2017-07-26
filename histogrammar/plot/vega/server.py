#Initializing server configurations

thefile='testgram/testgram.html'
def app(environ, start_response):
    content = (open(thefile).read())
    start_response('200 OK', [('Content-Type','text-html')])
    return [content]


#starts our wsgi server
if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        port=8888
        httpd = make_server('0.0.0.0', port, app)
        print("Serving at http://localhost:"+str(port)+"/"+thefile)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye!!')
