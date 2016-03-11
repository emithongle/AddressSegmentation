__author__ = 'Thong_Le'

from libs import store
from libs.features import extractFeature, randomSample
from libs.models import buildClassifer
from libs.config import *

# 1. Read txt data
tupleData = store.loadTxtData()

# 2. Extract features
featureTuples = extractFeature(feature_func, preprocessing_func, tupleData)
store.saveFeature(featureTuples)

# 3.1 Random Training and Testing Data
x = randomSample()
store.saveTrainingTestingData(x)

# 3.2 Load Training and Testing Data
modelData = store.loadTrainingTestingData()

# 3.3 Train model
print('=> Training model...')
clf_model = buildClassifer()
clf_model.fit(modelData['X_train'], modelData['y_train'])

y_hat = clf_model.predict(modelData['X_test'])
print('Acc = ', sum([1 for (y1, y2) in zip(modelData['y_test'], y_hat) if (y1 == y2)]) / len(y_hat))

store.saveClassifier(clf_model)

# 4. Test
import test_term_classifier_model
import test_address_segment

None