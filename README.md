# 📊 Business Intelligence Agent using LLM (Groq + LangChain + Streamlit)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-app-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Agent--framework-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM--powered-9cf?style=for-the-badge)

> A conversational AI-powered business intelligence system that transforms natural language questions into data-driven insights — with auto-generated charts and smart analysis.

---

## 🧠 Project Description

**"Business Intelligence Agent using LLM"** is an intelligent analytics assistant that allows business users, analysts, and non-technical professionals to gain powerful insights from structured sales datasets — simply by asking questions in plain English.

This application bridges the gap between **natural language processing** and **data analysis** by combining:
- 🧠 **LangChain agents**
- ⚡ **Groq-hosted LLaMA3-8B LLM**
- 📈 **Pandas & Plotly**
- 🖥️ **Streamlit frontend**

The result is a fully interactive, real-time **business intelligence agent** that analyzes uploaded sales data, interprets natural language questions, and generates visual reports — without writing code.

---

## 🚀 Features

✅ Upload your sales CSV file  
✅ Ask analytical questions in natural language  
✅ Uses LangChain + Groq to interpret your query  
✅ Generates insightful markdown explanations  
✅ Creates interactive charts using Plotly  
✅ Works with a default dataset if none uploaded  
✅ Sidebar shows versions of all required packages  

---

## 📸 Demo Preview

> Example:  
> **"Which product category achieved the highest sales growth in the last 6 months?"**


📊 Textual analysis from LLM:
(![WhatsApp Image 2025-07-04 at 11 14 18_001cef07](https://github.com/user-attachments/assets/1a5a0e44-88a4-497b-84c3-50c1f5990e14))

📈 Interactive chart generated with Plotly:
(![image](https://github.com/user-attachments/assets/7863df5c-f0ee-44c1-bf07-c7635fdd15c4))


✅ LLM processes the question  
✅ Agent analyzes the data using Pandas  
✅ Markdown answer + Line chart of trends  

---

## 📈 Real-World Applications

| Industry          | Example Use Case                                                                 |
|-------------------|----------------------------------------------------------------------------------|
| 🛍️ Retail          | "Which product category saw the largest increase in sales last quarter?"        |
| 🧪 Marketing       | "Which campaign had the highest ROI by region?"                                 |
| 🏥 Healthcare      | "Which department saw the most patient admissions last month?"                  |
| 🏦 Finance         | "How did revenue vs. expenses trend over the past year?"                        |
| 🎓 Education       | "What course had the highest attendance this semester?"                         |

---

## 🧰 Technical Highlights

| Feature                              | Description                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------|
| **LLM Agent (LangChain)**            | Uses `create_pandas_dataframe_agent` to execute real Python code on the data |
| **Groq Integration**                 | Accesses LLaMA3-8B via `langchain-groq` for ultra-fast inference            |
| **Streamlit UI**                     | Clean, interactive interface for CSV upload, question input, and results    |
| **Fallback Dataset Support**         | Uses a default CSV if user doesn’t upload a file                            |
| **Auto Visualization**               | Generates time-series or category-based plots using Plotly                  |
| **Tool Status Sidebar**              | Shows versions and availability of key packages like Groq and LangChain     |

---


