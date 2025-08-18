import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import argparse

def main(data_path, model_path):
    # Load dataset
    df = pd.read_csv(data_path)
    X = df.drop("class", axis=1)
    y = df["class"]

    # Load model
    clf = joblib.load(model_path)

    # Predictions
    y_pred = clf.predict(X)

    # Evaluation
    print("📊 Confusion Matrix:\n", confusion_matrix(y, y_pred))
    print("\n📈 Classification Report:\n", classification_report(y, y_pred))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to CSV dataset")
    parser.add_argument("--model", default="models/best_model.joblib", help="Path to model")
    args = parser.parse_args()
    main(args.data, args.model)
