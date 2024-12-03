import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import requests
import pandas as pd

# رابط الواجهة البرمجية (افتراضي)
api_url = "https://example-tickerchart-api.com/data"

# جلب البيانات
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write("البيانات:", df)
else:
    st.error("فشل في جلب البيانات!")
