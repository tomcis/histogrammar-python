#Initializing server configurations

testgram='testgram.html'

def visualization(environ, start_response):
    vis_content = (open(testgram).read())
    start_response('200 OK', [('Content-Type','text-html')])
    return [vis_content]



#starts our wsgi server
if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        vis_port=8008
        vis_httpd = make_server('0.0.0.0', vis_port, visualization)
        print("Serving youre chart at http://localhost:"+str(vis_port)+"/"+testgram)
        vis_httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye!!')

