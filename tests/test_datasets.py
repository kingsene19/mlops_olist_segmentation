"""Test sur les jeux de données"""

from pathlib import Path
import sys
import os

sys.path.append(str(Path.cwd()))
from src.load_dataset import load_data

# --------------------------- Variables utilses --------------------------- #
parent_path = Path.cwd()
target_dir = os.path.join(parent_path, "olist_dataset")


# --------------------------- Vérification des fichiers --------------------------- #
def test_all_files_used_are_present():
    """
    Test pour vérifier que tous les jeux de données utilisés dans les notebooks sont présents
    """
    all_files_used = [
        "olist_customers_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_products_dataset.csv",
        "olist_sellers_dataset.csv",
        "product_category_name_translation.csv",
    ]
    assert os.path.isdir(target_dir), f"Directory {target_dir} does not exist."
    files_in_dir = os.listdir(target_dir)
    for file in all_files_used:
        assert (
            file in files_in_dir
        ), f"File {file} is missing in the directory {target_dir}."


# ---------------------------  Vérification sur les jeux de données --------------------------- #
customers_df = load_data(os.path.join(target_dir, "olist_customers_dataset.csv"))
order_items_df = load_data(os.path.join(target_dir, "olist_order_items_dataset.csv"))
order_payments_df = load_data(
    os.path.join(target_dir, "olist_order_payments_dataset.csv")
)
orders_df = load_data(os.path.join(target_dir, "olist_orders_dataset.csv"))
products_df = load_data(os.path.join(target_dir, "olist_products_dataset.csv"))
sellers_df = load_data(os.path.join(target_dir, "olist_sellers_dataset.csv"))
product_category_df = load_data(
    os.path.join(target_dir, "product_category_name_translation.csv")
)


def test_dropped_columns_found():
    """
    Test pour vérifier que toutes les colonnes qui ont été drop lors du cleaning sont présentes
    """
    assert (
        "shipping_limit_date" in order_items_df.columns
    ), "Expected columns not found in order_items: shipping_limit_date"
    expected_columns = [
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    missing_columns = [col for col in expected_columns if col not in orders_df.columns]
    assert (
        not missing_columns
    ), f"Expected columns not found in orders: {missing_columns}"
    expected_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]
    missing_columns = [
        col for col in expected_columns if col not in products_df.columns
    ]
    assert (
        not missing_columns
    ), f"Expected columns not found in products: {missing_columns}"


def test_used_columns_found():
    """
    Test pour vérifier que toutes les colonnes utilisées lors de l'EDA sont présentes
    """
    used_columns = [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp",
        "order_item_id",
        "product_id",
        "seller_id",
        "price",
        "freight_value",
        "payment_sequential",
        "payment_type",
        "payment_installments",
        "payment_value",
        "product_category_name",
        "customer_unique_id",
        "customer_zip_code_prefix",
        "customer_city",
        "customer_state",
        "seller_zip_code_prefix",
        "seller_city",
        "seller_state",
    ]
    merged_df = orders_df.merge(order_items_df, on="order_id", how="left")
    merged_df = merged_df.merge(order_payments_df, on="order_id", how="outer")
    merged_df = merged_df.merge(products_df, on="product_id", how="outer")
    merged_df = merged_df.merge(customers_df, on="customer_id", how="outer")
    merged_df = merged_df.merge(sellers_df, on="seller_id", how="outer")
    missing_columns = [col for col in used_columns if col not in merged_df.columns]
    assert (
        not missing_columns
    ), f"Expected columns not found in orders: {missing_columns}"


def test_orders_dtypes():
    """
    Test sur le jeu de données 'olist_orders_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_orders, ncols_orders = orders_df.shape
    assert (
        nrows_orders >= 99441
    ), f"Expected at least 99441 rows, but got {nrows_orders}"
    assert ncols_orders == 8, f"Expected 8 columns, but got {ncols_orders}"
    assert (
        orders_df["order_id"].dtype == "object"
    ), "Data types incorrect pour 'order_id'"
    assert (
        orders_df["customer_id"].dtype == "object"
    ), "Data types incorrect pour 'customer_id'"
    assert (
        orders_df["order_status"].dtype == "object"
    ), "Data types incorrect pour 'order_status'"
    assert (
        orders_df["order_purchase_timestamp"].dtype == "object"
    ), "Data types incorrect pour 'order_purchase_timestamp'"
    assert (
        orders_df["order_approved_at"].dtype == "object"
    ), "Data types incorrect pour 'order_approved_at'"
    assert (
        orders_df["order_delivered_carrier_date"].dtype == "object"
    ), "Data types incorrect pour 'order_delivered_carrier_date'"
    assert (
        orders_df["order_delivered_customer_date"].dtype == "object"
    ), "Data types incorrect pour 'order_delivered_customer_date'"
    assert (
        orders_df["order_estimated_delivery_date"].dtype == "object"
    ), "Data types incorrect pour 'order_estimated_delivery_date'"


def test_order_payments_dtypes():
    """
    Test sur le jeu de données 'olist_order_payments_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_order_payments, ncols_order_payments = order_payments_df.shape
    assert (
        nrows_order_payments >= 103886
    ), f"Expected at least 103886 rows, but got {nrows_order_payments}"
    assert (
        ncols_order_payments == 5
    ), f"Expected 5 columns, but got {ncols_order_payments}"
    assert (
        order_payments_df["order_id"].dtype == "object"
    ), "Data types incorrect pour 'order_id'"
    assert (
        order_payments_df["payment_sequential"].dtype == "int64"
    ), "Data types incorrect pour 'payment_sequential'"
    assert (
        order_payments_df["payment_type"].dtype == "object"
    ), "Data types incorrect pour 'payment_type'"
    assert (
        order_payments_df["payment_installments"].dtype == "int64"
    ), "Data types incorrect pour 'payment_installments'"
    assert (
        order_payments_df["payment_value"].dtype == "float64"
    ), "Data types incorrect pour 'payment_value'"


def test_products_dtypes():
    """
    Test sur le jeu de données 'olist_products_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_products, ncols_products = products_df.shape
    assert (
        nrows_products >= 32951
    ), f"Expected at least 32951 rows, but got {nrows_products}"
    assert ncols_products == 9, f"Expected 9 columns, but got {ncols_products}"
    assert (
        products_df["product_id"].dtype == "object"
    ), "Data types incorrect pour 'product_id'"
    assert (
        products_df["product_category_name"].dtype == "object"
    ), "Data types incorrect pour 'product_category_name'"
    assert (
        products_df["product_name_lenght"].dtype == "float64"
    ), "Data types incorrect pour 'product_name_lenght'"
    assert (
        products_df["product_description_lenght"].dtype == "float64"
    ), "Data types incorrect pour 'product_description_lenght'"
    assert (
        products_df["product_photos_qty"].dtype == "float64"
    ), "Data types incorrect pour 'product_photos_qty'"
    assert (
        products_df["product_weight_g"].dtype == "float64"
    ), "Data types incorrect pour 'product_weight_g'"
    assert (
        products_df["product_length_cm"].dtype == "float64"
    ), "Data types incorrect pour 'product_length_cm'"
    assert (
        products_df["product_height_cm"].dtype == "float64"
    ), "Data types incorrect pour 'product_height_cm'"
    assert (
        products_df["product_width_cm"].dtype == "float64"
    ), "Data types incorrect pour 'product_width_cm'"


def test_order_items_dtypes():
    """
    Test sur le jeu de données 'olist_products_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_order_items_df, ncols_order_items_df = order_items_df.shape
    assert (
        nrows_order_items_df >= 112650
    ), f"Expected at least 112650 rows, but got {nrows_order_items_df}"
    assert (
        ncols_order_items_df == 7
    ), f"Expected 7 columns, but got {ncols_order_items_df}"

    assert (
        order_items_df["order_id"].dtype == "object"
    ), "Data types incorrect pour 'order_id'"
    assert (
        order_items_df["order_item_id"].dtype == "int64"
    ), "Data types incorrect pour 'order_item_id'"
    assert (
        order_items_df["product_id"].dtype == "object"
    ), "Data types incorrect pour 'product_id'"
    assert (
        order_items_df["seller_id"].dtype == "object"
    ), "Data types incorrect pour 'seller_id'"
    assert (
        order_items_df["shipping_limit_date"].dtype == "object"
    ), "Data types incorrect pour 'shipping_limit_date'"
    assert (
        order_items_df["price"].dtype == "float64"
    ), "Data types incorrect pour 'price'"
    assert (
        order_items_df["freight_value"].dtype == "float64"
    ), "Data types incorrect pour 'freight_value'"


def test_sellers_dtypes():
    """
    Test sur le jeu de données 'olist_sellers_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_sellers, ncols_sellers = sellers_df.shape
    assert (
        nrows_sellers >= 3095
    ), f"Expected at least 3095 rows, but got {nrows_sellers}"
    assert ncols_sellers == 4, f"Expected 4 columns, but got {ncols_sellers}"
    assert (
        sellers_df["seller_id"].dtype == "object"
    ), "Data types incorrect pour 'seller_id'"
    assert (
        sellers_df["seller_zip_code_prefix"].dtype == "int64"
    ), "Data types incorrect pour 'seller_zip_code_prefix'"
    assert (
        sellers_df["seller_city"].dtype == "object"
    ), "Data types incorrect pour 'seller_city'"
    assert (
        sellers_df["seller_state"].dtype == "object"
    ), "Data types incorrect pour 'seller_state'"


def test_customers_dtypes():
    """ "
    Test sur le jeu de données 'olist_customers_dataset.csv'

    Verification:
        - Shape du datafrane
        - Type des colonnes
    """
    nrows_customers, ncols_customers = customers_df.shape
    assert (
        nrows_customers >= 99441
    ), f"Expected at least 99441 rows, but got {nrows_customers}"
    assert ncols_customers == 5, f"Expected 5 columns, but got {ncols_customers}"
    assert (
        customers_df["customer_id"].dtype == "object"
    ), "Data types incorrect pour 'customer_id'"
    assert (
        customers_df["customer_unique_id"].dtype == "object"
    ), "Data types incorrect pour 'customer_unique_id'"
    assert (
        customers_df["customer_zip_code_prefix"].dtype == "int64"
    ), "Data types incorrect pour 'customer_zip_code_prefix'"
    assert (
        customers_df["customer_city"].dtype == "object"
    ), "Data types incorrect pour 'customer_city'"
    assert (
        customers_df["customer_state"].dtype == "object"
    ), "Data types incorrect pour 'customer_state'"


def test_translations_shape():
    """
    Test pour le shape du jeu de données 'product_category_name_translation.csv'
    """
    nrows_product_category, ncols_product_category = product_category_df.shape
    assert (
        nrows_product_category >= 71
    ), f"Expected at least 71 rows, but got {nrows_product_category}"
    assert (
        ncols_product_category == 2
    ), f"Expected 2 columns, but got {ncols_product_category}"
