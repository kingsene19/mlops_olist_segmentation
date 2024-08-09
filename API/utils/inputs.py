"""Module pour le format de données attendu par l'API"""

from pydantic import BaseModel
import pandas as pd


class Customer(BaseModel):
    customer_unique_id: str
    total_spent: float
    frequency: float
    avg_installments: float
    total_items: float
    payment_price_ratio: float
    recency: float
    avg_fractional_payment_ratio: float
    total_freight_value: float

    def to_df(self):
        data = {
            "total_spent": [self.total_spent],
            "frequency": [self.frequency],
            "avg_installments": [self.avg_installments],
            "total_items": [self.total_items],
            "payment_price_ratio": [self.payment_price_ratio],
            "recency": [self.recency],
            "avg_fractional_payment_ratio": [self.avg_fractional_payment_ratio],
            "total_freight_value": [self.total_freight_value],
        }
        return pd.DataFrame(data)
