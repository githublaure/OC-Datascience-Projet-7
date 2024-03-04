import mlflow
from mlflow import sklearn
l

with mlflow.start_run():
    model.fit(X_train, y_train)
    mlflow.log_param("model", "LogisticRegression")
    log_model(model, "model")
