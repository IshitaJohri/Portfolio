from PIL import Image
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Ishita Johri", layout="centered", page_icon="ℹ️")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- STYLING ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def _max_width_(prcnt_width:int = 75):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(f""" 
                <style> 
                .reportview-container .main .block-container{{{max_width_str}}}
                </style>    
                """, 
                unsafe_allow_html=True,
    )
_max_width_(65)
def hide_anchor_link():
    st.markdown("""
        <style>
        .css-eczf16 {display: none}
        </style>
        """, unsafe_allow_html=True)
  
hide_anchor_link()

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_url = "https://assets8.lottiefiles.com/packages/lf20_1LhsaB.json"
lottie_json = load_lottieurl(lottie_url)
img_gmail = Image.open("images/image.png")

# ---- SCROLL TO TOP  ----
if "counter" not in st.session_state:
    st.session_state.counter = 1

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi! I'm Ishita :cat:")
    st.markdown("<h1 style='text-align: center;'>I enjoy making fun and interactive things. Doing so helps me to visualise problems and solve them.</h1>", unsafe_allow_html=True)

# ---- BODY ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            I am a pre-final year undergraduate student in Electrical and Electronics Engineering. My interests are in building, organizing my ideas into fun and practical things using creative coding.

            In my free time, you can find me reading mystery-thrillers, watching documentaries, and ocassionally making candles.

            Fun-Fact about me: I am also pursuing a Bachelor of Science in Data Science from Indian Institute of Technology, Madras
            """
        )
    with right_column:
        st.write("##")
        st_lottie(lottie_json, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My latest project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_gmail)
    with text_column:
        st.subheader("Classic Flappy Bird Game")
        st.write(
            """
            If you're like me and have ever come across this android's easter egg then this game would surely be familiar to you. The OG Flappy Bird game sparked countless clones and here is my small effort to learn something from it.
            """
        )
        st.markdown("[Check it out >>](https://github.com/IshitaJohri/Flappy-Bird-game)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>👵🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Thanks for stopping by!</h3>", unsafe_allow_html=True)
    st.write("##")
with st.container():
    col1, col2, col3, col4, col5= st.columns((2.25,1,1,1,2))
    with col1:
        st.empty()
    with col2:
        st.write("[Email](mailto:Ishitajohri.ij@gmail.com)")
    with col3:
        st.write("[LinkedIn](https://www.linkedin.com/in/ishitajohri/)")
    with col4:
        st.write("[GitHub](https://github.com/IshitaJohri)")
    with col5:
        st.empty()
with st.container():
    st.write("##")
    col1, col2, col3= st.columns((4.5,2,4))
    with col1:
        st.empty()
    with col2:
        if st.button("Back to Top"):
            st.session_state.counter += 1
    with col3:
        st.empty()

with st.container():
    st.write("##")
    col1, col2= st.columns((1.75,5))
    
    with col1:
        st.write("session state counter: ")
    with col2:
        st.write(st.session_state.counter)

components.html(
    f"""
        <p>{st.session_state.counter}</p>
        <script>
            window.parent.document.querySelector('section.main').scrollTo(0, 0);
        </script>
    """,
    height=0
)