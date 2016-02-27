__author__ = 'Thong_Le'

from libs import store

# ================================
tmp = store.loadDictionary()
nameTermSet = tmp['name-term-set']
addressTermSet = tmp['address-term-set']
phoneTermSet = tmp['phone-term-set']

asi = tmp['ascii']
unic = tmp['unicode']

feature_func = 'feature'
preprocessing_func = 'preprocessing'

# Testing Model
standard_data = True
nTesting = 10