"""Test sur le fichier params.py"""

from pathlib import Path
import sys

sys.path.append(str(Path.cwd()))
from settings.params import PARAMS


def test_keys_in_params():
    keys = ["MIN_COMPLETION_RATE", "SEED", "EXPERIMENT_NAME"]
    for key in keys:
        assert key in PARAMS, f"Key {key} is missing in the PARAMS dictionary."
