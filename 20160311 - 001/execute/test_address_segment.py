__author__ = 'Thong_Le'

import libs.segment as sg
import libs.store as store
from config import *

def exc(file='testdata.txt'):
    # 5. Test
    textList = store.loadTextData(file=file)
    if (file_model):
        _time, templateList = sg.parseAddress(textList, file_model)
    else:
        _time, templateList = sg.parseAddress(textList)

    titles = [['#', 'Text', 'Runtime'],
              ['TestCase', 'Top', 'Name', 'Address', 'Phone', 'NameScore', 'AddressScore', 'PhoneScore', 'Score']]

    if (file_model):
        store.saveResults(titles, (textList, _time), templateList, file=file_model + '_' + file_segment_address_result)
    else:
        store.saveResults(titles, (textList, _time), templateList, file=timeManage.getTime() + '_' + file_segment_address_result)