__author__ = 'Thong_Le'

from libs import segment as sg, store
from libs.config import *

def test(feature_func, preprocessing_func):
    # 4. Test
    textList = store.loadTextData()
    print('=======================================================')
    print('=> Address Parsing...')
    _time, templateList = sg.parseAddress(textList, feature_func, preprocessing_func)

    titles = [['#', 'Text', 'Runtime'],
              ['TestCase', 'Top', 'Name', 'Address', 'Phone', 'NameScore', 'AddressScore', 'PhoneScore', 'Score']]

    store.saveResults(titles, (textList, _time), templateList)
    print('<= Address Parsed.')


test(feature_func, preprocessing_func)