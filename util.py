import requests
import json

def validatePostDiagnosisCodeRequest(body):
    if body.get("diagnosisCode") is None:
        raise Exception("diagnosisCode is mandatory")
    
    if body.get("longDesc") is None:
        raise Exception("longDesc is mandatory")
    

def getBioSentVectorEmbedding(sentence):
    #'''
    host = "http://20.6.154.196"
    url = host + "/sentence/vector-embedding"
    body = {"sentence": sentence}
    response = requests.post(url, json=body)
    response_obj = json.loads(response.text)
    #'''
    
    #response_obj = {"sentence":sentence, "prppedSengence":sentence, "vector":[0.001, 0.002, 0.003]}

    return (response_obj.get("vector"))

def validateSemanticSearchRequest(body):
    if body.get("sentence") is None:
        raise Exception("sentence is mandatory")