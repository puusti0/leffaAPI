from flask import Flask
from flask_restful import Api
from leffaAPI.resources.foo import Foo
from leffaAPI.resources.bar import Bar
from leffaAPI.resources.hello import Hello

app = Flask(__name__)
api = Api(app)

#Testailua
api.add_resource(Hello, '/')
api.add_resource(Foo, '/foo')
api.add_resource(Bar, '/bar')

if __name__ == '__main__':
    app.run(debug=True)