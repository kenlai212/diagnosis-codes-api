import requests

def validatePostDiagnosisCodeRequest(body):
    if body.get("diagnosisCode") is None:
        raise Exception("diagnosisCode is mandatory")
    
    if body.get("longDesc") is None:
        raise Exception("longDesc is mandatory")
    

def getBioSentVectorEmbedding(sentence):
    #apiUrl = "http://20.2.64.152/sentence/vector-embedding"
    #body = {"sentence": sentence}
    #response = requests.post(apiUrl, json=body)
    #return response.json()
    response_obj = {"sentence":sentence, "prppedSengence":sentence, "vector":[0.001, 0.002, 0.003]}
    
    return (response_obj.get("vector"))