import streamlit as st
import cohere
api_key = 'GqsxZlKmcBzSultkVOfKPf7kVhYkporXvivq9KHg'

# 初期設定
st.set_page_config(page_title="cohere embedding", layout="centered")

co = cohere.Client(api_key)
#co.check_api_key()

res_embed = co.embed(
    texts=['BRICSの首脳会議の全体会合が23日、ロシアで開かれ、ウクライナ侵攻でロシアが欧米などから制裁を科されていることを念頭に「国際法に反する一方的な経済制裁の撤廃を求める」などとした内容を盛り込んだ宣言を採択しました。ロシア中部の都市カザンで23日、エジプトやイランなどが加わって加盟国が拡大してから初めてとなるBRICSの首脳会議の全体会合が開かれました。', '11月5日の米大統領選投開票まで2週間足らずとなり、民主党候補のハリス副大統領と共和党候補のトランプ前大統領が引き続き異例の大接戦を繰り広げている。激戦州を対象にブルームバーグ・ニュースとモーニング・コンサルトが実施した最新の世論調査で示された。ロシア中部の都市カザンで23日、エジプトやイランなどが加わって加盟国が拡大してから初めてとなるBRICSの首脳会議の全体会合が開かれました。10月16－20日に７州の登録有権者計5308人を対象にオンラインで実施した調査によれば、いずれの州でも投票に行く可能性のある有権者の間で両候補が統計上タイとなっている。広告や集会、投票を呼び掛ける戸別訪問といった選挙戦最終盤の攻勢が勝敗を左右する可能性を浮き彫りにした。'],
    model='embed-multilingual-v2.0'
)

st.write(res_embed)

co_summarize = co.summarize(
    text=texts[0]
)

st.write(co_summarize)
