"""
This is a boilerplate pipeline 'data_selecting'
generated using Kedro 0.17.7
"""


import numpy as np
from sklearn.linear_model import LogisticRegression

def get_rid_of_true_eight_labels(x: np.ndarray, y: np.ndarray) -> [np.ndarray, np.ndarray]:

    print('get_rid_of_true_eight_labels')


    x = x[np.where(y != 8)[0]]
    y = y[np.where(y != 8)[0]]

    print(x.shape, y.shape)

    return x, y

def get_rid_of_eight_labels_by_filter_classificator(x: np.ndarray, y: np.ndarray) -> [np.ndarray, np.ndarray]:

    print('get_rid_of_eight_labels_by_pick_classifier')

    filter_classificator = LogisticRegression()
    filter_classificator.fit(x,y)
    filter_y = filter_classificator.predict(x)

    # not_filter_y_eight_indexes = np.where(filter_y != 8)[0]

    x = x[np.where(filter_y != 8)[0]]
    y = y[np.where(filter_y != 8)[0]]

    print(x.shape, y.shape)

    return x, y


def get_rid_of_true_majority_eights_and_noise_other(x: np.ndarray, y: np.ndarray, digit_anomalie = 8, portion_to_ommit =0.9) -> [np.ndarray, np.ndarray]:

    print('get_rid_of_true_majority_eights_and_noise_other')




    indexes_to_omit = np.random.choice(np.where(y == digit_anomalie)[0],
                                       int(portion_to_ommit * len(np.where(y == digit_anomalie)[0])))
    sub_array = [i for i in range(len(y)) if i not in indexes_to_omit]

    x = x[sub_array]
    y = y[sub_array]

    choose_label = np.array(range(10))
    choose_label = np.delete(choose_label, digit_anomalie)

    random_elements = np.random.choice(choose_label, len(y[np.where(y == digit_anomalie)]))
    indexes_to_change = np.where(y == digit_anomalie)

    y[indexes_to_change] = random_elements

    print(x.shape, y.shape)

    return x, y