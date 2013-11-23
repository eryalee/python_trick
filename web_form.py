#!/usr/bin/env python

# hook log GET POST
import web
from mylog import Log

#web.config.debug = False
render = web.template.render('templates/')
urls = (
    '/', 'index',
    '/origin', 'origin'
    #'/(.*)/', 'redirect',
)
import sys
print sys.getdefaultencoding()
class index:
    def GET(self):
        input_ = web.input(name = None, age = 0)
        print input_
        if input_.name != None:
            return render.name(input_.name)
        elif input_.age != 0:
            return render.age(input_.age)
        else:
            return "Default: Hello world!"

class origin:
    def GET(self):
        return render.origin()
    def POST(self):
        #input_ = web.data()
        input_ = web.input()
        #print web.ctx
        return render.origin()

class redirect:
    def GET(self, path):
        print "302 redirect path:", path
        web.seeother('/' + path)

def my_loadhook():
    print "load hook...."
    print "from load hook", web.input()
def my_unloadhook():
    print "unload hook...."

if __name__ == '__main__':
    #load web urls
    app = web.application(urls, globals())
    #add hooks
    app.add_processor(web.loadhook(my_loadhook))
    app.add_processor(web.unloadhook(my_unloadhook))
    #run as log
    #app.run(Log)
    #run as console
    app.run()
