import pandas as pd

"""
Simply convert the test data given as CSV to JSON

The JSON format will be used when asking for predictions from the Flask app
"""

df = pd.read_csv('./data/test.csv')
df.to_json('./data/test.json')
