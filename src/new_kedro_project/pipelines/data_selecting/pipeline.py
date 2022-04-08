"""
This is a boilerplate pipeline 'data_selecting'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_rid_of_true_eight_labels, get_rid_of_eight_labels_by_filter_classificator, get_rid_of_true_majority_eights_and_noise_other

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])

def get_rid_of_true_eight_labels_in_mnist_test_and_in_train_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=get_rid_of_true_eight_labels,
            inputs=["mnist-train-images", "mnist-train-labels"],
            outputs=["mnist-train-images-w-o-8", "mnist-train-labels-w-o-8"],
            name="get_rid_of_ground_truth_eights_in_mnist_train",
        ),

        node(
            func=get_rid_of_true_eight_labels,
            inputs=["mnist-test-images", "mnist-test-labels"],
            outputs=["mnist-test-images-w-o-8", "mnist-test-labels-w-o-8"],
            name="get_rid_of_ground_truth_eights_in_mnist_test",
        ),

    ])

def get_rid_of_true_eight_labels_in_mnist_test_pipeline_and_eight_labels_by_filter_classificator_in_train(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=get_rid_of_true_eight_labels,
            inputs=["mnist-test-images", "mnist-test-labels"],
            outputs=["mnist-test-images-w-o-8", "mnist-test-labels-w-o-8"],
            name="get_rid_of_ground_truth_eights_in_mnist_test",
        ),

        node(
            func = get_rid_of_eight_labels_by_filter_classificator,
            inputs=["mnist-train-images", "mnist-train-labels"],
            outputs = ["mnist-train-images-w-o-8-by_filter_classificator",
                       "mnist-train-labels-w-o-8-by_filter_classificator"],
            name = "get_rid_of_eight_labels_by_filter_classificator_in_mnist_train",
    ),

    ])


def get_rid_of_true_eight_labels_in_mnist_test_and_true_majority_eights_noise_other_classes_in_train(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=get_rid_of_true_eight_labels,
            inputs=["mnist-test-images", "mnist-test-labels"],
            outputs=["mnist-test-images-w-o-8", "mnist-test-labels-w-o-8"],
            name="get_rid_of_ground_truth_eights_in_mnist_test",
        ),

        node(
            func = get_rid_of_true_majority_eights_and_noise_other,
            inputs=["mnist-train-images", "mnist-train-labels"],
            outputs = ["mnist-train-images-w-o-8-noised_other_classes",
                       "mnist-train-labels-w-o-8-noised_other_classes"],
            name = "get_rid_of_true_majority_eights_and_noise_other_in_train",
    ),

    ])
