__author__ = 'Thong_Le'

import json
import numpy as np
import pickle
import xlsxwriter
from math import log

def readFile(file):
    strList = []
    infile = open(file, encoding="utf-8")
    for line in infile:
        strList.append(line)
    return strList

def saveJson(data, file):
    with open(file+'.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

def loadJson(file):
    try:
        return json.loads(''.join(readFile(file + '.json')))
    except:
        return None

def loadTxtData(folder='1. Data/', files=['name.txt', 'address.txt', 'phone.txt']):

    print('=======================================================')
    print('=> Reading data...')

    print('==> Reading name data...')
    name = readFile(folder + files[0])
    name = name[1:]
    print('<== Readed name data.')

    print('==> Reading address data...')
    address = readFile(folder + files[1])
    address = address[1:]
    print('<== Readed address data.')

    print('==> Reading phone data...')
    phone = readFile(folder + files[2])
    phone = phone[1:]
    print('<== Readed phone data.')

    return (name, address, phone)

def loadTextData(folder='4. Test/', file='testdata.txt'):

    print('=======================================================')
    print('=> Loading data test...')
    textList = readFile(folder + file)
    textList = textList[1:]
    print('<= Loading data test...')

    return textList

def saveFeature(tupledata, folder='2. Features/', files=['name_features', 'address_features', 'phone_features']):

    print('=======================================================')
    print('=> Saving features...')

    print('==> Saving name features...')
    saveJson(tupledata[0], folder + files[0])
    print('<== Saved name features.')

    print('==> Saving address features...')
    saveJson(tupledata[1], folder + files[1])
    print('<== Saved address features.')

    print('==> Saving phone features...')
    saveJson(tupledata[2], folder + files[2])
    print('<== Saved phone features.')

def saveTrainingTestingData(tupleData, folder='2. Features/', files=['X_train', 'y_train', 'X_test', 'y_test']):
    print('=======================================================')
    print('=> Saving data for training and testing...')

    saveJson(tupleData[0].tolist(), folder + files[0])
    saveJson(tupleData[1], folder + files[1])
    saveJson(tupleData[2].tolist(), folder + files[2])
    saveJson(tupleData[3], folder + files[3])

    print('<= Saved data.')

def loadTrainingTestingData(folder='2. Features/', files=['X_train', 'y_train', 'X_test', 'y_test']):
    print('=======================================================')
    print('=> Loading data for training and testing...')

    X_train = np.asarray(loadJson(folder + files[0]))
    y_train = np.asarray(loadJson(folder + files[1]))
    X_test = np.asarray(loadJson(folder + files[2]))
    y_test = np.asarray(loadJson(folder + files[3]))

    print('<= Loaded data.')

    return {'X_train': X_train, 'y_train': y_train, 'X_test': X_test, 'y_test': y_test}

def loadClassifier(name='3. Model/model'):
    print('=======================================================')
    print('=> Loading model...')
    with open(name + '.pkl', 'rb') as f:
        try:
            print('=> Loading model...')
            model = pickle.load(f, encoding='latin1')
            print('=> Loaded model.')
        except:
            model = pickle.load(f)
    print('<= Loaded model.')
    return model

def saveClassifier(clf, name='3. Model/model'):
    print('=======================================================')
    print('=> Saving model...')
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(clf, f)
    print('<= Saved model.')

def loadDictionary(file='0. Dictionary/dictionary'):
    tmp = loadJson(file)
    return tmp


def writeSheet(sheet, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])


def saveResults(titles, input_tuple, templateList, folder='5. Results/', file='result.xlsx'):

    orgData = [titles[0]]
    for i in range(len(input_tuple[0])):
        orgData.append([i, input_tuple[0][i], input_tuple[1][i]])

    sg_1 = [titles[1]]
    for i, templates in zip(range(len(templateList)), templateList):
        for j, template in zip(range(len(templates)), templates):
            t = [i, j, template['name']['term'], template['address']['term'], template['phone']['term'],
                 template['name']['score'], template['address']['score'], template['phone']['score'],
                 template['score']]
            sg_1.append(t)

    # =========================

    workbook = xlsxwriter.Workbook(folder + file)
    writeSheet(workbook.add_worksheet('original'), orgData)
    writeSheet(workbook.add_worksheet('segment_1'), sg_1)
    workbook.close()

def saveTestModel(accs, folder='5. Results/', file='test_model_results.xlsx'):

    data = [['#', 'Accuracy']]
    for i, acc in zip(range(len(accs)), accs):
        data.append([i, acc])

    workbook = xlsxwriter.Workbook(folder + file)
    writeSheet(workbook.add_worksheet('accuracy'), data)
    workbook.close()