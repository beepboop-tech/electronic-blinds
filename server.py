from flask            import Flask, g
from flask_restful    import Api, Resource, reqparse, abort
import motor_control

app  = Flask(__name__)
api  = Api(app)

blinds_are_up = True

class Blinds(Resource):
    def get(self):
        global blinds_are_up
        return {'blinds_are_up': str(blinds_are_up)}, 200

class BlindsUp(Resource):
    def post(self):
        global blinds_are_up

        if (blinds_are_up):
            return {'success': 'Blinds already raised'}, 200

        motor_control.blinds_up()
        blinds_are_up = True
        return {'success': 'Blinds raised'}, 200

class BlindsDown(Resource):
    def post(self):
        global blinds_are_up

        if (not blinds_are_up):
            return {'success': 'Blinds already lowered'}, 200

        motor_control.blinds_down()
        blinds_are_up = False
        return {'success': 'Blinds lowered'}, 200

api.add_resource(BlindsUp, '/blinds/up', endpoint='up')
api.add_resource(BlindsDown, '/blinds/down', endpoint='down')
api.add_resource(Blinds, '/blinds', endpoint='blinds')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
