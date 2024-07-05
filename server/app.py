from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):

    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)


# after making a request in the browser we an see something like;
# -{
#   "cookies": [
#     {
#       "mouse": "Cookie"
#     },
#     {
#       "session": "eyJnb29kbmlnaHQiOiJNb29uIiwiaGVsbG8iOiJXb3JsZCJ9.Y3KXKQ.oTqGI6rmhKDNLizZaHfJadRybUc"
#     }
#   ],
#   "session": {
#     "session_accessed": true,
#     "session_key": "hello",
#     "session_value": "World"
#   }
# }
    