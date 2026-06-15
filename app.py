import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Industrial Waste Analytics Dashboard",
    page_icon="♻️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.metric-card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("♻️ Industrial Waste Analytics Dashboard")
st.markdown("### Deep Analytics • AI Insights • Interactive Charts")

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    files = glob.glob("data/*.csv")

    df_list = []

    for file in files:

        temp_df = pd.read_csv(file)

        temp_df["Source_File"] = file.split("/")[-1]

        df_list.append(temp_df)

    final_df = pd.concat(df_list, ignore_index=True)

    return final_df

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("📌 Dashboard Filters")

numeric_columns = df.select_dtypes(
    include=['int64', 'float64']
).columns.tolist()

selected_column = st.sidebar.selectbox(
    "Select Numeric Column",
    numeric_columns
)

chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Histogram"]
)

# =========================================================
# KPI METRICS
# =========================================================

st.subheader("📊 Dashboard Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:
    st.metric(
        "Total Columns",
        len(df.columns)
    )

with col3:
    st.metric(
        "Average Value",
        round(df[selected_column].mean(), 2)
    )

with col4:
    st.metric(
        "Maximum Value",
        round(df[selected_column].max(), 2)
    )

# =========================================================
# DATA PREVIEW
# =========================================================

st.subheader("🗂 Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)

# =========================================================
# CHARTS
# =========================================================

st.subheader("📈 Analytics Visualization")

if chart_type == "Bar Chart":

    top_df = df.nlargest(10, selected_column)

    fig = px.bar(
        top_df,
        x=top_df.index,
        y=selected_column,
        color=selected_column,
        title=f"Top 10 Records by {selected_column}",
        text=selected_column
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Line Chart":

    line_df = df[selected_column].head(100)

    fig = px.line(
        line_df,
        y=selected_column,
        markers=True,
        title=f"{selected_column} Trend Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Histogram":

    fig = px.histogram(
        df,
        x=selected_column,
        nbins=30,
        color_discrete_sequence=['blue'],
        title=f"{selected_column} Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# PIE CHART
# =========================================================

st.subheader("🥧 Source File Distribution")

source_df = df["Source_File"].value_counts().reset_index()

source_df.columns = ["File", "Count"]

fig2 = px.pie(
    source_df,
    names="File",
    values="Count",
    title="Dataset File Contribution"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# CORRELATION HEATMAP
# =========================================================

st.subheader("🔥 Correlation Analysis")

corr_df = df[numeric_columns].corr()

fig3 = px.imshow(
    corr_df,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# AI INSIGHTS
# =========================================================

st.subheader("🧠 AI Insights")

avg_value = round(df[selected_column].mean(), 2)
max_value = round(df[selected_column].max(), 2)
min_value = round(df[selected_column].min(), 2)
std_value = round(df[selected_column].std(), 2)

st.success(f"""
✅ Average {selected_column}: {avg_value}

✅ Maximum {selected_column}: {max_value}

✅ Minimum {selected_column}: {min_value}

✅ Standard Deviation: {std_value}

✅ Dashboard successfully processed industrial waste analytics dataset.
""")

# =========================================================
# DOWNLOAD SECTION
# =========================================================

st.subheader("⬇ Download Processed Dataset")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='processed_waste_data.csv',
    mime='text/csv'
)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
### 🚀 Technologies Used
- Python
- Streamlit
- Plotly
- Pandas
- NumPy

### 📌 Deployment
```bash
streamlit run app.py
