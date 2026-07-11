from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "traffic_model.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"
DATA_PATH = BASE_DIR / "data" / "processed" / "master_weather.parquet"
MASTER_DATASET_PATH = (
    BASE_DIR /
    "data" /
    "processed" /
    "master_dataset.csv"
)


# ======================================================
# Cached Loaders
# ======================================================

@st.cache_resource
def load_model():
    """Load the trained machine learning model."""
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_feature_columns():
    """Load feature column names used during training."""
    return joblib.load(FEATURE_PATH)


@st.cache_data
def load_data():
    """Load processed traffic dataset."""
    return pd.read_parquet(DATA_PATH)

@st.cache_data
def load_master_dataset():
    """
    Load monitoring site dataset containing
    latitude and longitude information.
    """
    return pd.read_csv(MASTER_DATASET_PATH)