from flask import session, jsonify


def authentication_required(f):
    def decorator(*args, **kwargs):
        if 'username' not in session:
            return jsonify(message='Must be authenticated'), 401
        return f(*args, **kwargs)
    return decorator
