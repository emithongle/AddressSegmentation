__author__ = 'Thong_Le'

from sknn.mlp import Classifier, Layer

def buildClassifer(name='Neuron Network'):

    return Classifier(
        layers=[
            Layer("Sigmoid", units=100),
            Layer("Softmax", units=3)],
        learning_rule='adagrad',
        learning_rate=0.01,
        # n_iter=1000
        n_iter=1
    )
