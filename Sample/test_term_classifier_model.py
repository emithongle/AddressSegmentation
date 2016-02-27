__author__ = 'Thong_Le'

from libs import segment as sg, store
from libs.config import *
from libs.features import extractFeatureText
import numpy as np

def test(feature_func, preprocessing_func):
    # 4. Test
    termList = store.loadTermData()

    print('=======================================================')
    print('=> Term Classifying...')
    # _time, templateList = sg.parseAddress(termList, feature_func, preprocessing_func)

    clf = store.loadClassifier()
    results = []

    for i in range(len(termList['X'])):
        X = np.asarray([extractFeatureText(feature_func, preprocessing_func, termList['X'][i])])
        results.append(clf.predict(X)[0].tolist() + clf.predict_proba(X)[0].tolist())

    titles = ['TestCase', 'Term', 'Label', 'Predicted Label', 'Name Score', 'Address Score', 'Phone Score']

    store.saveTermTestResults(titles, termList, results)



test(feature_func, preprocessing_func)