import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="Industrial Waste Dashboard",
    page_icon="♻️",
    layout="wide"
)

# TITLE
st.title("♻️ Industrial Waste Analytics Dashboard")

# READ YOUR CSV FILE
df = pd.read_csv("archive (6).zip.csv")
import pandas as pd
import plotly.express as px
import glob

# PAGE CONFIG
st.set_page_config(
    page_title="Waste Analytics Dashboard",
    page_icon="♻️",
    layout="wide"
)

# TITLE
st.title("♻️ Industrial Waste Analytics Dashboard")

# READ ALL CSV FILES
files = glob.glob("archive (6).zip.csv")

# CHECK FILES
if len(files) == 0:
    st.error("No CSV files found in data folder")
    st.stop()

# LOAD DATA
df_list = []

for file in files:

    temp_df = pd.read_csv("archive (6).zip.csv")
import pandas as pd
import plotly.express as px
import glob

# PAGE CONFIG
st.set_page_config(
    page_title="Waste Analytics Dashboard",
    page_icon="♻️",
    layout="wide"
)

# TITLE
st.title("♻️ Industrial Waste Analytics Dashboard")

# READ ALL CSV FILES
files = glob.glob("archive (6).zip.csv")

# CHECK FILES
if len(files) == 0:
    st.error("No CSV files found in data folder")
    st.stop()

# LOAD DATA
df_list = []

for file in files:

    temp_df = pd.read_csv("archive (6).zip.csv")

    df_list.append(temp_df)

# COMBINE DATA
df = pd.concat(df_list, ignore_index=True)

# SHOW DATA
st.subheader("Dataset Preview")

st.dataframe(df.head())

# NUMERIC COLUMNS
numeric_cols = df.select_dtypes(
    include=['int64', 'float64']
).columns.tolist()

# SELECT COLUMN
selected_column = st.selectbox(
    "Select Column",
    numeric_cols
)

# STATISTICS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average",
    round(df[selected_column].mean(), 2)
)

col2.metric(
    "Maximum",
    round(df[selected_column].max(), 2)
)

col3.metric(
    "Minimum",
    round(df[selected_column].min(), 2)
)

# BAR CHART
fig1 = px.bar(
    df.head(10),
    y=selected_column,
    title="Bar Chart"
)

st.plotly_chart(fig1, use_container_width=True)

# LINE CHART
fig2 = px.line(
    df.head(100),
    y=selected_column,
    title="Line Chart"
)

st.plotly_chart(fig2, use_container_width=True)

# HISTOGRAM
fig3 = px.histogram(
    df,
    x=selected_column,
    nbins=30,
    title="Histogram"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Dashboard Loaded Successfully ✅")

    

# COMBINE DATA
df = pd.concat(df_list, ignore_index=True)

# SHOW DATA
st.subheader("Dataset Preview")

st.dataframe(df.head())

# NUMERIC COLUMNS
numeric_cols = df.select_dtypes(
    include=['int64', 'float64']
).columns.tolist()

# SELECT COLUMN
selected_column = st.selectbox(
    "Select Column",
    numeric_cols
)

# STATISTICS
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average",
    round(df[selected_column].mean(), 2)
)

col2.metric(
    "Maximum",
    round(df[selected_column].max(), 2)
)

col3.metric(
    "Minimum",
    round(df[selected_column].min(), 2)
)

# BAR CHART
fig1 = px.bar(
    df.head(10),
    y=selected_column,
    title="Bar Chart"
)

st.plotly_chart(fig1, use_container_width=True)

# LINE CHART
fig2 = px.line(
    df.head(100),
    y=selected_column,
    title="Line Chart"
)

st.plotly_chart(fig2, use_container_width=True)

# HISTOGRAM
fig3 = px.histogram(
    df,
    x=selected_column,
    nbins=30,
    title="Histogram"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Dashboard Loaded Successfully ✅").csv")

# SHOW DATA
st.subheader("Dataset Preview")

st.dataframe(df.head())

# GET NUMERIC COLUMNS
numeric_cols = df.select_dtypes(
    include=['int64', 'float64']
).columns.tolist()

# CHECK NUMERIC COLUMNS
if len(numeric_cols) == 0:

    st.error("No numeric columns found")

    st.stop()

# SELECT COLUMN
selected_column = st.selectbox(
    "Select Numeric Column",
    numeric_cols
)

# STATISTICS
st.subheader("Statistics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average",
    round(df[selected_column].mean(), 2)
)

col2.metric(
    "Maximum",
    round(df[selected_column].max(), 2)
)

col3.metric(
    "Minimum",
    round(df[selected_column].min(), 2)
)

# BAR CHART
st.subheader("Bar Chart")

fig1 = px.bar(
    df.head(10),
    y=selected_column,
    title="Top 10 Records"
)

st.plotly_chart(fig1, use_container_width=True)

# LINE CHART
st.subheader("Line Chart")

fig2 = px.line(
    df.head(100),
    y=selected_column,
    title="Trend Analysis"
)

st.plotly_chart(fig2, use_container_width=True)

# HISTOGRAM
st.subheader("Histogram")

fig3 = px.histogram(
    df,
    x=selected_column,
    nbins=30,
    title="Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# SUCCESS
st.success("Dashboard Loaded Successfully ✅")
