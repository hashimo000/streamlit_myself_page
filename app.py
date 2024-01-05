# ターミナルで `streamlit run your_script.py` を実行します。
import streamlit as st
import datetime

# タイトルの設定
st.title('私の自己紹介')

# テキストを追加
st.write("こんにちは！私の名前は橋本瑞樹です。")

# 画像の追加
st.image('S__101130247.jpg', caption='画像')
# サイドバーの使用
with st.sidebar:
    st.write("ホーム")
    st.write("お問い合わせ")
    st.write("その他")

# テキスト入力で名前を尋ねる
name = st.text_input('あなたの名前は何ですか？')

# 日付入力
birthday = st.date_input("あなたの誕生日は？")

# 年齢を計算して表示
if birthday is not None:
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    st.write(f"あなたは {age} 歳です！")

# セレクトボックスを使用して好きな食べ物を尋ねる
food = st.selectbox('好きな食べ物は何ですか？', ('寿司', 'ラーメン', 'カレー'))
st.write(f'あなたは {food} が好きですね！')

# スライダーを使って気分を尋ねる
mood = st.slider('今の気分は？', 0, 100, 50)
st.write(f'あなたの気分: {mood}')

# ボタンを使ってアクションを実行
if st.button('挨拶'):
    st.write(f'こんにちは、{name}さん！')
