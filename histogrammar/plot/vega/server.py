#Initializing server configurations

def app(environ, start_response):
    content = (open('testgram/testgram.html').read())
    start_response('200 OK', [('Contetn-Type','text-html')])
    return [content]


#starts our wsgi server
if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('0.0.0.0', 8080, app)
        print("Serving at http://localhost:8080/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye!!')




