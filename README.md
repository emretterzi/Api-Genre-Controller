# Genre Prediction API

This repository contains a Flask-based API for predicting the genre of a song based on its lyrics. The API utilizes a pre-trained machine learning model to perform genre predictions.

## Features

- **Predict Genre**: Send a POST request with song lyrics, and receive a predicted genre in response.
- **Pre-trained Model**: The API uses a pre-trained model to provide quick and accurate genre predictions.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.6 or later
- Flask
- joblib

You can install the required Python packages using `pip`:

```sh
pip install Flask joblib
```

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/genre-prediction-api.git
cd genre-prediction-api
```

2. Place your trained model file (`trained_model.joblib`) in the project directory. Ensure the model file path in the code matches the location where you place your model.

### Usage

1. Run the Flask application:

```sh
python app.py
```

2. The API will be accessible at `http://127.0.0.1:5000`.

### API Endpoint

#### Predict Genre

- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**: JSON object containing the song lyrics.
  
  ```json
  {
    "lyrics": "Your song lyrics here"
  }
  ```

- **Response**: JSON object containing the predicted genre.

  ```json
  {
    "predicted_genre": "The predicted genre"
  }
  ```

### Example Request

Use `curl` or any HTTP client to send a POST request to the API:

```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"lyrics": "your song lyrics here"}'
```

### Example Response

```json
{
  "predicted_genre": "The predicted genre"
}
```

### Error Handling

- If the lyrics are not provided in the request, the API responds with a `400 Bad Request` status and an error message:

  ```json
  {
    "error": "Lyrics not provided"
  }
  ```

- If the model file is not found, the API responds with a `500 Internal Server Error` status and an error message:

  ```json
  {
    "error": "Model file not found. Make sure to train the model first."
  }
  ```

## Model Training

To train your own model, you need to prepare a dataset of song lyrics with their corresponding genres. You can use various machine learning libraries such as scikit-learn to train your model and save it using `joblib`. Ensure the saved model is named `trained_model.joblib` and placed in the project directory.



## Screenshots

<img width="411" alt="image" src="https://github.com/emretterzi/Api-Genre-Controller/assets/56559417/bf7d2adf-760e-41e6-860c-1ffa87bc19f8">





