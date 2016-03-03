__author__ = 'Thong_Le'

import libs.segment as sg
import libs.store as store
from libs.config import *

# def checkTemplate(template):
#     if(template['Phone']):
#         return True
#     return False
#
# def templateFilter(ttime, ttemplate):
#     _time, templateList = [], []
#
#     for t1, t2 in zip(ttime, ttemplate):
#         if (checkTemplate(t2)):
#             _time.append(t1)
#             templateList.append(t2)
#
#     return _time, templateList

def test(feature_func, preprocessing_func, file='testdata.txt'):
    # 4. Test
    textList = store.loadTextData(file=file)
    _time, templateList = sg.parseAddress(textList, feature_func, preprocessing_func)
    # _time, templateList = templateFilter(_time, templateList)

    titles = [['#', 'Text', 'Runtime'],
              ['TestCase', 'Top', 'Name', 'Address', 'Phone', 'NameScore', 'AddressScore', 'PhoneScore', 'Score']]

    store.saveResults(titles, (textList, _time), templateList)

test(feature_func, preprocessing_func)