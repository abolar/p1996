import tornado.ioloop
import tornado.web
import os
jenkins_sys = os.environ['jenkins_sys']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World! - from " + jenkins_sys)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
