__author__ = 'Thong_Le'

import string

from sklearn.cross_validation import train_test_split
import numpy as np

from config import *
from libs import store

def extractFeature(tupledata):
    names, addresses, phones = tupledata

    y_name, X_name = names[0], []
    y_address, X_address = addresses[0], []
    y_phone, X_phone = phones[0], []

    print('=======================================================')
    print('=> Feature extracting...')

    print('==> Name feature extracting...')
    for text in names[1]:
        X_name.append(feature(text[0]))

    print('<== Name feature extracted.')

    print('==> Address feature extracting...')
    for text in addresses[1]:
        X_address.append(feature(text[0]))
    print('<== Address feature extracted.')

    print('==> Phone feature extracting...')
    for text in phones[1]:
        X_phone.append(feature(str(text[0])))
    print('<== Phone feature extracted.')

    # return [{'X': X_name, 'y': y_name}, {'X': X_address, 'y': y_address}, {'X': X_phone, 'y': y_phone}]
    return [[y_name, X_name, names[1]], [y_address, X_address, addresses[1]], [y_phone, X_phone, phones[1]]]


def extractFeatureText(text):
    if (bpreprocessing):
        text = preprocess(text)
    return feature(text)

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

        datatuple = store.loadFeatureCSV()

        X_train_names, X_test_names, y_train_name, y_test_name = \
            train_test_split(np.asarray(datatuple[0][1]), datatuple[0][0], test_size=testSize)

        X_train_address, X_test_address, y_train_address, y_test_address = \
            train_test_split(np.asarray(datatuple[1][1]), datatuple[1][0], test_size=testSize)

        X_train_phone, X_test_phone, y_train_phone, y_test_phone = \
            train_test_split(np.asarray(datatuple[2][1]), datatuple[2][0], test_size=testSize)

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

# feature_names = ['length', '%asciis', '%digits', '%punctuations', '%others',
# 	'%name_keywords', '%address_keywords', '%phone_keywords',
#     'first_ascii', 'first_digit', 'second_ascii', 'second_digit', 'third_ascii', 'third_digit']

def checkCharacterType(c):
    if c in string.digits:
        return {True: 'digit'}
    elif c in string.ascii_uppercase + string.ascii_lowercase + unic:
        return {True: 'ascii'}
    else:
        return {True: None}

def feature(text):
    textLen = text.__len__()
    termList = text.split()

    preprocessText = preprocess4GetTerm(text)
    preprocessedTermList = preprocessText.split()
    preprocessedTermListLen = len(preprocessedTermList)

    nameTerms = removeDuplicate([term for term in nameTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])
    addressTerms = removeDuplicate([term for term in addressTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])
    phoneTerms = removeDuplicate([term for term in phoneTermSet if (preprocessText.find(' ' + term + ' ')>= 0)])

    # nNameTerm = sum([len(term.split()) for term in nameTerms])
    # nAddressTerm = sum([len(term.split()) for term in addressTerms])
    # nPhoneTerm = sum([len(term.split()) for term in phoneTerms])


    return [
             len(text),

             sum([1 for c in text if (c in string.ascii_letters)]) / textLen,
             sum([1 for c in text if (c in string.digits)]) / textLen,
             sum([1 for c in text if (c in string.punctuation)]) / textLen,

             sum([1 for c in text if (c not in (string.punctuation + string.ascii_letters + string.digits))]) / textLen,

             len(nameTerms) / len(nameTermSet) if (len(nameTermSet) > 0) else 0,
             len(addressTerms) / len(addressTermSet) if (len(addressTermSet)) else 0,
             len(phoneTerms) / len(phoneTermSet) if (len(phoneTermSet)) else 0
            ] + \
           ([
                # First Character Type
                 1 if checkCharacterType(text[0])[True] == 'ascii' else 0,
                 1 if checkCharacterType(text[0])[True] == 'digit' else 0
            ] if len(text) >= 1 else [0, 0]) + \
           ([
                # Second Character Type
                 1 if checkCharacterType(text[1])[True] == 'ascii' else 0,
                 1 if checkCharacterType(text[1])[True] == 'digit' else 0
            ] if len(text) >= 2 else [0, 0]) + \
           ([
                # Third Character Type
                 1 if checkCharacterType(text[2])[True] == 'ascii' else 0,
                 1 if checkCharacterType(text[2])[True] == 'digit' else 0
            ] if len(text) >= 3 else [0, 0])

def dataPreprocess(tupleData):

    for i in range(len(tupleData[0][1])):
        tupleData[0][1][i] = preprocess(tupleData[0][1][i])

    for i in range(len(tupleData[0][1])):
        tupleData[1][1][i] = preprocess(tupleData[1][1][i])

    for i in range(len(tupleData[0][1])):
        tupleData[2][1][i] = preprocess(tupleData[2][1][i])

    return tupleData

def preprocess(text):
    # remove unicode
    if (preprocessing_name['convert unicode to ascii']):
        for i in range(len(unic)):
            text = text.replace(unic[i], asi[i])

    if (preprocessing_name['remove break line']):
        text = text.replace('\n', '')

    if (preprocessing_name['convert to lower']):
        text = text.lower()

    if (preprocessing_name['remove space by space']):
        while (text != text.replace('  ', ' ')):
            text = text.replace('  ', ' ')

    return text