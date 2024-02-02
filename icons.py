# import streamlit as st
# import base64

# def render_svg(svg):
#     """Renders the given svg string."""
#     b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
#     html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
#     c = st.container()
#     c.write(html, unsafe_allow_html=True)

# render_svg(open("icons/adobexdicon.svg").read())


import streamlit as st
import base64
from streamlit.components.v1 import html

def render_svg(svg_string):
    """Renders the given svg string."""
    c = st.container()
    with c:
        html(svg_string)



def skills_page():
    col1, col2, col3, col4 = st.columns([1,1.1,1,1.7,])
    with col1:
        st.markdown(" ## ***Python***")
        render_svg(open("icons/python-icon.svg").read())
        st.markdown(" ## ***Github***")
        render_svg(open("icons/githubicon.svg").read())
        st.markdown(" ## ***Linux***")
        render_svg(open("icons/linuxicon.svg").read())
        st.markdown(" ## ***Opencv***")
        render_svg(open("icons/opencvicon.svg").read())


    with col2:
        st.markdown(" ## ***C++***")
        render_svg(open("icons/cppicon.svg").read())
        st.markdown(" ## ***Numpy***")
        render_svg(open("icons/numpyicon.svg").read())
        st.markdown(" ## ***CNN***")
        render_svg(open("icons/cnnicon.svg").read())
        st.markdown(" ## ***Photoshop***")
        render_svg(open("icons/photoshopicon.svg").read())


    with col3:
        st.markdown(" ## ***Java***")
        render_svg(open("icons/javaicon.svg").read())
        st.markdown(" ## ***Django***")
        render_svg(open("icons/djangoicon.svg").read())
        st.markdown(" ## ***Tensorflow***")
        render_svg(open("icons/tensorflowicon.svg").read())
        st.markdown(" ## ***Canva***")
        render_svg(open("icons/canvaicon.svg").read())
        
        