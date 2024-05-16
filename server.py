from flask import Flask, request, abort
import util as util
import service as service

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Welcome to Diagnosis Codes API</h2>'


@app.route('/diagnosis-code', methods=['POST'])
def postDiagnosisCode():
    body = request.get_json()

    try:
        util.validatePostDiagnosisCodeRequest(body)
    except Exception as e:
        print(e)
        abort(400, e)

    try:
        service.postDiagnosisCode(body.get("diagnosisCode"), body.get("longDesc"))
    except Exception as e:
        print(e)
        abort(500, e)

    return ("success!")


if __name__ == "__main__":
    app.run(debug=True)