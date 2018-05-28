# xebia_mower_market
This project is aimed at fulfilling the datascience exercice provided by Xebia 

## Using the repository
*To build the docker type from within the repository :

```
docker build -t mower_market:dev:dev -f Dockerfile.dev .
```

*Once built use to start the docker as in stance for Jyputer :

```
docker run -it -p 8889:8888 -p 5000:5000 -p 6006:6006 --rm -v //c/Users/thilegall/Desktop/Projets/Xebia/mower_market:/root mower_market:dev jupyter notebook --allow-root
```

*Finally, you can access your Jupyter notebook at (in any browser) :

```
localhost:8889
```

## Architecture

#Filesystem |(dockerfilesystem)

```
(/root)
    |-mower_mark
               |
               |-API    -> File containing a set of function for datascience purpose
                   |-crunching.py           -> data crunching functions
                   |-features.py            -> feature_engineering functions
                   |-finalistaion.py        -> specific function linked to a project (fitting stastical distibution, etc...)
                   |-model_application.py   -> functions that apply the selected model
                   |-model_testing.py       -> functions used to tes, evaluate and register models
               |-data     -> File containing the data regarding the project
                   |-crunching              -> scripts for data crunching (empty)
                   |-DF                     -> output data
                   |-features               -> scripts for feature engineering (empty)
                   |-finalisation           -> scripts for finalisation (empty)
                   |-model                  -> models
                   |-mower_market_datasets  -> input data
                   |-ref                    -> File containing a reference table with the model and their metadata (performance, associated scripts, etc...) (empty)
                   |-scaler                 -> scaler of the data (if the model is not a scikitlearn model purpose) (empty)
               |-LOG      -> File where the logs will be written
               |-notebook -> File containing the notebooks
                        |-data_explo.ipnb -> the exploration and cleaning notebook
                        |-tests_scripts_crunching.ipnb -> test of crunching fucntion called as API + data modelling
                        |-test_main.ipnb -> tests of the main function to call it as a script
               |-source   -> File containing the script rnning the project
                      |-main.py -> script used to run the main
               |-utils    -> File containing utility functions (empty)
```
