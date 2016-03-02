__author__ = 'Thong_Le'

import string

from sklearn.cross_validation import train_test_split
import numpy as np
from libs.config import *

def extractFeature(func, pfunc, tupledata):
    names, addresses, phones = tupledata

    X_name, X_address, X_phone = [], [], []
    y_name, y_address, y_phone = [0] * len(names), [1] * len(addresses), [2] * len(phones)

    print('=======================================================')
    print('=> Feature extracting...')

    print('==> Name feature extracting...')
    for text in names:
        X_name.append(eval(func + '(' + pfunc +'(text))'))
    print('<== Name feature extracted.')

    print('==> Address feature extracting...')
    for text in addresses:
        X_address.append(eval(func + '(' + pfunc +'(text))'))
    print('<== Address feature extracted.')

    print('==> Phone feature extracting...')
    for text in phones:
        X_phone.append(eval(func + '(' + pfunc +'(text))'))
    print('<== Phone feature extracted.')

    return [{'X': X_name, 'y': y_name}, {'X': X_address, 'y': y_address}, {'X': X_phone, 'y': y_phone}]


def extractFeatureText(func, pfunc, text):
    return eval(func + '(' + pfunc +'(text))')

def randomSample(tupleData=None, testSize=0.2):
    print('=======================================================')
    print('=> Randoming data...')

    if (tupleData):
        X_train_names, X_test_names, y_train_name, y_test_name = \
            train_test_split(np.asarray(tupleData[0]['X']), tupleData[0]['y'], test_size=testSize)

        X_train_address, X_test_address, y_train_address, y_test_address = \
            train_test_split(np.asarray(tupleData[1]['X']), tupleData[1]['y'], test_size=testSize)

        X_train_phone, X_test_phone, y_train_phone, y_test_phone = \
            train_test_split(np.asarray(tupleData[2]['X']), tupleData[2]['y'], test_size=testSize)

    else:
        folder = '2. Features/'

        datatmp = store.loadJson(folder + 'name_features')
        X_train_names, X_test_names, y_train_name, y_test_name = \
            train_test_split(np.asarray(datatmp['X']), datatmp['y'], test_size=testSize)

        datatmp = store.loadJson(folder + 'address_features')
        X_train_address, X_test_address, y_train_address, y_test_address = \
            train_test_split(np.asarray(datatmp['X']), datatmp['y'], test_size=testSize)

        datatmp = store.loadJson(folder + 'phone_features')
        X_train_phone, X_test_phone, y_train_phone, y_test_phone = \
            train_test_split(np.asarray(datatmp['X']), datatmp['y'], test_size=testSize)

    X_train = np.append(np.append(X_train_names.tolist(),X_train_address.tolist(), axis=0), X_train_phone, axis=0)
    y_train = y_train_name + y_train_address + y_train_phone

    X_test = np.append(np.append(X_test_names.tolist(), X_test_address.tolist(), axis=0), X_test_phone, axis=0)
    y_test = y_test_name + y_test_address + y_test_phone

    print('=> Randomed data.')

    return (X_train, y_train, X_test, y_test)

def removeDuplicate(termList):
    t = []
    for i in range(len(termList)):
        b = True
        for j in range(len(t)):
            if ((' ' + t[j] + ' ').find(' ' + termList[i] + ' ') >= 0):
                b = False
                break
            elif ((' ' + termList[i] + ' ').find(' ' + t[j] + ' ') >= 0):
                t[j] = termList[i]
                b = False
                break
        if (b):
            t.append(termList[i])

    return t

def preprocess4GetTerm(text):
    for c in string.digits:
        text = text.replace(c, ' ')

    for c in string.punctuation:
        text = text.replace(c, ' ')

    return text

feature_names = ['length', '%max_ascii_skip_2', '%max_digit_skip_2',
                 '%asciis', '%digits', '%punctuations', '%others', '%name_keywords', '%address_keywords', '%phone_keywords']

def findMaxStringP(text, cod, skip=0):
    i, nskip = 0, 0
    while (i < len(text) and nskip <= skip):
        if (cod):
            if (text[i] in string.digits):
                nskip += 1
                i += 1
            elif (text[i] in string.ascii_lowercase):
                i += 1
                nskip = 0
            else:
                i += 1
        elif (1 - cod):
            if (text[i] in string.ascii_lowercase):
                nskip += 1
                i += 1
            elif (text[i] in string.digits):
                i += 1
                nskip = 0
            else:
                i += 1
    if nskip > skip:
        return text[:i-2]
    elif (i == len(text)):
        return text

    return text[:i]

def findMaxString(text, skip=0):
    tc, td = '', ''
    try:
        for i in range(len(text)):
            if text[i] in string.digits:
                t = findMaxStringP(text[i:], False, skip)
                if (len(td) < len(t)):
                    td = t
            elif text[i] in string.ascii_lowercase:
                t = findMaxStringP(text[i:], True, skip)
                if (len(tc) < len(t)):
                    tc = t
    except ValueError:
        None

    return tc, td

def feature(text):
    textLen = text.__len__()
    termList = text.split()

    preprocessText = preprocess4GetTerm(text)
    preprocessedTermList = preprocessText.split()
    preprocessedTermListLen = len(preprocessedTermList)

    nameTerms = removeDuplicate([term for term in nameTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])
    addressTerms = removeDuplicate([term for term in addressTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])
    phoneTerms = removeDuplicate([term for term in phoneTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])

    tc, td = findMaxString(text, 2)

    return [
             textLen,

             len(tc) / textLen,
             len(td) / textLen,

             sum([1 for c in text if (c in string.ascii_letters)]) / textLen,
             sum([1 for c in text if (c in string.digits)]) / textLen,
             sum([1 for c in text if (c in string.punctuation)]) / textLen,

             sum([1 for c in text if (c not in (string.punctuation + string.ascii_letters + string.digits))]) / textLen,

             len(nameTerms) / len(nameTermSet) if (len(nameTermSet) > 0) else 0,
             len(addressTerms) / len(addressTermSet) if (len(addressTermSet)) else 0,
             len(phoneTerms) / len(phoneTermSet) if (len(phoneTermSet)) else 0
            ]

def preprocessing(text):
    return text