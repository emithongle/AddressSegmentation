__author__ = 'Thong_Le'

from libs import store
from libs.features import extractFeature, feature_names

def exc():
    preprocessedData = store.loadPreprocessedDataCSV()

    # 3. Extract features
    featureTuples = extractFeature(preprocessedData)
    store.saveFeatureCSV(featureTuples, feature_names)