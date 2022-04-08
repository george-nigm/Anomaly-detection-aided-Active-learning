"""
This is a boilerplate pipeline 'data_loading'
generated using Kedro 0.17.7
"""

from mlxtend.data import loadlocal_mnist

def load_mnist_ubyte_to_numpy():

    print('load_train_mnist_ubyte_to_numpy')

    images_train_pat = "data/01_raw/mnist/train-images-idx3-ubyte"
    labels_train_pat = "data/01_raw/mnist/train-labels-idx1-ubyte"
    images_test_pat = "data/01_raw/mnist/t10k-images-idx3-ubyte"
    labels_test_pat = "data/01_raw/mnist/t10k-labels-idx1-ubyte"

    x_train, y_train = loadlocal_mnist(images_path=images_train_pat, labels_path=labels_train_pat)
    x_test, y_test = loadlocal_mnist(images_path=images_test_pat, labels_path=labels_test_pat)

    print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

    return x_train, y_train, x_test, y_test
