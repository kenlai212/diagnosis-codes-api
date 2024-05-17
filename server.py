from flask import Flask, request, abort
import util
import service
import db
import json

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

@app.route('/semantic-search', methods=['POST'])
def semanticSearch():
    body = request.get_json()

    try:
        util.validateSemanticSearchRequest(body)
    except Exception as e:
        print(e)
        abort(400, e)

    try:
        searchVector = util.getBioSentVectorEmbedding(body.get("sentence"))
    except Exception as e:
        print(e)
        abort(500, e)

    try:
        result = db.searchSimilar(searchVector)
    except Exception as e:
        print(e)
        abort(500, e)

    output = []
    for i in result:
        output.append(i)

    outputObj = {"output":output}
    print(outputObj)
    return (outputObj)

if __name__ == "__main__":
    app.run(debug=True)