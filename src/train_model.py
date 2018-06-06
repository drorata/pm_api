"""
Train a pipeline using training data Furthermore, implements a
data preparation utility
"""

import pandas as pd
from pubdsutils import preprocessing as pr
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def prepare_data(df, train=True):
    """
    Super basic data preparation
    """
    logger.info('Preparing data')
    df = df.copy()
    df.Age.fillna(0, inplace=True)
    df.Sex.fillna('-1', inplace=True)
    df.Embarked.fillna('NA', inplace=True)
    if train:
        logger.info("Returning data (train mode)")
        return df[['Age', 'Sex', 'Embarked', 'Survived']]
    else:
        logger.info("Returning data (non-train mode)")
        return df[['Age', 'Sex', 'Embarked']]


df = pd.read_csv('./data/train.csv')
df = prepare_data(df)

pipeline = make_pipeline(
    pr.LabelEncodingColoumns(cols=['Sex', 'Embarked']),
    pr.ColumnsOneHotEncoder(cols=['Sex'], n_values=2),
    pr.ColumnsOneHotEncoder(['Embarked'], n_values=4),
    RandomForestClassifier()
)

features = ['Age', 'Sex', 'Embarked']
target = 'Survived'

pipeline.fit(df[features], df[target])
joblib.dump(pipeline, 'pipeline.pkl')
