__author__ = 'Thong_Le'

from libs import store
from config import bpreprocessing
from libs.features import dataPreprocess, feature_names

def exc():
    # 1. Read txt data
    tupleData = store.loadTxtData()

    # 2. Preprocessing
    preprocessedData = tupleData
    if (bpreprocessing):
        preprocessedData = dataPreprocess(tupleData)
    store.savePreprocessedDataCSV(preprocessedData, feature_names)