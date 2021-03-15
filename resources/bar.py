from flask_restful import Resource

class Bar(Resource):
    def get(self):
        return {'Bar': 'Foo'}
    def post(self):
        pass