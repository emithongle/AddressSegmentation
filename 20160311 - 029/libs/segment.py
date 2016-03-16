__author__ = 'Thong_Le'

import time
import copy
from math import log
import numpy as np

from libs import store
import libs.features as fe

nterm = 3

def parseAddress(textList, file_model=None):
    if (file_model):
        clf_model = store.loadClassifier(file=file_model)
    else:
        clf_model = store.loadClassifier()
    _time = []
    templateList = []

    print('=======================================================')
    print('=> Address Parsing...')
    for (i, text) in zip(range(len(textList)), textList):
        print('==> Parsing text ' + str(i) + '...')
        millis_S = int(round(time.time() * 1000))
        ptemplates = templateSegment(text, nterm)
        templates = templateFiler(clf_model, ptemplates)
        millis_E = int(round(time.time() * 1000))
        _time.append((millis_E - millis_S)/1000)

        templateList.append(templates)

    return (_time, templateList)

def buildTermList(terms, l):
    if (len(l) > 0):
        lt = []
        lt.append(' '.join(terms[:l[0]]))

        for i in range(len(l) - 1):
            lt.append(' '.join(terms[l[i]:l[i+1]]))

        return lt

    return []

def calcum(l):
    if (len(l) > 0):
        cl = [l[0]]
        for i in range(len(l) - 1):
            t = cl[-1] + l[i + 1]
            cl.append(t)
        return cl
    return []

def getNext(nl, n, t):
    for i in range(n-1):
        nl[-(i + 2)] += 1
        if (sum(nl[:-(i+1)]) <= t - i - 1):
            for j in range(i+1):
                nl[-(j + 1)] = 1
            nl[-1] = t - sum(nl[:-1])
            return nl

    return None

def templateSegment(text, n):
    # split by spaces
    terms = text.split()

    nterms = len(terms)
    nl = [1] * (n - 1)
    nl.append(nterms - len(nl))

    segL = [buildTermList(terms, calcum(nl))]

    while (1):
        nl = getNext(nl, n, nterms)
        if (nl == None):
            break
        segL.append(buildTermList(terms, calcum(nl)))

    return segL

def templateFiler(clf, ptemplates):
    templates = []

    m = {0: 'name', 1: 'address', 2: 'phone'}

    # =======================================
    # for template in ptemplates:
    #     dct = {}
    #     for i, terr in zip(range(len(template)), template):
    #         dct[m[i]] = {'term': template[i], 'score': 0}
    #
    #     templates.append(dct)
    # =======================================

    for terms in ptemplates:
        X = np.asarray([fe.extractFeatureText(term) for term in terms])
        cls = clf.predict(X)

        tmp = copy.deepcopy(cls.reshape((1, cls.shape[0])).tolist()[0])
        tmp.sort()
        if (tmp == list(range(len(terms)))):
            dct = {}
            probs = clf.predict_proba(X)
            for (term, cl, prob) in zip(terms, cls, probs):
                try:
                    dct[m[int(cl)]] = {'term': term, 'score': prob[int(cl)]}
                except ValueError:
                    dct[m[int(cl)]] = {'term': term, 'score': prob[cl]}
            dct['score'] = sum([log(dct[key]['score']) for key in dct])
            templates.append(dct)

    if (len(templates) > 0):
        templates = sorted(templates, key=lambda k: k['score'], reverse=True)

    return templates