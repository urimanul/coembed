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

text = (
  "経済産業省は、ヘルスケア産業政策を通じて、超高齢社会における様々な課題に取り組んでいます。まず、急速な高齢化が進む中、社会保障費が増加し、これが財政に圧力をかけ、労働力の減少が経済活動を停滞させる懸念があることが指摘されています。特に、65歳以上の高齢者人口が横ばいである一方、若年層の減少が進んでいることが問題視されています。現在、社会保障給付費は年々増加しており、医療給付費と介護給付費の両方が2025年度に大幅に増加する見込みです。 次に、経済産業省は健康経営や健康投資を推進し、企業が従業員の健康を重視することで生産性の向上を目指しています。また、地域においては、ヘルスケア産業の創出を促進し、地域経済の活性化を図る施策が進められています。健康・医療情報の活用も重要なテーマであり、データの収集と分析を通じて、より良い医療サービスの提供を目指しています。 医療の国際展開に関しては、日本の医療技術や製品を海外市場に展開する取り組みが進んでいます。これにより、日本の医療機器産業の競争力を高めることが期待されています。認知症や介護予防に関しても、国民の健康寿命を延ばすための施策が必要とされています。さらに、ビジネスコンテストなどを通じて新たなアイデアや技術の開発が奨励されています。 医療機器産業の重点分野としては、手術支援、人工組織・臓器、低侵襲治療、イメージング、在宅医療機器が挙げられます。これらの分野では、国内企業の技術力を活用しながら、世界水準の医療機器の開発が進められています。特に、ロボット技術や3Dプリンティングなどの先端技術の応用が期待されています。 最後に、経済産業省は医療機器産業の全体像を描き、市場開拓や開発・治験、販売プロセスを通じて、海外市場の獲得を目指しています。産学官の連携を強化し、臨床ニーズに基づいた医療機器の開発を進めることで、実用化を図っています。また、海外展開に向けた国際標準化の加速も重要な施策として位置付けられています。"
)

co_summarize = co.summarize(
    text=text,
    model='command-light',
    length='short',
    format='bullets',
    extractiveness='high'
)

st.write(co_summarize)

#cochat = cohere.ClientV2(api_key)
cochat = cohere.Client(api_key)

# ユーザーからの入力を受け取る
user_input = st.text_input("プロンプトを入力して下さい:")

# 入力がある場合にCohereのAPIを呼び出してレスポンスを表示
if user_input:
    response = cochat.chat(
        model="command-r-plus-08-2024",
        messages=[{"role": "user", "content": user_input}],
        connectors=[{"id": "authryh-wfc54k"},{"id": "o365schedule-e4baaa"},{"id": "web-search"}],
    )
    st.write(response.message.content[0].text)
