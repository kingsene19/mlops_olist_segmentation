from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils.strategies import STRATEGIES
from utils.loaders import load_data, load_model
from utils.inputs import Customer
from starlette.responses import JSONResponse
import pandas as pd
from io import BytesIO

app = FastAPI(
    title="Olist Segmentation API",
    description="API for Olist segmentation use cases",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Chargement du modèle et du jeu de données utilisateurs
model = load_model()
data = load_data()


@app.post("/api/segment")
def predict_customer_segment(customer: Customer) -> JSONResponse:
    """Effectuer une prédiction pour un client

    Args:
        customer (Customer) : Informations relatifs au client

    Returns:
        JSONResponse : Réponse contenant l'id du client et le segment prédit
    """
    try:
        result = model.predict(customer.to_df())[0]
        # Renvoyer le resultat
        return JSONResponse(
            content={
                "customer_unique_id": customer.customer_unique_id,
                "segment": STRATEGIES[result],
            }
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/segment/batch")
def predict_customer_segment_batch(file: UploadFile = File(...)) -> JSONResponse:
    """Effectuer une prédiction en lot pour plusieurs clients via un fichier CSV ou XLSX

    Args:
        file (UploadFile) : Fichier contenant les informations des clients (CSV ou XLSX)

    Returns:
        JSONResponse : Réponse contenant une liste d'id du client et du segment prédit
    """
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(
            status_code=400, detail="Le fichier doit être au format CSV ou XLSX"
        )

    try:
        # Load file into DataFrame
        if file.filename.endswith(".csv"):
            df = pd.read_csv(BytesIO(file.file.read()))
        elif file.filename.endswith(".xlsx"):
            df = pd.read_excel(BytesIO(file.file.read()))

        results = []

        for _, row in df.iterrows():
            entry = row.drop("customer_unique_id")
            result = model.predict(entry.to_frame().T)[0]
            results.append(
                {
                    "customer_unique_id": row["customer_unique_id"],
                    "segment": STRATEGIES[result],
                }
            )
        return JSONResponse(content=results)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/segment/{customer_unique_id}")
def retrieve_customer_segment(customer_unique_id: str) -> JSONResponse:
    """Récupérer le segment prédit pour un client par son id

    Args:
        customer_unique_id (str) : ID du client

    Returns:
        JSONResponse : Réponse contenant une list d'id du client et son segment prédit
    """
    try:
        row = data[data["customer_unique_id"] == customer_unique_id]
        return JSONResponse(
            content={
                "customer_unique_id": customer_unique_id,
                "segment": STRATEGIES[row.iloc[0].segments],
            }
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/segments")
def retrieve_all_segments() -> JSONResponse:
    """Récupérer l'ensemble des segments

    Returns:
        JSONResponse : Réponse contenant une list d'id du client et son segment prédit
    """
    results = []
    try:
        segments = STRATEGIES.keys()
        for segment in segments:
            temp = data[data["segments"] == segment]
            customer_unique_ids = temp["customer_unique_id"].tolist()
            results.append(
                {"Segment": STRATEGIES[segment], "Customers": customer_unique_ids}
            )
        return JSONResponse(content=results)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
