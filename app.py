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
  "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. "
  "It may be made from milk or cream and is flavoured with a sweetener, "
  "either sugar or an alternative, and a spice, such as cocoa or vanilla, "
  "or with fruit such as strawberries or peaches. "
  "It can also be made by whisking a flavored cream base and liquid nitrogen together. "
  "Food coloring is sometimes added, in addition to stabilizers. "
  "The mixture is cooled below the freezing point of water and stirred to incorporate air spaces "
  "and to prevent detectable ice crystals from forming. The result is a smooth, "
  "semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). "
  "It becomes more malleable as its temperature increases.\n\n"
  "The meaning of the name \"ice cream\" varies from one country to another. "
  "In some countries, such as the United States, \"ice cream\" applies only to a specific variety, "
  "and most governments regulate the commercial use of the various terms according to the "
  "relative quantities of the main ingredients, notably the amount of cream. "
  "Products that do not meet the criteria to be called ice cream are sometimes labelled "
  "\"frozen dairy dessert\" instead. In other countries, such as Italy and Argentina, "
  "one word is used fo\r all variants. Analogues made from dairy alternatives, "
  "such as goat's or sheep's milk, or milk substitutes "
  "(e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are "
  "lactose intolerant, allergic to dairy protein or vegan."
)

co_summarize = co.summarize(
    text=text
)

st.write(co_summarize)
