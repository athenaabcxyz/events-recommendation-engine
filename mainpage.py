import streamlit as st


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

st.switch_page("pages/list_page.py")