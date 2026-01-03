from typing import List
import streamlit as st
from services import ParserService


def process_files_button_label(file_count: int) -> str:
    return "Process File" if file_count == 1 else "Process Files"

def preview_parsed_file_data_section():
    if "documents" not in st.session_state or not st.session_state.documents:
        return

    with st.expander("📄 Preview Parsed File Data", expanded=False):

        # -------------------------
        # File Selection
        # -------------------------
        file_names = list(st.session_state.documents.keys())

        selected_file = st.selectbox(
            "Select a file",
            file_names,
            key="preview_selected_file"
        )

        # Reset page index when file changes
        if st.session_state.get("last_selected_file") != selected_file:
            st.session_state.page_index = 1
            st.session_state.last_selected_file = selected_file

        pages = st.session_state.documents.get(selected_file, [])
        total_pages = len(pages)

        # -------------------------
        # Empty / No Pages
        # -------------------------
        if total_pages == 0:
            st.warning("No parsed content available for this file.")
            return

        # -------------------------
        # Page Navigation
        # -------------------------
        if total_pages > 1:
            col1, col2, col3 = st.columns([1, 3, 1])

            with col1:
                prev_page = st.button("⬅ Previous", key="prev_page_btn")

            with col2:
                page_index = st.slider(
                    "Page",
                    min_value=1,
                    max_value=total_pages,
                    value=min(
                        st.session_state.get("page_index", 1),
                        total_pages
                    ),
                    key="page_slider"
                )

            with col3:
                next_page = st.button("Next ➡", key="next_page_btn")

            # Update page index safely
            if prev_page and page_index > 1:
                page_index -= 1
            if next_page and page_index < total_pages:
                page_index += 1

            st.session_state.page_index = page_index

        else:
            # Single-page document (NO SLIDER)
            page_index = 1
            st.session_state.page_index = 1

        page = pages[page_index - 1]

        # -------------------------
        # Page Viewer
        # -------------------------
        st.divider()
        st.subheader(f"📄 Page {page_index} / {total_pages}")

        col1, col2 = st.columns([1, 4])

        with col1:
            st.markdown("**Metadata**")
            st.json(page.metadata)

        with col2:
            st.markdown("**Content Preview**")
            st.write(page.page_content[:3000])

            if len(page.page_content) > 3000:
                st.caption("Showing first 3000 characters")


def data_ingestion_page():
        # Initialize session state
    if "documents" not in st.session_state:
        st.session_state.documents = []


    if len(st.session_state.documents) == 0:
        st.header("📄 Parse Files")
        st.caption("Upload documents to prepare them for question answering")

        uploaded_files = st.file_uploader(
            "Choose files",
            accept_multiple_files=True,
            type=["pdf", "csv", "txt", "docx", "xlsx"]
        )

        if uploaded_files:
            st.info(f"{len(uploaded_files)} file(s) selected")

            col1, col2 = st.columns([1, 4])

            with col1:
                process_btn = st.button(
                    process_files_button_label(len(uploaded_files)),
                    type="primary"
                )

            if process_btn:
                with st.spinner("Parsing documents..."):
                    documents, errors = ParserService.parse_files(uploaded_files)
                    if errors:
                        st.warning("Some files could not be parsed:")
                        for fname, err in errors.items():
                            st.caption(f"⚠️ {fname}: skipped")


                    st.session_state.documents = documents

                st.success(f"Successfully processed {len(documents)} documents")
                st.rerun()

    if st.session_state.documents:
        preview_parsed_file_data_section()