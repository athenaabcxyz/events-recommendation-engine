import streamlit as st
import requests


def get_recommend(name):
    url = "http://127.0.0.1:5000/api/recommend/{}".format(name)
    data = requests.post(url).json()
    eventList = data["eventList"]
    return eventList

def fetch_id(id):
    url = "http://127.0.0.1:5000/api/fetch/{}".format(id)
    data = requests.post(url).json()
    name = data["name"]
    image_url = data["image"]
    venues = data["venues"]
    startTime = data["startTime"]
    info = data["info"]
    return name, image_url, venues, startTime, info

st.set_page_config(
    page_title="Events Recommendation Engine",
    initial_sidebar_state ='collapsed'
)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
if 'key' not in st.session_state:
    st.session_state['key'] = ''
if(st.session_state['key'] != ''):    
    name, image_url, venues, startTime, info = fetch_id(st.session_state["key"])
    if st.button("Go back"):
        st.switch_page("pages/list_page.py")
    st.header(name)
    st.image(image_url, width=800)
    st.markdown("<h1 style='font-size: 30px;'>Detailed Info:</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 20px;'>Official Event Name:</h1>", unsafe_allow_html=True)
    st.write(name)
    st.markdown("<h1 style='font-size: 20px;'>Location:</h1>", unsafe_allow_html=True)
    st.write(venues)
    st.markdown("<h1 style='font-size: 20px;'>Start Time:</h1>", unsafe_allow_html=True)
    st.write(startTime)
    st.markdown("<h1 style='font-size: 20px;'>Additional Info:</h1>", unsafe_allow_html=True)
    st.write(info)
    st.markdown("<h1 style='font-size: 30px;'>----------------------------------------------------------------------</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 30px;'>You may be also interested:</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    recommend_events_id= get_recommend(name)
    for i in range(3):
        name1, image_url1, venues1, startTime1, info1 = fetch_id(recommend_events_id[i])
        cols[i].image(image_url1)
        if cols[i].button(name1, key = recommend_events_id[i], use_container_width = True):
            st.session_state['key'] = recommend_events_id[i]