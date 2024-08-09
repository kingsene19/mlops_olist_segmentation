"""Module pour le chargement de jeu de données"""

import pandas as pd
from loguru import logger


def load_data(path: str) -> pd.DataFrame:
    """Charger le jeu de données à partir du fichier

    Args:
       path (str): Chemin du fichier à charger


    Returns:
       pd.Dataframe : Dataframe contentant les données chargées du fichier
    """
    logger.info(f"Dataset path to load {path}")
    if not path:
        logger.error("ValueError, path invalide")
        raise ValueError("Path est requis")
    if path:
        try:
            data = pd.read_csv(path)
        except FileNotFoundError as e:
            logger.error(f"Le chargement des données à échouer avec l'erreur {e}")
        else:
            logger.info(f"Data shape: {data.shape}")
            print(data.head(10))
            return data


def make_stability_dataset(path: str, period: int) -> pd.DataFrame:
    """Filtrage du jeu de de données sur une période spécifiée

    Args:
        path (str) : chemin vers le fichier à charger
        period (int) : incrément de la période en mois

    Returns:
        pd.DataFrame : DataFrame contenant les données filtrés sur la période specifiée
    """
    if not path or not period:
        logger.error("ValueError, path ou period non spécifié")
        raise ValueError("path et period sont requis")
    else:
        try:
            data = pd.read_csv(path)
        except FileNotFoundError as e:
            logger.error(f"Le chargement des données à échouer avec l'erreur {e}")
        else:
            # Filtrage sur la période
            data["order_purchase_timestamp"] = pd.to_datetime(
                data["order_purchase_timestamp"]
            )

            start = data["order_purchase_timestamp"].min()
            stop = start + pd.DateOffset(months=period)

            filtered_data = data[
                (data["order_purchase_timestamp"] >= start)
                & (data["order_purchase_timestamp"] < stop)
            ]

            # Feature Engineering
            total_spent = (
                filtered_data.groupby("customer_unique_id")["price"].sum().reset_index()
            )
            total_spent.columns = ["customer_unique_id", "total_spent"]
            frequency = (
                filtered_data.groupby("customer_unique_id")["order_id"]
                .count()
                .reset_index()
            )
            frequency = frequency.rename({"order_id": "frequency"}, axis=1)
            avg_installments = (
                filtered_data.groupby("customer_unique_id")["payment_installments"]
                .mean()
                .reset_index()
            )
            avg_installments.columns = ["customer_unique_id", "avg_installments"]
            total_items = (
                filtered_data.groupby("customer_unique_id")["order_item_id"]
                .sum()
                .reset_index()
            )
            total_items.columns = ["customer_unique_id", "total_items"]
            payment_price_ratio = (
                filtered_data.groupby("customer_unique_id")["payment_value"].sum()
                / filtered_data.groupby("customer_unique_id")["price"].sum()
            )
            payment_price_ratio = payment_price_ratio.reset_index()
            payment_price_ratio.columns = ["customer_unique_id", "payment_price_ratio"]
            last_order = (
                filtered_data.groupby("customer_unique_id")["order_purchase_timestamp"]
                .max()
                .reset_index()
            )
            last_order.columns = ["customer_unique_id", "last_order"]
            last_order["recency"] = (
                last_order["last_order"].max() - last_order["last_order"]
            ).dt.days
            avg_fractional_payment_ratio = (
                filtered_data.groupby("customer_unique_id")[
                    "payment_installments"
                ].mean()
                / filtered_data.groupby("customer_unique_id")["payment_value"].sum()
            )
            avg_fractional_payment_ratio = avg_fractional_payment_ratio.reset_index()
            avg_fractional_payment_ratio.columns = [
                "customer_unique_id",
                "avg_fractional_payment_ratio",
            ]
            total_freight_value = (
                filtered_data.groupby("customer_unique_id")["freight_value"]
                .sum()
                .reset_index()
            )
            total_freight_value.columns = ["customer_unique_id", "total_freight_value"]

            df_features = pd.merge(
                total_spent,
                frequency[["customer_unique_id", "frequency"]],
                on="customer_unique_id",
                how="left",
            )
            df_features = pd.merge(
                df_features, avg_installments, on="customer_unique_id", how="left"
            )
            df_features = pd.merge(
                df_features, total_items, on="customer_unique_id", how="left"
            )
            df_features = pd.merge(
                df_features, payment_price_ratio, on="customer_unique_id", how="left"
            )
            df_features = pd.merge(
                df_features,
                last_order[["customer_unique_id", "recency"]],
                on="customer_unique_id",
                how="left",
            )
            df_features = pd.merge(
                df_features,
                avg_fractional_payment_ratio,
                on="customer_unique_id",
                how="left",
            )
            df_features = pd.merge(
                df_features, total_freight_value, on="customer_unique_id", how="left"
            )

            df_features.drop("customer_unique_id", axis=1, inplace=True)

            logger.info(f"Data shape: {df_features.shape}")

            return df_features
