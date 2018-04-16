import tornado.ioloop
import tornado.web
import os
lsys = os.environ.get('jenkins_sys', 'unknown')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h2>Hello world -- " + lsys + "</h1>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
