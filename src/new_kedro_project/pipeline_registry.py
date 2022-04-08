"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline, pipeline

from new_kedro_project.pipelines.data_loading import pipeline as data_loading
from new_kedro_project.pipelines.data_selecting import pipeline as data_selecting
from new_kedro_project.pipelines.classification import pipeline as classification
from new_kedro_project.pipelines.anomaly_detection import pipeline as anomaly_detection

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    load_mnist_ubyte_to_numpy = data_loading.load_mnist_ubyte_to_numpy_pipeline()

    get_rid_of_true_eight_labels_in_mnist_test_and_in_train = data_selecting.get_rid_of_true_eight_labels_in_mnist_test_and_in_train_pipeline()
    get_rid_of_true_eight_labels_in_mnist_test_pipeline_and_eight_labels_by_filter_classificator_in_train = data_selecting.get_rid_of_true_eight_labels_in_mnist_test_pipeline_and_eight_labels_by_filter_classificator_in_train()
    get_rid_of_true_eight_labels_in_mnist_test_and_true_majority_eights_noise_other_classes_in_train = data_selecting.get_rid_of_true_eight_labels_in_mnist_test_and_true_majority_eights_noise_other_classes_in_train()

    active_learning = classification.active_learning_pipeline()
    active_learning_second_expirement_pipeline = classification.active_learning_second_expirement_pipeline()
    active_learning_second_expirement_article_pipeline = classification.active_learning_second_expirement_article_pipeline()
    active_learning_third_expirement_pipeline = classification.active_learning_third_expirement_pipeline()
    active_learning_article_third_expirement_pipeline = classification.active_learning_article_third_expirement_pipeline()

    get_rid_of_anomalies_in_mnist_train = anomaly_detection.get_rid_of_anomalies_in_mnist_train_pipeline()
    get_rid_of_anomalies_in_mnist_article_train = anomaly_detection.get_rid_of_anomalies_in_mnist_article_train()

    return {"__default__": load_mnist_ubyte_to_numpy +
                           get_rid_of_true_eight_labels_in_mnist_test_and_in_train+
                           active_learning,

            "first_expirement_dataset_loading": load_mnist_ubyte_to_numpy,
            "first_expirement_input_construction": get_rid_of_true_eight_labels_in_mnist_test_and_in_train,
            "first_expirement_active_learning": active_learning,

            "first_expirement": load_mnist_ubyte_to_numpy +
                           get_rid_of_true_eight_labels_in_mnist_test_and_in_train +
                           active_learning,

            "second_expirement": load_mnist_ubyte_to_numpy+
                                 get_rid_of_true_eight_labels_in_mnist_test_pipeline_and_eight_labels_by_filter_classificator_in_train+
                                 active_learning_second_expirement_pipeline,

            "second_expirement_article": load_mnist_ubyte_to_numpy +
                                 get_rid_of_true_eight_labels_in_mnist_test_and_true_majority_eights_noise_other_classes_in_train +
                                 active_learning_second_expirement_article_pipeline,

            "third_expirement": load_mnist_ubyte_to_numpy+
                                get_rid_of_true_eight_labels_in_mnist_test_pipeline_and_eight_labels_by_filter_classificator_in_train+
                                get_rid_of_anomalies_in_mnist_train+
                                active_learning_third_expirement_pipeline,

            "third_expirement_article": load_mnist_ubyte_to_numpy +
                                get_rid_of_true_eight_labels_in_mnist_test_and_true_majority_eights_noise_other_classes_in_train +
                                get_rid_of_anomalies_in_mnist_article_train +
                                active_learning_article_third_expirement_pipeline,
            }






