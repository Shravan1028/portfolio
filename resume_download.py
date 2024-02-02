import streamlit as st

def resume_download():
    st.markdown("### To Download Resume Click the ***Download file*** Button and then click ***Click to Download*** button ")
    
    # Data to be saved to the file
    file_content = "Hello, this is the content of the file."

    # Display a button for downloading the file
    if st.button("Download File"):
        
        st.download_button(
            label="Click to Download",
            data=file_content,
            key="download_button",
            file_name="Resume.pdf",
            mime="text/plain"
        )

    
    import base64

    # Function to encode a PDF file to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Function to embed PDF using HTML
    def embed_pdf_viewer(pdf_file, width=700, height=600):
        pdf_base64 = get_base64_of_bin_file(pdf_file)
        pdf_viewer_html = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="{width}" height="{height}" style="border: none;"></iframe>'
        return pdf_viewer_html

    # Replace 'your_pdf_file.pdf' with the actual name of your PDF file
    pdf_file_path = 'Resume.pdf'

    # Display the PDF viewer
    pdf_viewer_html = embed_pdf_viewer(pdf_file_path)
    st.markdown(pdf_viewer_html, unsafe_allow_html=True)
