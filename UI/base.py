import streamlit as st
import requests

# Set the page configuration
st.set_page_config(page_title="API Segmentation Olist", layout="wide", page_icon="📜")

# Title and description
st.title("Segmentation des clients Olist")
st.markdown(
    "![Image](https://media.licdn.com/dms/image/D5612AQEbR-vj1LqUFw/article-cover_image-shrink_600_2000/0/1693362637757?e=2147483647&v=beta&t=yD-EP9-YR-_gitRaxxiAGd5jzvvlnrjyzuSgVfXYDQY)"
)

# Define tabs
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Single Prediction",
        "Batch Prediction",
        "Get Customer Segment",
        "Get Segments Information",
    ]
)

# Single Prediction
with tab1:
    st.header("Single Prediction")
    customer_id = st.text_input("Customer ID")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    with col1:
        recency = st.number_input("Récence", key="rececny")
    with col2:
        frequency = st.number_input("Fréquence", key="freq")
    with col3:
        total_spent = st.number_input("Dépense totale", format="%.2f", key="spe")
    with col4:
        avg_installments = st.number_input(
            "Nombre d'installs moyen", format="%.2f", key="ins"
        )
    with col5:
        total_items = st.number_input("Nombre items total", key="items")
    with col6:
        payment_price_ratio = st.number_input(
            "Ratio prix initial et prix payé", format="%.2f", key="ratio"
        )
    with col7:
        total_freight_value = st.number_input(
            "Total livraison", format="%.2f", key="fret"
        )
    with col8:
        avg_fractional_payment_ratio = st.number_input(
            "Moyenne paiement install / en 1 fois", format="%.2f", key="frac"
        )

    if st.button("Prédire le segment"):
        if customer_id:
            customer_data = {
                "customer_id": customer_id,
                "total_spent": total_spent,
                "frequency": frequency,
                "avg_installments": avg_installments,
                "total_items": total_items,
                "payment_price_ratio": payment_price_ratio,
                "recency": recency,
                "avg_fractional_payment_ratio": avg_fractional_payment_ratio,
                "total_freight_value": total_freight_value,
            }
            response = requests.post(
                "https://segmentation-olist-deployment.onrender.com/api/segment",
                json=customer_data,
            )
            if response.status_code == 200:
                result = response.json()
                st.json(result)
            else:
                st.error("Erreur: " + response.text)
        else:
            st.error("Veuillez enter un Customer ID")

# Batch Prediction
with tab2:
    st.header("Batch Prediction")
    uploaded_file = st.file_uploader(
        "Choisissez un fichier CSV ou XLSX", type=["csv", "xlsx"]
    )
    if st.button("Prédire les segments en lot"):
        if uploaded_file:
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type,
                )
            }
            response = requests.post(
                "https://segmentation-olist-deployment.onrender.com/segment/batch",
                files=files,
            )
            if response.status_code == 200:
                result = response.json()
                st.json(result)
            elif response.status_code == 403:
                st.error("Accès refusé : vérifiez vos permissions et réessayez.")
            else:
                st.error("Erreur: " + response.text)
        else:
            st.error("Veuillez charger un fichier CSV ou XLSX")

# Get Customer Segment
with tab3:
    st.header("Get Customer Segment")
    customer_id = st.text_input("Customer ID", key="customer_id_tab3")

    if st.button("Récupérer le segment utilisateur", key="get_segment_button"):
        if customer_id:
            response = requests.get(
                f"https://segmentation-olist-deployment.onrender.com/api/segment/{customer_id}"
            )
            if response.status_code == 200:
                result = response.json()
                st.json(result)
            else:
                st.error("Erreur: " + response.text)
        else:
            st.error("Veuillez entrer un Customer ID")

# Get Segments Information
with tab4:
    st.header("Get Segments Information")
    if st.button("Récupérer les informations des segments"):
        response = requests.get(
            "https://segmentation-olist-deployment.onrender.com/api/segments"
        )
        if response.status_code == 200:
            result = response.json()
            st.json(result)
        else:
            st.error("Erreur: " + response.text)
