import streamlit as st
from streamlit_option_menu import option_menu
import webbrowser
from embedded_buttons import *
from image import *
from icons import *


def homepage():
    image()
    #st.image("Shravan.jpg", caption="Shravan Singh", width=660)

    st.title("Hi I am Shravan Vijaypratap Singh")

    st.markdown("---")
    col1, col2, col3,col4 = st.columns([1,1,1,1])
    with col1:
        # if st.button('Portfolio'):
        #     webbrowser.open_new_tab('https://bt-portfolio-nmfg.vercel.app/')
        portfolio_button()
        

    with col2:
        # if st.button('Github'):
        #     webbrowser.open_new_tab('https://github.com/Shravan1028')

    #     '''
    # [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Shravan1028) 

    # '''
    #     st.markdown("<br>",unsafe_allow_html=True)
        github_button()

    with col3:
        # if st.button('LinkedIN'):
        #     webbrowser.open_new_tab('https://www.linkedin.com/in/shravan-singh-b011b9209/')
    #     '''
    # [![Linkedin](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.sv)(https://github.com/Shravan1028) 

    # '''
    #     st.markdown("<br>",unsafe_allow_html=True)
            
        linked_button()
        
    with col4:
        # if st.button('Mail'):
        #     webbrowser.open_new_tab('shravansingh80001@gmail.com')

#     '''
#     [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Shravan1028) 

# '''
#     st.markdown("<br>",unsafe_allow_html=True)

    # st.markdown("[Portfolio](https://bt-portfolio-nmfg.vercel.app/)")
    # st.markdown("[Github](https://github.com/Shravan1028)")
    # st.markdown("[Linkedin](https://www.linkedin.com/in/shravan-singh-b011b9209/)")
    # st.markdown("[Mail](shravansingh80001@gmail.com)")
        mail_button()

    st.markdown("---")
    
    st.header("I am an AI Engineer")
    st.subheader("B Tech in Artificial Intelligence, Honors in Data Science")



    #markdown function in python

    st.markdown(" --- ")
    st.markdown(" # Summary")

    st.text("I am Shravan Vijaypratap Singh pursuing my B tech in Artificial Intelligence and  \nHonors in Data Science from G.H Raisoni college of Engineering and Management, Pune. \nI have Cgpa of 9.19.")

    st.markdown(" --- ")


    st.markdown(" # Education")

    selected2 = option_menu(None, ["Graduation", "HSC", "SSC"], 
    icons=['mortarboard-fill', 'mortarboard-fill', "mortarboard-fill" ], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    selected2

    if selected2=="Graduation":
        st.markdown(" > ## *Bachelor's of  Technology*")
        st.markdown(" **G.H Raisoni College of Engineering and Management, Pune** ")
        st.markdown("Stream: ***Artificial Intelligence***")
        st.markdown("Honors: ***Data Science*** ")
        st. markdown(" >*cgpa: 9.19* ")

    if selected2=="HSC":
        st.markdown(" > ## *Higher Secondary School Certificate.*")
        st.markdown(" **Gopal Krishna Gokhale College, Kolhapur** ") 
        st. markdown(" >*Percentage:66..61%* ")

    
    if selected2=="SSC":
        st.markdown(" > ## *Secondary School Certificate.*")
        st.markdown(" **Sou.Ambubai Patil Englsih Medium Schools, Kolhapur** ")
        st.markdown(" >*Percentage:83.20%* ")

    st.markdown("---")

    st.markdown(" # Skills")

    #caption function in python

    # st.caption(" Example of caption")

    # st.markdown("---")

    
    #code Function in Streamlit
    # code="""
    # import streamlit as st
    
    # if selected==home:
    #     homepage()

    # """

    # st.code(code, language="python")

    # st.markdown("---")

    #st.text_area('Input',"Enter Your Input")

    st.markdown(" # Skills")
    
    skills_page()

    
