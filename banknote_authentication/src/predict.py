import joblib
import argparse

def main(model_path, variance, skewness, curtosis, entropy):
    # Load model
    clf = joblib.load(model_path)

    # Prediction
    features = [[variance, skewness, curtosis, entropy]]
    prediction = clf.predict(features)[0]

    result = "🟢 Genuine Banknote" if prediction == 0 else "🔴 Fake Banknote"
    print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="models/best_model.joblib", help="Path to model")
    parser.add_argument("--variance", type=float, required=True)
    parser.add_argument("--skewness", type=float, required=True)
    parser.add_argument("--curtosis", type=float, required=True)
    parser.add_argument("--entropy", type=float, required=True)
    args = parser.parse_args()
    main(args.model, args.variance, args.skewness, args.curtosis, args.entropy)
