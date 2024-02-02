import streamlit as st
from streamlit_option_menu import option_menu
from embedded_buttons import *
import webbrowser
from pathlib import Path
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def project():
    selected2 = option_menu(None, ["Emotion Detection Using CNN", "Traffic Signal Violation", "GUI Based Human Tracking and Detection using SSD"], 
    icons=['github', 'github', "github"], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    selected2

    if selected2=="Emotion Detection Using CNN":
        st.title("Emotion Detection using CNN")
        if st.button(" :link: "'Click Here to go to Github Repository'):
            webbrowser.open_new_tab('https://github.com/Shravan1028/Emotion-Detection-using-CNN')

        from pathlib import Path

        def read_markdown_file1(markdown_file):
            return Path(markdown_file).read_text()

        intro_markdown1 = read_markdown_file1("EDUC.md")
        st.markdown(intro_markdown1, unsafe_allow_html=True)
        st.image("imgs_EDUC/accuracy.png")


    if selected2=="Traffic Signal Violation":
        st.title("Traffic Signal Violation Using Yolo")
        if st.button(" :link: "'Click Here to go to Github Repository'):
            webbrowser.open_new_tab('https://github.com/Shravan1028/Traffic-Signal-violation')

        
        from pathlib import Path
        def read_markdown_file2(markdown_file):
            return Path(markdown_file).read_text()

        intro_markdown1 = read_markdown_file2("Traffic.md")
        st.markdown(intro_markdown1, unsafe_allow_html=True)
        
        st.image("Traffic_images/Violation_Detection_Frame.jpg")
        st.image("Traffic_images/Violation_Detection_Frame_Red.jpg")

    if selected2=="GUI Based Human Tracking and Detection using SSD":
        st.title("GUI Based Human Tracking and Detection using SSD")
        if st.button(" :link: "'Click Here to go to Github Repository'):
            webbrowser.open_new_tab('https://github.com/Shravan1028/GUI-Based-Human-Detection-and-Tracking-Using-SSD')

        from pathlib import Path
        def read_markdown_file3(markdown_file):
            return Path(markdown_file).read_text()

        intro_markdown1 = read_markdown_file3("Gui.md")
        st.markdown(intro_markdown1, unsafe_allow_html=True)
        
        st.image("GUI_Images/S1.png")
        st.image("GUI_Images/S2.png")
        st.image("GUI_Images/S3.png")
        st.image("GUI_Images/S4.png")
        st.image("GUI_Images/S5.png")
        st.image("GUI_Images/S6.png")
        st.image("GUI_Images/S7.png")
        

    