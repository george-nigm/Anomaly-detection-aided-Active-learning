"""
This is a boilerplate pipeline 'classification'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import active_learning


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])


def active_learning_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=active_learning,
            inputs={'x_train': "mnist-train-images-w-o-8", 'y_train': "mnist-train-labels-w-o-8",
                    'x_test': "mnist-test-images-w-o-8", 'y_test': "mnist-test-labels-w-o-8",
                    "classificator": 'params:classificator',
                    "active_learning_step": 'params:active_learning_step',
                    "expirement_name": 'params:exp_name_1'},
            outputs=["active_metrics_plot", "first_expirements_predicts", "no_correct_classified_dynamic", "train_volume"],
            name="Active_learning_batch_train_evaluate",
        ),

    ])

def active_learning_second_expirement_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=active_learning,
            inputs={'x_train': "mnist-train-images-w-o-8-by_filter_classificator",
                    'y_train': "mnist-train-labels-w-o-8-by_filter_classificator",
                    'x_test': "mnist-test-images-w-o-8",
                    'y_test': "mnist-test-labels-w-o-8",
                    "classificator": 'params:classificator',
                    "active_learning_step": 'params:active_learning_step',
                    "expirement_name": 'params:exp_name_2'},

            outputs=["second_expirement_active_metrics_plot", "second_expirement_predicts", "second_expirement_no_correct_classified_dynamic", "second_expirement_train_volume"],
            name="second_expirement_active_learning_batch_train_evaluate",
        ),
    ])

def active_learning_second_expirement_article_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=active_learning,
            inputs={'x_train': "mnist-train-images-w-o-8-noised_other_classes",
                    'y_train': "mnist-train-labels-w-o-8-noised_other_classes",
                    'x_test': "mnist-test-images-w-o-8",
                    'y_test': "mnist-test-labels-w-o-8",
                    "classificator": 'params:classificator',
                    "active_learning_step": 'params:active_learning_step',
                    "expirement_name": 'params:exp_name_2',
                    "noised": 'params:noised'},

            outputs=["second_expirement_article_active_metrics_plot", "second_expirement_predicts", "second_expirement_no_correct_classified_dynamic", "second_expirement_train_volume"],
            name="active_learning_second_expirement_article",
        ),
    ])


def active_learning_third_expirement_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=active_learning,
            inputs={'x_train': "mnist-train-images-w-o-8-by_filter_classificator_after_ad",
                    'y_train': "mnist-train-labels-w-o-8-by_filter_classificator_after_ad",
                    'x_test': "mnist-test-images-w-o-8",
                    'y_test': "mnist-test-labels-w-o-8",
                    "classificator": 'params:classificator',
                    "active_learning_step": 'params:active_learning_step',
                    "expirement_name": 'params:exp_name_3',
                    "ad_name": 'params:anomaly_detector',
                    "ad_step": 'params:active_learning_step',
                    "noised": 'params:noised'},

            outputs=["third_expirement_active_metrics_plot", "third_expirement_predicts",
                     "third_expirement_no_correct_classified_dynamic", "third_expirement_train_volume"],
            name="third_expirement_active_learning_batch_train_evaluate",
        ),
    ])

def active_learning_article_third_expirement_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=active_learning,
            inputs={'x_train': "mnist-train-images-w-o-8-noised_other_classes_after_ad",
                    'y_train': "mnist-train-labels-w-o-8-noised_other_classes_after_ad",
                    'x_test': "mnist-test-images-w-o-8",
                    'y_test': "mnist-test-labels-w-o-8",
                    "classificator": 'params:classificator',
                    "active_learning_step": 'params:active_learning_step',
                    "expirement_name": 'params:exp_name_3',
                    "ad_name": 'params:anomaly_detector',
                    "ad_step": 'params:active_learning_step',
                    "noised": 'params:noised'},

            outputs=["third_expirement_active_metrics_plot", "third_expirement_predicts",
                     "third_expirement_no_correct_classified_dynamic", "third_expirement_train_volume"],
            name="third_expirement_active_learning_batch_train_evaluate",
        ),
    ])