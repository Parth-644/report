import pandas as pd
import streamlit as st

def load_reports(files):
    data_frames = []
    for file in files:
        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file)
            data_frames.append(df)
        except Exception as e:
            st.error(f"Error loading file {file.name}: {e}")
    return pd.concat(data_frames, ignore_index=True)

def analyze_data(df):
    try:
        summary = df.describe()
        return summary
    except Exception as e:
        st.error(f"Error analyzing data: {e}")

def main():
    st.title("Reports Analysis")

    uploaded_files = st.file_uploader("Upload Reports", accept_multiple_files=True, type=["csv", "xlsx", "xls"])

    if uploaded_files:
        try:
            data = load_reports(uploaded_files)
            summary = analyze_data(data)
            st.header("Data Summary")
            st.write(summary)
            st.header("Data")
            st.dataframe(data)
        except Exception as e:
            st.error(f"Error processing files: {e}")

if __name__ == "__main__":
    main()
