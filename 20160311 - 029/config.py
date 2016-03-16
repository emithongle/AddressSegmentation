__author__ = 'Thong_Le'

import json
import datetime

def readFile(file):
    strList = []
    infile = open(file, encoding="utf-8")
    for line in infile:
        strList.append(line)
    return strList

def loadJson(file):
    try:
        return json.loads(''.join(readFile(file + '.json')))
    except:
        return None

class TimeManage():
    def __init__(self):
        self.time = ''

    def setTime(self, _time):
        self.time = _time

    def getTime(self):
        return self.time

timeManage = TimeManage()

# ================================

folder_dictionary = '0. Dictionary'
files_dictionary = 'dictionary' # json

folder_data = '1. Data'
files_data = ['name.txt', 'address.txt', 'phone.txt']

folder_preprocessing = '2. Preprocessing'
files_preprocessed = ['preprocessed_name', 'preprocessed_address', 'preprocessed_phone'] # csv

folder_features = '3. Features'
files_features = ['name_features', 'address_features', 'phone_features'] # csv
files_traintest = ['training_data', 'testing_data']

folder_model = '4. Model'
file_model = None

folder_test = '5. Test'
file_full_address_test = 'testdata.txt'
file_term_test = 'termdata' # csv

folder_results = '6. Results'
file_segment_address_result = 'full_address_results.xlsx'
file_term_classify_result = 'term_results.xlsx'
file_model_result = 'test_model_results.xlsx'

folder_running_logs = 'running_logs'
file_log = 'logs.xlsx' # csv

# ==============================================

# number of executive run.py
nrun = 1

tmp = loadJson(folder_dictionary + '/' + files_dictionary)
nameTermSet = tmp['name-term-set']
addressTermSet = tmp['address-term-set']
phoneTermSet = tmp['phone-term-set']

asi = tmp['ascii']
unic = tmp['unicode']
upchars = tmp['upper-characters']

feature_func = 'feature'
preprocessing_func = 'preprocessing'


# Preprocessing
bpreprocessing = True
preprocessing_name = {'convert unicode to ascii': True, 'convert to lower': True,
                      'remove break line': True, 'remove space by space': True}

# Features
feature_names = ['%digits', '%ascii', 'length', 'first_character_ascii', 'first_character_digit']

# Model
model_type = 'Neuron Network'
model_config = {
    'layers': [(100, 'Sigmoid'), (3, 'Softmax')],
    'learning_rate': 0.01,
    'learning_rule': 'adagrad',
    'n_iter': 1000
}

# Testing Model
standard_data = True
nTesting = 10



