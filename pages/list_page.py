import streamlit as st
import requests
from app import rewriteGroup

def filterEvent(text_input):
    if (text_input==""):
        text_input=" "
    url = "http://127.0.0.1:5000/api/filter/{}".format(text_input)
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
st.header("Current Available Events Ticket")  
text_input = st.text_input("Type to search for events")
filterer_id = filterEvent(text_input)
groups = rewriteGroup(filterer_id)

cols = st.columns(3)
for group in groups:
    for i, id in enumerate(group):
        name, image_url, venues, startTime, info = fetch_id(id)
        cols[i].image(image_url)
        if cols[i].button(name, key = id, use_container_width = True):
            st.session_state['key'] = id
            st.switch_page("pages/detail_page.py")
        cols[i].text('\n')