__author__ = 'Thong_Le'

from libs import store
from libs.models import buildClassifer

def exc():
    # 4.2 Load Training and Testing Data
    modelData = store.loadTrainingTestingDataCSV()

    # 4.3 Train model
    print('=> Training model...')
    clf_model = buildClassifer()
    clf_model.fit(modelData['X_train'], modelData['y_train'])

    y_hat = clf_model.predict(modelData['X_test'])
    tacc = sum([1 for (y1, y2) in zip(modelData['y_test'], y_hat) if (y1 == y2)]) / len(y_hat)
    print('Acc = ', tacc)

    store.saveClassifier(clf_model)

    return tacc

acc = exc()