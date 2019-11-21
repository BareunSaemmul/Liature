from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


INFOS = {
    'weather': {},
    'shelter': {},
    'disaster': {}
}


def abort_if_info_doesnt_exist(info_id):
    if info_id not in INFOS:
        abort(404, message=f"Info {info_id} doesn't exist")


parser = reqparse.RequestParser()
parser.add_argument('task')


class Info(Resource):
    def get(self, info_id):
        abort_if_info_doesnt_exist(info_id)
        return INFOS(info_id)


class InfoList(Resource):
    def get(self):
        return INFOS

    def post(self):
        args = parser.parse_args()
        info_id = 'info'
        return INFOS[info_id], 201


api.add_resource(InfoList, '/infos/')
api.add_resource(Info, '/infos/<string:info_id')

if __name__ == '__main__':
    app.run(debug=True)
