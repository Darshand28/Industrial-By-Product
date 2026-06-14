import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Cheddar Cheese Analytics Dashboard",
    page_icon="🧀",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #1f2937;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/cheese_data.csv")

    # Clean columns
    if 'Sales' in df.columns:
        df['Sales'] = (
            df['Sales']
            .astype(str)
            .str.replace(',', '')
        )
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

    if 'Weighted Prices' in df.columns:
        df['Weighted Prices'] = pd.to_numeric(
            df['Weighted Prices'],
            errors='coerce'
        )

    return df

df = load_data()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📊 Dashboard Filters")

min_price = float(df['Weighted Prices'].min())
max_price = float(df['Weighted Prices'].max())

price_range = st.sidebar.slider(
    "Select Weighted Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

filtered_df = df[
    (df['Weighted Prices'] >= price_range[0]) &
    (df['Weighted Prices'] <= price_range[1])
]

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🧀 40 Pound Block Cheddar Cheese Dashboard")
st.markdown("### Deep Analytics & Business Insights")

st.divider()

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Price",
        f"${filtered_df['Weighted Prices'].mean():.2f}"
    )

with col2:
    st.metric(
        "Maximum Price",
        f"${filtered_df['Weighted Prices'].max():.2f}"
    )

with col3:
    st.metric(
        "Total Sales",
        f"{filtered_df['Sales'].sum():,.0f}"
    )

with col4:
    st.metric(
        "Average Sales",
        f"{filtered_df['Sales'].mean():,.0f}"
    )

st.divider()

# ---------------------------------------------------
# PRICE TREND
# ---------------------------------------------------
st.subheader("📈 Weighted Price Trend")

line_chart = px.line(
    filtered_df,
    x=filtered_df.index,
    y='Weighted Prices',
    markers=True,
    title="Cheddar Cheese Price Movement"
)

line_chart.update_layout(
    xaxis_title="Index",
    yaxis_title="Weighted Price",
    template="plotly_white"
)

st.plotly_chart(line_chart, use_container_width=True)

# ---------------------------------------------------
# SALES DISTRIBUTION
# ---------------------------------------------------
st.subheader("💰 Sales Distribution")

hist_chart = px.histogram(
    filtered_df,
    x='Sales',
    nbins=30,
    title="Sales Frequency Distribution"
)

hist_chart.update_layout(
    template="plotly_white"
)

st.plotly_chart(hist_chart, use_container_width=True)

# ---------------------------------------------------
# SCATTER PLOT
# ---------------------------------------------------
st.subheader("🔍 Price vs Sales Correlation")

scatter_chart = px.scatter(
    filtered_df,
    x='Weighted Prices',
    y='Sales',
    size='Sales',
    trendline='ols',
    title="Relationship Between Prices and Sales"
)

scatter_chart.update_layout(
    template="plotly_white"
)

st.plotly_chart(scatter_chart, use_container_width=True)

# ---------------------------------------------------
# MOVING AVERAGE ANALYSIS
# ---------------------------------------------------
st.subheader("📊 Moving Average Analytics")

filtered_df['Rolling Average'] = (
    filtered_df['Weighted Prices']
    .rolling(window=7)
    .mean()
)

moving_avg_chart = go.Figure()

moving_avg_chart.add_trace(
    go.Scatter(
        x=filtered_df.index,
        y=filtered_df['Weighted Prices'],
        mode='lines',
        name='Actual Price'
    )
)

moving_avg_chart.add_trace(
    go.Scatter(
        x=filtered_df.index,
        y=filtered_df['Rolling Average'],
        mode='lines',
        name='7-Day Moving Average'
    )
)

moving_avg_chart.update_layout(
    title="Price Trend with Moving Average",
    xaxis_title="Index",
    yaxis_title="Price",
    template="plotly_white"
)

st.plotly_chart(moving_avg_chart, use_container_width=True)

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------
st.subheader("🧠 Business Insights")

highest_sales = filtered_df.loc[
    filtered_df['Sales'].idxmax()
]

lowest_sales = filtered_df.loc[
    filtered_df['Sales'].idxmin()
]

correlation = filtered_df['Weighted Prices'].corr(
    filtered_df['Sales']
)

st.success(
    f"""
    Highest sales recorded:
    {highest_sales['Sales']:,.0f}
    at weighted price
    ${highest_sales['Weighted Prices']:.2f}
    """
)

st.warning(
    f"""
    Lowest sales recorded:
    {lowest_sales['Sales']:,.0f}
    at weighted price
    ${lowest_sales['Weighted Prices']:.2f}
    """
)

st.info(
    f"""
    Correlation between weighted price and sales:
    {correlation:.2f}
    """
)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------
st.subheader("📋 Dataset Preview")

with st.expander("View Raw Dataset"):
    st.dataframe(filtered_df)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, Plotly & Python")
