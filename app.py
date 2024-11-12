import streamlit as st
import cohere
api_key = 'GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg'

# 初期設定
st.set_page_config(page_title="cohere embedding", layout="centered")

co = cohere.Client(api_key)
#co.check_api_key()

res_embed = co.embed(
    texts=['こんにちは', '世界'],
    model='embed-multilingual-v2.0'
)

st.write(res_embed)
