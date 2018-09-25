# TW-JP project dataset

## Overviews
This is a kind of prototype to developing a dataset by python. We use `metadata.yaml` and `labeldata.yaml` to restore the infromation of this dataset. There are also 3 python program for building the two infromation data. The 3 python program is:
* `build_meta.py`: Generating a `metadata.yaml` file with some statisical information automatically.
* `add_keywords.py`: Providing a way to insert a keyword to `metadata.yaml`.
* `file_dragger`: A base for the labeling tool of `labeldata.yaml`. It sould can provide the options (keywords) which are defined in `metadata.yaml`.

## Requirments
* python 3
* numpy
* [ruamel.yaml](https://yaml.readthedocs.io/en/latest/install.html)
* [wxPython](https://www.wxpython.org/pages/downloads/) for `file_dragger.py`

## TODO
* Developing `file_dragger` (and rename it if needed)
* Revise `build_meta` and `add_keyword`. (Maybe combine the two with a simple GUI?)
# TWJP-dataset
