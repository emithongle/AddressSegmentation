__author__ = 'Thong_Le'

import libs.segment as sg
import libs.store as store
from libs.config import *

def test(feature_func, preprocessing_func, file='testdata.txt'):
    # 4. Test
    textList = store.loadTextData(file=file)
    _time, templateList = sg.parseAddress(textList, feature_func, preprocessing_func)

    titles = [['#', 'Text', 'Runtime'],
              ['TestCase', 'Top', 'Name', 'Address', 'Phone', 'NameScore', 'AddressScore', 'PhoneScore', 'Score']]

    store.saveResults(titles, (textList, _time), templateList)

test(feature_func, preprocessing_func)