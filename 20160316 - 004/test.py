# __author__ = 'Thong_Le'
#
# from os import listdir
# from os.path import isfile, join
# from config import folder_model, model_config_file, feature_list
# from libs.store import loadJson, loadClassifier
# from libs.features import getFeatureNames
# import random
#
# import numpy as np
#
# def listFolders(path):
#     return [f for f in listdir(path) if 1 - isfile(join(path, f))]
#
# def listFiles(path):
#     return [f for f in listdir(path) if isfile(join(path, f))]
#
# def getFeatureList(mcfl):
#     fl = []
#     for (i, tmp) in feature_list:
#         if (i in mcfl):
#             fl.append((i, True))
#         else:
#             fl.append((i, False))
#     return fl
#
# def classifyModels(modelConfig):
#     dct = {}
#
#     for mc in modelConfig:
#         if (mc['model']['config']['n_iter'] not in dct.keys()):
#             dct[mc['model']['config']['n_iter']] = { mc['name']: loadClassifier(file=mc['name'])
#                 # {
#                 #     'model': loadClassifier(file=mc['name']),
#                 #     'features': getFeatureList(mc['features'])
#                 # }
#             }
#         else:
#             dct[mc['model']['config']['n_iter']][mc['name']] = loadClassifier(file=mc['name'])
#             # {
#             #     'model': loadClassifier(file=mc['name']),
#             #     'features': getFeatureList(mc['features'])
#             # }
#
#     dct = sorted(dct.items(), key=lambda k: k[0])
#
#     return dct
#
# def randomSamples(n):
#     l = []
#     ndim = len(getFeatureNames())
#
#     for i in range(n):
#         x = []
#         for xi in range(ndim):
#             x.append(random.random() * 100)
#         l.append(x)
#
#     return np.asarray(l)
#
# modelConfig = loadJson(folder_model + '/' + model_config_file)
# gmodels = classifyModels(modelConfig)
#
# nSamples = 10
#
# X = randomSamples(nSamples)
#
# modelOutputs = {}
# for n_iter, modelDct in gmodels:
#     modelOutputs[n_iter] = {}
#     for mname in modelDct:
#         modelOutputs[n_iter][mname] = modelDct[mname].predict_proba(X).tolist()
#
# None
#
#
#


from libs.segment import templateSegment

X = templateSegment('81 Duong 16, P. Binh Tri Dong B, Q.Binh Tan, 0909218877, Dinh Thi Bich Phuong', 3)
None