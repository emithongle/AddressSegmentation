__author__ = 'Thong_Le'

import numpy as np

from config import *
from libs.features import extractFeatureText, feature_names, preprocess
from libs import store


def exc():
    # 5. Test
    tmp = store.loadTermData()
    termList = {'X': [i[0] for i in tmp], 'y': [i[1] for i in tmp]}

    print('=======================================================')
    print('=> Term Classifying...')

    clf = store.loadClassifier()
    results = []

    for i in range(len(termList['X'])):
        preprocessd_term = preprocess(termList['X'][i])
        X = np.asarray([extractFeatureText(termList['X'][i])])
        results.append(clf.predict(X)[0].tolist() + clf.predict_proba(X)[0].tolist() +
                       ['', preprocessd_term] + X[0].tolist())

    titles = ['TestCase', 'Term', 'Label', 'Predicted Label', 'Name Score', 'Address Score', 'Phone Score', '', 'Preprocessed_Term'] + \
            feature_names

    tacc = sum([1 for (y1, y2) in zip(termList['y'], [result[0] for result in results]) if (y1 == y2)]) / len(termList['y'])

    store.saveTermTestResults(tacc, titles, termList, results, file=timeManage.getTime() + '_' + file_term_classify_result)

    return tacc