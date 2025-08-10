    import streamlit as st
    import pandas as pd
    import requests
    import os
    from dotenv import load_dotenv

    # Must be the first Streamlit command
    st.set_page_config(page_title="Data Quality Checker", layout="wide")

    load_dotenv()

    # API_KEY = st.secrets["api"]["OPEN_ROUTER_API_KEY"]
    API_KEY = st.text_input("🔑 Enter your OpenRouter API Key", type="password")

    st.title("📊 Data Quality Checker using LLM 🚀")

    uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.success("✅ File successfully uploaded!")

        st.markdown("### 🔍 Data Preview")
        st.dataframe(df.head(), use_container_width=True)

        # Generate quality stats
        total_rows = len(df)
        total_columns = len(df.columns)
        duplicate_rows = df.duplicated().sum()
        missing_report = df.isnull().mean() * 100
        dtypes = df.dtypes.astype(str)

        # Show metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("🧮 Total Rows", f"{total_rows}")
        col2.metric("🧾 Total Columns", f"{total_columns}")
        col3.metric("🗂️ Duplicate Rows", f"{duplicate_rows}")

        # Expanders for details
        with st.expander("🕳️ Missing Values Report"):
            st.dataframe(missing_report.reset_index().rename(columns={"index": "Column", 0: "Missing (%)"}), use_container_width=True)

        with st.expander("📦 Column Data Types"):
            st.dataframe(dtypes.reset_index().rename(columns={"index": "Column", 0: "Type"}), use_container_width=True)

        # Build raw quality text report
        report = f"""
    Total Rows: {total_rows}
    Total Columns: {total_columns}
    Duplicate Rows: {duplicate_rows}

    Missing Values (%):
    {missing_report.to_string()}

    Data Types:
    {dtypes.to_string()}
    """

    if st.button("🧠 Summarize with LLM"):
        if report.strip() == "":
            st.error("⚠️ Report is empty. Please upload a proper CSV file.")
        else:
            with st.spinner("Generating summary with LLM..."):

                prompt = f"""
    You are a data quality analyst. Summarize the following raw data quality report:

    {report}

    Write a human-readable summary highlighting key issues and suggesting fixes.
    """

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }

                payload = {
                    "model": "deepseek/deepseek-r1-0528:free",
                    "messages": [
                        {"role": "system", "content": "You are a helpful data quality analyst."},
                        {"role": "user", "content": prompt}
                    ]
                }

                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=payload
                )

                if response.status_code == 200:
                    try:
                        summary = response.json()["choices"][0]["message"]["content"]
                        st.success("✅ Summary generated!")
                        st.markdown("### 🧠 LLM Summary")
                        st.markdown(summary)
                    except Exception as e:
                        st.error("❌ Failed to parse LLM response.")
                        st.exception(e)
                else:
                    st.error("❌ Failed to fetch response from LLM")
                    st.code(f"Status Code: {response.status_code}")
                    st.code(f"Response: {response.text}")
    else:
        st.info("📁 Please upload a CSV file to begin.")
