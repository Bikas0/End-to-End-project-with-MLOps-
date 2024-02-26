import os
import pathlib
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
print(PACKAGE_ROOT)