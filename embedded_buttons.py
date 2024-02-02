import streamlit as st
import base64


def linked_button():
    st.markdown(
        """<a href="https://www.linkedin.com/in/shravan-singh-b011b9209/">
        <img src="data:image/png;base64,{}" width="25">
        </a>""".format(
            base64.b64encode(open("linkedin.gif", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )


def portfolio_button():
    st.markdown(
        """<a href="https://bt-portfolio-nmfg.vercel.app/">
        <img src="data:image/png;base64,{}" width="25">
        </a>""".format(
            base64.b64encode(open("portfolio1.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
        

def github_button():
    st.markdown(
        """<a href="https://github.com/Shravan1028">
        <img src="data:image/png;base64,{}" width="25">
        </a>""".format(
            base64.b64encode(open("github.gif", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
        

def mail_button():
    st.markdown(
        """<a href="shravansingh80001@gmail.com">
        <img src="data:image/png;base64,{}" width="25">
        </a>""".format(
            base64.b64encode(open("mail.gif", "rb").read()).decode()
        ),
        unsafe_allow_html=True,
    )
        
def project1():
    '''
            
        [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/Shravan1028/Emotion-Detection-using-CNN) 

    '''
    st.markdown("<br>",unsafe_allow_html=True)

