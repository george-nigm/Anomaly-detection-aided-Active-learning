from pathlib import PurePosixPath
from typing import Any, Dict

import fsspec
import numpy as np
from numpy import savetxt, loadtxt
from PIL import Image

from kedro.io import AbstractVersionedDataSet
from kedro.io.core import get_filepath_str, get_protocol_and_path, Version

class NumpyDataSet(AbstractVersionedDataSet):
    def __init__(self, filepath: str, version: Version = None):

        protocol, path = get_protocol_and_path(filepath)
        self._protocol = protocol
        self._fs = fsspec.filesystem(self._protocol)

        super().__init__(filepath = PurePosixPath(path), version = version,
                         exists_function = self._fs.exists, glob_function = self._fs.glob)

    def _load(self) -> np.ndarray:
        load_path = get_filepath_str(self._get_load_path(), self._protocol)
        with self._fs.open(load_path, mode="r") as f:
            data = loadtxt(f, delimiter=',')
            return data

    def _save(self, data: np.ndarray) -> None:
        """Saves image data to the specified filepath."""
        save_path = get_filepath_str(self._get_save_path(), self._protocol)
        with self._fs.open(save_path, mode="wb") as f:
            savetxt(f, data, delimiter=',')

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset."""
        return dict(filepath=self._filepath, version = self._version, protocol = self._protocol)