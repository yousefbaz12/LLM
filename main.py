import streamlit as st
import pandas as pd
import plotly.express as px
import pkg_resources

# Print versions of installed libraries in sidebar
st.sidebar.text(f"✅ pandas version: {pd.__version__}")
st.sidebar.text(f"✅ plotly version: {px}")

try:
    from langchain_groq import ChatGroq
    st.sidebar.text(f"✅ langchain_groq version: {pkg_resources.get_distribution('langchain-groq').version}")
except ImportError:
    st.sidebar.error("❌ langchain_groq is not available")

try:
    from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
    st.sidebar.text(f"✅ langchain_experimental version: {pkg_resources.get_distribution('langchain-experimental').version}")
except ImportError as e:
    st.sidebar.error(f"❌ langchain_experimental import failed: {e}")

# Set Streamlit page configuration
st.set_page_config(page_title="📊 Business Intelligence Agent using LLM", layout="wide")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload your sales dataset (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
else:
    try:
        df = pd.read_csv("sanitary_warehouse_simulated.csv")
        st.info("✅ Using default dataset: sanitary_warehouse_simulated.csv")
    except FileNotFoundError:
        st.error("❌ Default dataset 'sanitary_warehouse_simulated.csv' not found. Please upload a file.")
        st.stop()

# Initialize LLM using Groq
try:
    llm = ChatGroq(
        groq_api_key="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",
        model="llama3-8b-8192",
        temperature=0
    )
except Exception as e:
    st.error(f"❌ Failed to initialize ChatGroq: {e}")
    st.stop()

# Create agent if the function is available
agent = None
if 'create_pandas_dataframe_agent' in globals():
    try:
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=df,
            verbose=True,
            allow_dangerous_code=True
        )
        st.sidebar.success("✅ Agent created successfully")
    except Exception as e:
        st.sidebar.error(f"❌ Failed to create agent: {e}")
else:
    st.error("❌ The create_pandas_dataframe_agent function is not available. Please check the langchain-experimental installation.")
    st.stop()

# Streamlit UI
st.title("🔍 Business Intelligence Analyst using LLM and Groq")
st.markdown("Enter your analytical question regarding the sales data:")

# User input text area
user_query = st.text_area("✍️ Your Question:", """
Assume you are a data analyst. You have a sales dataset with columns like category, sale_date, and amount_sold.
Which product category achieved the highest sales growth in the last 6 months? Explain in detail.
""", height=200)

# Run analysis when button is clicked
if st.button("🚀 Run Analysis"):
    if agent is not None:
        with st.spinner("Analyzing using LLM..."):
            try:
                response = agent.invoke({"input": user_query})  # Adjusted for compatibility
                st.subheader("📌 Result:")
                st.markdown(f"```markdown\n{response['output'] if isinstance(response, dict) else response}```")
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
    else:
        st.error("❌ Agent not available. Please check the setup.")

    # Generate chart if data contains necessary columns
    required_columns = ["category", "sale_date", "amount_sold"]
    if all(col in df.columns for col in required_columns):
        try:
            df['sale_date'] = pd.to_datetime(df['sale_date'])
            last_6_months = df[df['sale_date'] >= pd.Timestamp.now() - pd.DateOffset(months=6)]
            if not last_6_months.empty:
                monthly_sales = last_6_months.groupby([
                    last_6_months['sale_date'].dt.to_period('M').astype(str),
                    'category'
                ])['amount_sold'].sum().reset_index()

                st.subheader("📊 Monthly Sales by Category (Last 6 Months)")
                fig = px.line(
                    monthly_sales,
                    x='sale_date',
                    y='amount_sold',
                    color='category',
                    markers=True,
                    title='Monthly Sales by Category',
                    labels={'sale_date': 'Month', 'amount_sold': 'Total Sales'}
                )
                fig.update_layout(template='plotly_white')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("⚠️ No data available for the last 6 months.")
        except Exception as e:
            st.warning(f"⚠️ Could not generate the chart: {e}")
    else:
        st.warning("⚠️ Dataset must contain 'category', 'sale_date', and 'amount_sold' columns.")

# Display dataset sample for debugging
if st.checkbox("Show sample of dataset"):
    st.write(df.head())