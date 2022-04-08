"""
This is a boilerplate pipeline 'anomaly_detection'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_rid_of_anomalies_unsupervised


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])

def get_rid_of_anomalies_in_mnist_train_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func = get_rid_of_anomalies_unsupervised,
            inputs={"x": "mnist-train-images-w-o-8-by_filter_classificator",
                    "y": "mnist-train-labels-w-o-8-by_filter_classificator",
                    "anomaly_detector": 'params:anomaly_detector'},


            outputs = ["mnist-train-images-w-o-8-by_filter_classificator_after_ad",
                       "mnist-train-labels-w-o-8-by_filter_classificator_after_ad"],
            name = "get_rid_of_anomalies_in_mnist_train",
    ),

    ])

def get_rid_of_anomalies_in_mnist_article_train(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func = get_rid_of_anomalies_unsupervised,
            inputs={"x": "mnist-train-images-w-o-8-noised_other_classes",
                    "y": "mnist-train-labels-w-o-8-noised_other_classes",
                    "anomaly_detector": 'params:anomaly_detector'},


            outputs = ["mnist-train-images-w-o-8-noised_other_classes_after_ad",
                       "mnist-train-labels-w-o-8-noised_other_classes_after_ad"],
            name = "get_rid_of_anomalies_in_mnist_train",
    ),

    ])

# https://github.com/dataman-git/codes_for_articles/blob/master/PyOD%20Tutorial%20-%20autoencoder.ipynb