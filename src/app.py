from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd
import train_model as tm
import logging
import time

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Prediction end point

    Post a JSON holding the features and expect a prediction

    Returns
    -------
    JSON
        The field `predictions` will hold a list of 0 and 1's corresponding
        to the predictions.
    """
    logger.info('Starting prediction')
    json_ = request.get_json()

    query_df = pd.DataFrame(json_)

    query = tm.prepare_data(query_df, train=False)

    prediction = clf.predict(query)
    prediction = [int(x) for x in prediction]

    logger.info("Prediction is ready")
    return jsonify({'prediction': prediction})


@app.route('/minimal_test', methods=['POST'])
def minimal_test():
    """
    Test end point

    You can use this end point to simply try out Flask.
    Run the app using `python app.py` and then either post a
    JSON `{"x": 3, "y": 4}` and expect to get the answer 7.
    Or, when using `httpie`, you can simply call
    `http POST http://127.0.0.1:8080/minimal_test x=3 y=4`.

    Returns
    -------
    JSON
        Containing a single field `prediction` holding the sum of the input
    """
    json_ = request.get_json()
    x = json_['x']
    y = json_['y']
    prediction = int(x) + int(y)
    return jsonify({'prediction': prediction})


@app.route('/sleep', methods=['POST'])
def my_sleep():
    json_ = request.get_json()
    n = json_['n']
    logger.info(f"Started SLEEP with '{n}' seconds")
    time.sleep(n)
    logger.info(f"Finished SLEEP with '{n}' seconds")
    return jsonify({'Success': "YAY"})


if __name__ == '__main__':
    clf = joblib.load('pipeline.pkl')
    app.run(debug=True, host='0.0.0.0')
