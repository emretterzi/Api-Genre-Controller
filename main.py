from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict_genre():
    # İstekten veriyi al
    data = request.json

    # Şarkı sözlerini al
    new_lyric = data.get('lyrics', None)

    if new_lyric is None:
        return jsonify({'error': 'Lyrics not provided'}), 400

    # Eğitilmiş modeli yükle
    model_filename = "/Users/emreterzi/PycharmProjects/Api-Genre-Controller/trained_model.joblib"
    try:
        grid_search = joblib.load(model_filename)
        print("Pre-trained model loaded successfully.")
    except FileNotFoundError:
        return jsonify({'error': 'Model file not found. Make sure to train the model first.'}), 500

    # Tahmin yap
    predicted_type = grid_search.predict([new_lyric])[0]

    return jsonify({'predicted_genre': predicted_type}), 200


if __name__ == '__main__':
    app.run(debug=True)
