import streamlit as st
from pages.data_ingestion import data_ingestion_page


def main():
    st.set_page_config(
        page_title="Simple RAG",
        layout="wide"
    )

    st.title("📚 Simple RAG With Vector Store")

    tab1, tab2 = st.tabs(["📥 Data Ingestion", "🔍 Retrieval"])

    with tab1:
        data_ingestion_page()

    with tab2:
        st.header("🔍 Data Retrieval")
        if "documents" not in st.session_state:
            st.info("Please ingest documents first.")
        else:
            st.success(f"{len(st.session_state.documents)} documents ready for retrieval 🚀")


if __name__ == "__main__":
    main()
