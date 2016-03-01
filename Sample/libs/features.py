__author__ = 'Thong_Le'

from sklearn.cross_validation import train_test_split
import numpy as np

from libs import store


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


feature_names = ['Length/2']

def feature(text):
    return [len(text)/2]

def preprocessing(text):
    return text