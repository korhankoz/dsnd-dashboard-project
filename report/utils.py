import pickle
from pathlib import Path

# Root of the project (two levels up from report/)
project_root = Path(__file__).parent.parent.resolve()

# Path to the model file
model_path = project_root / "assets" / "model.pkl"

def load_model():
    with model_path.open('rb') as file:
        model = pickle.load(file)
    return model