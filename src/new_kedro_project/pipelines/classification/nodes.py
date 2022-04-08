"""
This is a boilerplate pipeline 'classification'
generated using Kedro 0.17.7
"""

from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_classification_metrics(y_pred, y_test):

    print('metrics calculation on test data')
    metric = np.sum(y_test == y_pred)

    print('# of samples in test:', y_test.shape)
    print('final metric:', metric)

    return metric

def active_learning(x_train, y_train, x_test, y_test,
                    active_learning_step = 10000,
                    classificator = "LogisticRegression",
                    expirement_name = "exp_no__",
                    ad_name = "",
                    ad_step = "",
                    noised = ""):

    if classificator == "LogisticRegression":
        model = LogisticRegression()

    budget_list = []
    active_metrics = []
    y_pred_list = []

    for budget in range(5000, x_train.shape[0], active_learning_step):

        print(f'train on {budget} of total {x_train.shape[0]}')
        budget_list.append(budget)

        model.fit(x_train[:budget], y_train[:budget])
        y_pred = np.array(model.predict(x_test))
        active_metrics.append(get_classification_metrics(y_pred, y_test))
        y_pred_list.append(y_pred)

    # training on all available data (final stage of active learning)

    print(f'train on {x_train.shape[0]} of total {x_train.shape[0]}')
    budget_list.append(x_train.shape[0])
    model.fit(x_train, y_train)
    y_pred = np.array(model.predict(x_test))
    active_metrics.append(get_classification_metrics(y_pred, y_test))
    y_pred_list.append(y_pred)

    print(active_metrics)

    sns.set_style("darkgrid")
    plt.plot(budget_list, active_metrics)

    if ad_name == "":
        pd.DataFrame(data={'budget': budget_list, 'metric': active_metrics}).to_csv(
            f'data/08_reporting/{expirement_name}{noised}budget_step_{ad_step}_metric.csv')
    else:
        pd.DataFrame(data={'budget': budget_list, 'metric': active_metrics}).to_csv(
            f'data/08_reporting/{expirement_name}{noised}{ad_name}_budget_step_{ad_step}_metric.csv')

    return plt, np.array(y_pred_list), np.array(active_metrics), np.array(budget_list)
