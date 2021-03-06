from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Incidents(Resource):
    def get(self):
        return 'Here be incidents, man'

class Incident(Resource):
    def get(self, inc_no):
        return f'Here is the one and only incident: {inc_no}'

api.add_resource(Incidents, '/api/incident') # Route_1
api.add_resource(Incident, '/api/incident/<inc_no>') # Route_2


if __name__ == '__main__':
     app.run(port='4242')

# http://127.0.0.1:4242/api/incident/42 should work boiw
