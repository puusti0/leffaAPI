from flask_restful import Resource

class Foo(Resource):
    def get(self):
        return {'Foo': 'Bar'}
    def post(self):
        pass