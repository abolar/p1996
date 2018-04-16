import tornado.ioloop
import tornado.web
import os
jenkins_sys = os.environ.get('jenkins_sys', 'unknown')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>This is python saying hi from " + jenkins_sys + "</h1>")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
