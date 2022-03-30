"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline, pipeline

from ad2ml.pipelines.data_loading import pipeline as data_loading
from ad2ml.pipelines.data_selecting import pipeline as data_selecting
from ad2ml.pipelines.classification import pipeline as classification

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    load_train_mnist_ubyte_to_numpy_pipeline = data_loading.load_train_mnist_ubyte_to_numpy_pipeline()
    get_rid_of_true_eight_labels_in_test_and_in_train = data_selecting.get_rid_of_true_eight_labels_in_test_and_in_train()
    fit_model = classification.fit_model_pipeline()
    fit_model_and_evaluation = classification.fit_model_and_evaluation_pipeline()
    active_learning = classification.active_learning_pipeline()

    return {"__default__": load_train_mnist_ubyte_to_numpy_pipeline,
            "first_expirement": load_train_mnist_ubyte_to_numpy_pipeline+
                                get_rid_of_true_eight_labels_in_test_and_in_train+
                                fit_model,

            "first_expirement_metrics": load_train_mnist_ubyte_to_numpy_pipeline +
                                get_rid_of_true_eight_labels_in_test_and_in_train +
                                active_learning,
            }




