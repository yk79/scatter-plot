import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def create_plot(df: pd.DataFrame, x_column: str, y_column: str, z_column: str, label: str, plot_type: str):
    if plot_type == "3D":
        return px.scatter_3d(
            df,
            x_column,
            y_column,
            z_column,
            text=label,
            hover_name=label,
            height=700,
            width=700,
            color="スコア"
        )
    else:
        return px.scatter(
            df,
            x_column,
            y_column,
            color=z_column,
            text=label,
            hover_name=label
        )


def create_scatter_plot():
    uploaded_file = st.file_uploader("CSVをアップロードしてください。", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        columns = df.columns.tolist()
        label = st.selectbox("ラベルを選択してください", columns)
        x_column = st.selectbox("X軸を選択してください", columns, index = None)
        y_column = st.selectbox("Y軸を選択してください", columns, index = None)
        z_column = st.selectbox("Z軸を選択してください", columns, index = None)
        plot_type = st.selectbox("plotするグラフの形式を選択してください", ("2D", "3D"))
        if x_column and y_column and z_column and plot_type:
            df["スコア"] = df.apply(lambda row: row[x_column] + row[y_column] + row[z_column], axis=1)
            st.plotly_chart(create_plot(df, x_column, y_column, z_column, label, plot_type))
