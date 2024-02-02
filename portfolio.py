import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
from embedded_buttons import *
from Homepage import *
from projects import *
from contact_form import *
from resume_download import *

# if st.session_state.get('switch_button', False):
#     st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
#     manual_select = st.session_state['menu_option']
# else:
#     manual_select = None
    
# selected4 = option_menu(None, ["Home", "Upload", "Projects", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     orientation="horizontal", manual_select=manual_select, key='menu_4')
# st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
# selected4

# 1. as sidebar menu
with st.sidebar:
    selected4 = option_menu("Select Page", ["Home", "Projects", "Resume"], 
        icons=['house','github','download'], menu_icon="cast", default_index=0)
    selected4


if selected4 == "Home":
    homepage()

    if st.session_state.get('switch_button', False):
        st.session_state['repo_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
        manual_select = st.session_state['repo_option']
    else:
        manual_select = None
        
    selected2 = option_menu(None, ["Contact me", "My Projects"], 
    icons=['mail', 'github',], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    selected2

    if selected2=="My Projects":
        project()

    if selected2 =="Contact me":
        contact_form()

    


if selected4 == "Upload":
    st.file_uploader(" Upload your file")

if selected4 =="Projects":
    project()


with st.sidebar:
    st.button("Contact me",contact_form())



if selected4=="Resume":
   resume_download()