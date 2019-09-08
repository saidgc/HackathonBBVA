
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import time
from flask import Flask, jsonify, request
app = Flask(__name__)


mlp = None
scaler = None

tags = ["Not authorized", "Authorized"]

def evaluate_clasifier(data_classifier, test_data, test_labels):
    prediction = data_classifier.predict(test_data)
    CM = confusion_matrix(test_labels, prediction)
    return CM


@app.route('/<saldo>')
def predecir(saldo):
    global mlp, scaler
    print(type(saldo))
    testeo = scaler.transform(
        [[2, 11000, 6131969, 4, 1, 1, 1311984, -1, -1, -1, 0, 0.0, 0, 0, 1, 0, 0, 0, float(saldo), 0, 0, 0, 0]])[0]

    print(mlp.predict([testeo]))

    return tags[(int(str(mlp.predict([testeo])).replace(']','').replace('[','')))]


if __name__ == "__main__":
    scaler = StandardScaler()
    X = pd.read_csv('dataset.csv')
    y = pd.read_csv('tags.csv')

    train_data, test_data, train_labels, test_labels = train_test_split(
        X, y, test_size=0.3, random_state=42)

    scaler.fit(train_data)

    train_data = scaler.transform(train_data)
    test_data = scaler.transform(test_data)

    mlp = MLPClassifier(hidden_layer_sizes=(30, 30, 30))
    mlp.fit(train_data, train_labels.values.ravel())

    predictions = mlp.predict(train_data)

    confusionmatrix = evaluate_clasifier(mlp, test_data, np.array(test_labels))
    score = confusionmatrix.diagonal().sum() * 100. / confusionmatrix.sum()

    print("Accuracy", score)

    app.run()
        # En esta seccion hay que esperar a que manden datos para evaluar
