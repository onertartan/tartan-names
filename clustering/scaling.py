import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler, normalize


def scale(scaler_method, df, total_counts_unique):
    """Apply scaling to clustering features and preserve the input shape.

    L1/L2 options normalize each row.
    Standard/MinMax/Robust scalers transform each column across rows.
    """
    if scaler_method == "None":
        df_scaled = df.values

    elif "L1" in scaler_method:
        # Row-wise relative distribution of selected features.
        df_scaled = normalize(df, axis=1, norm="l1")

    elif "L2" in scaler_method:
        # Row-wise unit-length vectors for angular similarity.
        df_scaled = normalize(df, axis=1, norm="l2")

    elif "Share of Total" in scaler_method:
        # Share of all births (not just top-n)
        df_scaled = df.div(total_counts_unique, axis=0)

    elif "TF-IDF" in scaler_method:
        tfidf = TfidfTransformer(
            norm="l2",
            use_idf=True,
            smooth_idf=True
        )
        df_scaled = tfidf.fit_transform(df.values).toarray()

    elif "Standard Scaler" in scaler_method:
        # Column-wise z-score scaling across all rows.
        df_scaled = StandardScaler().fit_transform(df)

    elif "MinMaxScaler" in scaler_method:
        # Column-wise min-max scaling across all rows.
        df_scaled = MinMaxScaler().fit_transform(df)

    elif "RobustScaler" in scaler_method:
        # Column-wise robust scaling across all rows.
        df_scaled = RobustScaler().fit_transform(df)

    else:
        st.warning(f"Unknown scaling option: {scaler_method}. Using raw counts.")
        df_scaled = df.values

    return pd.DataFrame(
        df_scaled,
        index=df.index,
        columns=df.columns
    )
