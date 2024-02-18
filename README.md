# MLOPS_ASSIGNMENT_GROUP2_TEAM6

## Tools used in this project

- [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
- [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
- [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting
- [DVC](https://dvc.org/): Data version control - [article](https://mathdatasimplified.com/2023/02/20/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-2/)
- [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project

## Set up the environment

1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:

```bash
make env
```

## Install dependencies

To install all dependencies for this project, run:

```bash
poetry install
```

To install a new package, run:

```bash
poetry add <package-name>
```

## Version your data

To track changes to the "data" directory, type:

```bash
dvc add data
```

This command will create the "data.dvc" file, which contains a unique identifier and the location of the data directory in the file system.

To keep track of the data associated with a particular version, commit the "data.dvc" file to Git:

```bash
git add data.dvc
git commit -m "add data"
```

To push the data to remote storage, type:

```bash
dvc push
```

## Auto-generate API documentation

To auto-generate API document for your project, run:

```bash
make docs
```

"# MLOPS_ASSIGNMENT_GROUP2_TEAM6"

## Run Application on Local Server

```
python main.py

```

A readme file for the deployment guide & folder structure and an URL to the
web app

## Deployment Configuration with Render

Link: https://dashboard.render.com/

Step 1: Set up requirements.txt file to install necessary libraries

```bash
pip freeze >> requirements.txt / manually Configure

```

Step 2: Sign up / Login with GitHub

Step 3: Select Deploy with Web Service

Step 4: Choose Github Repository for deployment.

Step 5: Configure deployment setup

**General Coniguration**

```bash
Name = MLOPS_ZX_PK
```

**Build & Deploy**

```bash
Repository: https://github.com/ZXiang1121/MLOPS_ASSIGNMENT_GROUP2_TEAM6

Branch: main

Root Directory (optional): app

Build Command: pip install -r requirements.txt

Start Command: gunicorn main:app

Auto-Deploy: No

```

**Configure Environment (Important)**
Key Value

```bash
PYTHON_VERSION = 3.9.7
```

Step 6: Hover over "Manual Deploy" button & select "Deploy latest commit"

## Folder Structure

```Bash
C:.
│   .gitignore
│   .pre-commit-config.yaml
│   logs.log
│   Makefile
│   poetry.lock
│   pyproject.toml
│   README.md
│
├───.dvc
│   │   .gitignore
│   │   config
│   │
│   ├───cache
│   │   └───files
│   │       └───md5
│   │           ├───b6
│   │           │       b21f73e29aee0a406900932f1ebe3e
│   │           │
│   │           └───fe
│   │                   05fad3c483a3f1381de3d20726fef2
│   │
│   └───tmp
│           lock
│           rwlock
│           rwlock.lock
│
├───app
│   │   build.sh
│   │   Dockerfile
│   │   logs.log
│   │   main.py
│   │   requirements.txt
│   │
│   ├───models
│   │       hdb_best_tuned_model.pkl
│   │       medical_best_tuned_model.pkl
│   │
│   ├───None
│   │   └───joblib
│   │       └───pycaret
│   │           └───internal
│   │               └───pipeline
│   │                   ├───_full_transform
│   │                   │   │   func_code.py
│   │                   │   │
│   │                   │   ├───90b78754442cfc9dd0768f331acd907b
│   │                   │   │       metadata.json
│   │                   │   │       output.pkl
│   │                   │   │
│   │                   │   └───d692db623b332ef1060ba096f870c6ae
│   │                   │           metadata.json
│   │                   │           output.pkl
│   │                   │
│   │                   └───_transform_one
│   │                           func_code.py
│   │
│   ├───static
│   │   ├───images
│   │   │       Medical Background.jpg
│   │   │       medical.jpg
│   │   │
│   │   ├───js
│   │   │       script.js
│   │   │
│   │   └───styles
│   │           style.css
│   │
│   └───templates
│       │   base.html
│       │   home.html
│       │   medical_predict.html
│       │   medical_result.html
│       │   parik_hdb.html
│       │   submit.html
│       │
│       ├───includes
│       │       _formHelper.html
│       │
│       └───navbar
│               userNavbar.html
│   │
│   ├───static
│   │   ├───images
│   │   │       Medical Background.jpg
│   │   │       medical.jpg
│   │   │
│   │   ├───js
│   │   │       script.js
│   │   │
│   │   └───styles
│   │           style.css
│   │
│   └───templates
│       │   base.html
│       │   home.html
│       │   medical_predict.html
│       │   medical_result.html
│       │   parik_hdb.html
│       │   submit.html
│       │
│       ├───includes
│       │       _formHelper.html
│       │
│       └───navbar
│               userNavbar.html
│
├───config
│   │   hdb_pre_processing.yaml
│   │   main.yaml
│   │   medical_pre_processing.yaml
│   │
│   ├───model
│   │       model1.yaml
│   │       model2.yaml
│   │
│   └───process
│           process1.yaml
│           process2.yaml
│
├───data
│   ├───final
│   │       .gitkeep
│   │
│   ├───processed
│   │       02_medical_records_processed.csv
│   │
│   └───raw
│           .gitignore
│           .gitkeep
│           01_hdb_resale_transactions.csv
│           01_hdb_resale_transactions.csv.dvc
│           02_medical_records.csv
│           02_medical_records.csv.dvc
│
├───docs
│       .gitkeep
│
├───models
│       .gitkeep
│
├───notebooks
│   │   .gitkeep
│   │
│   ├───HDB
│   │   │   hdb_modelling.ipynb
│   │   │
│   │   ├───mlruns
│   │   │   ├───0
│   │   │   │       meta.yaml
│   │   │   │
│   │   │   ├───1
│   │   │   │   │   meta.yaml
│   │   │   │   │
│   │   │   │   ├───0478e7d3d8e54dfe8684781fcf6171a5
│   │   │   │   │   │   meta.yaml
│   │   │   │   │   │
│   │   │   │   │   ├───artifacts
│   │   │   │   │   │   │   Holdout.html
│   │   │   │   │   │   │   Results.html
│   │   │   │   │   │   │
│   │   │   │   │   │   └───model
│   │   │   │   │   │           conda.yaml
│   │   │   │   │   │           MLmodel
│   │   │   │   │   │           model.pkl
│   │   │   │   │   │           python_env.yaml
│   │   │   │   │   │           requirements.txt
│   │   │   │   │   │
│   └───Medical
│       │   logs.log
│       │   Medical_Prediction.ipynb
│       │
│       ├───.ipynb_checkpoints
│       │       Medical_Prediction-checkpoint.ipynb
│       │
│       ├───catboost_info
│       │   │   catboost_training.json
│       │   │   learn_error.tsv
│       │   │   time_left.tsv
│       │   │
│       │   ├───learn
│       │   │       events.out.tfevents
│       │   │
│       │   └───tmp
│       ├───mlruns
│       │   ├───.trash
│       │   ├───0
│       │   │       meta.yaml
│       │   │
│       │   ├───418952812343069946
│       │   │   │   meta.yaml
│       │   │   │
│       │   │   ├───0169246931da49e085b5743ef7a5736a
│       │   │   │   │   meta.yaml
│       │   │   │   │
│       │   │   │   ├───artifacts
│       │   │   │   │   │   Results.html
│       │   │   │   │   │
│       │   │   │   │   └───model
│       │   │   │   │           conda.yaml
│       │   │   │   │           MLmodel
│       │   │   │   │           model.pkl
│       │   │   │   │           python_env.yaml
│       │   │   │   │           requirements.txt
│       │   │   │   │
│       │   │   │   ├───metrics
│       │   │   │   │       Accuracy
│       │   │   │   │       AUC
│       │   │   │   │       F1
│       │   │   │   │       Kappa
│       │   │   │   │       MCC
│       │   │   │   │       Prec
│       │   │   │   │       Recall
│       │   │   │   │       TT
│       │   │   │   │
│       │   │   │   ├───params
│       │   │   │   │       boosting_type
│       │   │   │   │       class_weight
│       │   │   │   │       colsample_bytree
│       │   │   │   │       importance_type
│       │   │   │   │       learning_rate
│       │   │   │   │       max_depth
│       │   │   │   │       min_child_samples
│       │   │   │   │       min_child_weight
│       │   │   │   │       min_split_gain
│       │   │   │   │       num_leaves
│       │   │   │   │       n_estimators
│       │   │   │   │       n_jobs
│       │   │   │   │       objective
│       │   │   │   │       random_state
│       │   │   │   │       reg_alpha
│       │   │   │   │       reg_lambda
│       │   │   │   │       subsample
│       │   │   │   │       subsample_for_bin
│       │   │   │   │       subsample_freq
│       │   │   │   │
│       │   │   │   └───tags
│       │   │   │           mlflow.log-model.history
│       │   │   │           mlflow.parentRunId
│       │   │   │           mlflow.runName
│       │   │   │           mlflow.source.name
│       │   │   │           mlflow.source.type
│       │   │   │           mlflow.user
│       │   │   │           Run ID
│       │   │   │           Run Time
│       │   │   │           Source
│       │   │   │           URI
│       │   │   │           USI
│
├───src
│       process.py
│       train_model.py
│       __init__.py
│
└───tests
        test_process.py
        test_train_model.py
        __init__.py
```

## Deployed URL to Website

May take awhile to load into the webpage, as we are using a free hosting server.

- Homepage URL: https://mlops-pk-zx.onrender.com

- HDB Prediction URL: https://mlops-pk-zx.onrender.com/parik

- Medical Prediction(Cardiovascular) URL: https://mlops-pk-zx.onrender.com/medical_predict

