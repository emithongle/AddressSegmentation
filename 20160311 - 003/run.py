__author__ = 'Thong_Le'

import time

import xlrd
import xlsxwriter

from libs.models import modelDetails
from config import *
from libs.store import writeSheet

tmpsheet = xlrd.open_workbook('running_logs/logs.xlsx').sheet_by_index(0)
logs = []
for i in range(tmpsheet.nrows):
    logs.append(tmpsheet.row_values(i))

millis_S = int(round(time.time() * 1000))


# 1. Preprocessing
from execute import preprocessing

# 2. Extract Features
from execute import extract_feature

# 3. Random Data
from execute import random_data

# 4. Train Data
from execute import train

# 5. Test
# 5.1. Test Term Classification
from execute import test_term_classifier_model as tt, train
# 5.2. Test Address Segmentation
from execute import test_address_segment

millis_E = int(round(time.time() * 1000))
# _time.append((millis_E - millis_S)/1000)


logs.append([time_start,
             (millis_E - millis_S)/1000,
             ', '.join([key for key in preprocessing_name if preprocessing_name[key]])
                if bpreprocessing else '',
             str(len(feature_names)) + ' features: ' + ', '.join(feature_names),
             model_type,
             modelDetails(),
             train.acc,
             tt.acc]
        )

workbook = xlsxwriter.Workbook(folder_running_logs + '/' + file_log)
writeSheet(workbook.add_worksheet('logs'), logs)
workbook.close()