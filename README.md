# Building a minimal Flask based prediction API

So, you finished training your model.
Congratulations!
Now, it is time to expose it to the world (or at least to your peers).
A standard way would be to build a RESTful API; to that end [Flask](http://flask.pocoo.org/) is probably a natural choice.
In this repository, we:

1. Fetch titanic survival data
2. Train a model out of it
3. Persist the model into a Python [pickle](https://docs.python.org/3/library/pickle.html)
4. Build an app which accepts JSON and returns predictions

In reality, it is likely you will need to split this example into three components:
1. *Model training* and persisting/pickling
2. Trained model *storage* (e.g. on S3)
3. *Prediction app* which will load the trained model and provide prediction based on requests

# How to try out this?

## Virtual environment

For your own safety, make sure you work with this example inside a virtual environment.
Simple way to do so is `conda create -n try-out-prediction-app python=3.6` if you're using `conda`.
In the virtual environment, install the requirements: `pip install -r requirements.txt`

## Prepare data and train model

To make life easy, simply run `make train`.

## Run the app

### Local and naive

First, from the root of the project run `python src/app.py`.
You are expecting the following: `* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)`.
If you install `httpie`, you could now easily try out the app.
In another terminal, you can now ask the app for predictions on the test set: `http POST http://0.0.0.0:5000/predict < data/test.json`.
That's it.

### Using docker

You can also use the provided `Dockerfile`. First, build the image:

```bash
docker build -t pm_api .
```

Once built, you can start a container running the image.
It is important to forward the port `5000` from the container to the host; use the `-p` parameter to do so:

```bash
docker run -p 5000:5000 pm_api
```

Once, running, you can send requests using the same line as above (used for the local example).

# Remarks

- I used the skeleton provided by [Amir Ziai](https://medium.com/@amirziai/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa)
- To have a consistent way of training and predicting, I use the tools from [ds-pub-utils](https://github.com/drorata/ds-pub-utils).
  This allows fitting the model on the training set (including with regards to the data preprocessing).
