import util as util
import db as db

def postDiagnosisCode(diagnosisCode, longDesc):
    vector = util.getBioSentVectorEmbedding(longDesc)
    record = {"diagnosisCode": diagnosisCode, "longDesc": longDesc, "embedding":vector}
    db.saveCode(record)