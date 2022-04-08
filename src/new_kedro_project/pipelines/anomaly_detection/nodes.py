"""
This is a boilerplate pipeline 'anomaly_detection'
generated using Kedro 0.17.7
"""
import numpy as np

from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

def get_rid_of_anomalies_unsupervised(x: np.ndarray, y: np.ndarray, anomaly_detector = "IsolationForest") -> [np.ndarray, np.ndarray]:

    print('get_rid_of_anomalies')

    if anomaly_detector == "IsolationForest":
        model = IsolationForest()

    if anomaly_detector == "EllipticEnvelope":
        model = EllipticEnvelope()

    if anomaly_detector == "OneClassSVM":
        model = OneClassSVM()

    if anomaly_detector == "LocalOutlierFactor":
        model = LocalOutlierFactor(novelty=True)



    model.fit(x)
    ad_labels = model.predict(x)

    x = x[np.where(ad_labels == 1)[0]]
    y = y[np.where(ad_labels == 1)[0]]

    print(x.shape, y.shape)

    return x, y