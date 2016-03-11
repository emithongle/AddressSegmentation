__author__ = 'Thong_Le'

import libs.segment as sg
import libs.store as store
from config import *

def exc(file='testdata.txt'):
    # 5. Test
    textList = store.loadTextData(file=file)
    _time, templateList = sg.parseAddress(textList)

    titles = [['#', 'Text', 'Runtime'],
              ['TestCase', 'Top', 'Name', 'Address', 'Phone', 'NameScore', 'AddressScore', 'PhoneScore', 'Score']]

    store.saveResults(titles, (textList, _time), templateList, file=timeManage.getTime() + '_' + file_segment_address_result)