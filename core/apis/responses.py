from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))
    @classmethod
    def respond_error(cls, message, status_code):
        response = {
            "error": message
        }
        return make_response(jsonify(response), status_code)