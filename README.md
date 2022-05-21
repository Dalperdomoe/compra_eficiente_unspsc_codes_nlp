Compra Eficiente UNSPSC Codes NLP
==============================

classification of public procurement through UNSPSC codes.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

Setup
------------

Credentials
-----------

In order to use sodapy, you must take the following into account to use the API token:
- Create a '.env' file in root's repository.
- Finally, the credentials MUST be stored as it is shown in environment_example file.

Python Enviroment (Optional)
-----------

Create a python enviroment in root's repository
```
python3 -m venv env
```

Activate the enviroment
```
source .env/bin/activate
```


Installation
------------
```
python setup.py install
```

Install required packages
```
pip install -r requirements
```

Authors
------------

Laura Navarro

Julian Vargas

Daniel Perdomo

Julian Chacon

Victor Rivera

Jose Dager

Jose Cardenas

For Contributors
------------

General Remarks
-----------
This library broadly follows the PEP8 style guide.

Additionally, names of classes, methods and functions must be written in English, and the documentation must also be in English.

Docstrings use the NumPy style and type hints are highly encouraged.

Version Change Policies
-----------
- X.0.0 -- Major version change: merge to master branch (stable release).

- 0.X.0 -- Middle version change: change that may affect previous functionality.

- 0.0.X -- Minor version change: change that does not affect existing functionality.


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
