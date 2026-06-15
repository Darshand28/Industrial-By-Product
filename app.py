import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import numpy as np

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Industrial Waste Analytics",
    page_icon="♻️",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("♻️ Industrial Waste Analytics Dashboard")

st.markdown("### Statistics • Charts • Insights")

# =====================================================
# LOAD DATA
# =====================================================

files = glob.glob("archive(6).zip.csv")

if len(files) == 0:

    st.error("No CSV files found inside data folder")

    st.stop()

df_list = []

for file in files:

    temp_df = pd.read_csv("archive(6).zip.csv")

    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

# =====================================================
# SHOW DATA
# =====================================================

st.subheader("📂 Dataset Preview")

st.dataframe(df.head())

# =====================================================
# NUMERIC COLUMNS
# =====================================================

numeric_cols = df.select_dtypes(
    include=['int64', 'float64']
).columns.tolist()

if len(numeric_cols) == 0:

    st.error("No numeric columns found")

    st.stop()

selected_column = st.selectbox(
    "Select Numeric Column",
    numeric_cols
)

# =====================================================
# STATISTICS
# =====================================================

st.subheader("📊 Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Mean",
    round(df[selected_column].mean(), 2)
)

col2.metric(
    "Median",
    round(df[selected_column].median(), 2)
)

col3.metric(
    "Maximum",
    round(df[selected_column].max(), 2)
)

col4.metric(
    "Minimum",
    round(df[selected_column].min(), 2)
)

col5, col6, col7 = st.columns(3)

col5.metric(
    "Standard Deviation",
    round(df[selected_column].std(), 2)
)

col6.metric(
    "Variance",
    round(df[selected_column].var(), 2)
)

col7.metric(
    "Total Records",
    len(df)
)

# =====================================================
# BAR CHART
# =====================================================

st.subheader("📈 Bar Chart")

fig1 = px.bar(
    df.head(10),
    y=selected_column,
    title="Top 10 Records"
)

st.plotly_chart(fig1, use_container_width=True)

# =====================================================
# LINE CHART
# =====================================================

st.subheader("📉 Line Chart")

fig2 = px.line(
    df.head(100),
    y=selected_column,
    title="Trend Analysis"
)

st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# HISTOGRAM
# =====================================================

st.subheader("📊 Histogram")

fig3 = px.histogram(
    df,
    x=selected_column,
    nbins=30,
    title="Distribution Analysis"
)

st.plotly_chart(fig3, use_container_width=True)

# =====================================================
# BOX PLOT
# =====================================================

st.subheader("📦 Box Plot")

fig4 = px.box(
    df,
    y=selected_column,
    title="Box Plot Analysis"
)

st.plotly_chart(fig4, use_container_width=True)

# =====================================================
# SCATTER PLOT
# =====================================================

if len(numeric_cols) >= 2:

    st.subheader("🔵 Scatter Plot")

    x_axis = st.selectbox(
        "Select X Axis",
        numeric_cols,
        index=0
    )

    y_axis = st.selectbox(
        "Select Y Axis",
        numeric_cols,
        index=1
    )

    fig5 = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        title="Scatter Plot Analysis"
    )

    st.plotly_chart(fig5, use_container_width=True)

# =====================================================
# PIE CHART
# =====================================================

st.subheader("🥧 Pie Chart")

pie_df = pd.DataFrame({
    "Category": ["Mean", "Median", "Maximum", "Minimum"],
    "Value": [
        df[selected_column].mean(),
        df[selected_column].median(),
        df[selected_column].max(),
        df[selected_column].min()
    ]
})

fig6 = px.pie(
    pie_df,
    names="Category",
    values="Value",
    title="Statistics Distribution"
)

st.plotly_chart(fig6, use_container_width=True)

# =====================================================
# CORRELATION HEATMAP
# =====================================================

st.subheader("🔥 Correlation Heatmap")

corr = df[numeric_cols].corr()

fig7 = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Matrix"
)

st.plotly_chart(fig7, use_container_width=True)

# =====================================================
# DESCRIPTIVE STATISTICS
# =====================================================

st.subheader("🧠 Descriptive Statistics")

st.dataframe(
    df[numeric_cols].describe()
)

# =====================================================
# DOWNLOAD CSV
# =====================================================

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="processed_data.csv",
    mime="text/csv"
)

# =====================================================
# FOOTER
# =====================================================

st.success("Dashboard Loaded Successfully ✅")
