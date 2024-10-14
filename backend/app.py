from fastapi import FastAPI
from models import lstm_model, transformer_model, ensemble_model, quantum_model
from utils.data_loader import load_tesla_data
from utils.rag_engine import get_llm_augmented_prediction
from utils.causal_inference_engine import run_causal_inference
from utils.security_manager import secure_request

app = FastAPI()

# Load the Tesla stock dataset
tesla_data = load_tesla_data()

@app.get("/")
def read_root():
    return {"message": "Tesla Stock Prediction API with LLM-augmented RAG and Causal Inference"}

@app.get("/predict/{model_type}")
def get_prediction(model_type: str):
    secure_request()

    # Model predictions based on the user's selection
    if model_type == "lstm":
        prediction = lstm_model.predict(tesla_data)
    elif model_type == "transformer":
        prediction = transformer_model.predict(tesla_data)
    elif model_type == "ensemble":
        prediction = ensemble_model.predict(tesla_data)
    elif model_type == "quantum":
        prediction = quantum_model.predict(tesla_data)
    else:
        return {"error": "Model type not supported"}

    # Run causal inference on the predictions
    causal_effects = run_causal_inference(tesla_data, prediction)

    # Augment predictions with LLM insights using the RAG system
    augmented_response = get_llm_augmented_prediction(prediction, tesla_data)

    return {
        "prediction": augmented_response,
        "causal_inference": causal_effects
    }
