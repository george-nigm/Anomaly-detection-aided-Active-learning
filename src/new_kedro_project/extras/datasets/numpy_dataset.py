from pathlib import PurePosixPath
from typing import Any, Dict

import fsspec
import numpy as np
from numpy import savetxt, loadtxt
from PIL import Image

from kedro.io import AbstractDataSet
from kedro.io.core import get_filepath_str, get_protocol_and_path

class NumpyDataSet(AbstractDataSet):
    def __init__(self, filepath: str):

        protocol, path = get_protocol_and_path(filepath)
        self._protocol = protocol
        self._filepath = PurePosixPath(path)
        self._fs = fsspec.filesystem(self._protocol)

    def _load(self) -> np.ndarray:
        """Loads data from the image file.

        Returns:
            Data from the image file as a numpy array
        """
        load_path = get_filepath_str(self._filepath, self._protocol)
        with self._fs.open(load_path, mode="r") as f:
            data = loadtxt(f, delimiter=',')
            return data

    def _save(self, data: np.ndarray) -> None:
        """Saves image data to the specified filepath."""
        save_path = get_filepath_str(self._filepath, self._protocol)
        with self._fs.open(save_path, mode="wb") as f:
            savetxt(f, data, delimiter=',')

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset."""
        return dict(filepath=self._filepath, protocol=self._protocol)