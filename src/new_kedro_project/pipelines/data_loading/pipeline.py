"""
This is a boilerplate pipeline 'data_loading'
generated using Kedro 0.17.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_mnist_ubyte_to_numpy


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])


def load_mnist_ubyte_to_numpy_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func=load_mnist_ubyte_to_numpy,
            inputs=[],
            outputs=["mnist-train-images", "mnist-train-labels", "mnist-test-images", "mnist-test-labels"],
            name="load_mnist_ubyte_to_pandas_csv",
        ),

    ])

