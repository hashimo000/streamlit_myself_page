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




# セッション状態の使用
if 'greeted' not in st.session_state:
    st.session_state['greeted'] = False

# ボタンを使ってアクションを実行
if st.button('挨拶'):
    st.session_state['greeted'] = True
    st.experimental_rerun()

# メッセージの表示
if st.session_state['greeted']:
      st.markdown('<style>p.big-font {font-size: 30px;}</style><p class="big-font">Welcome to my Page!</p>', unsafe_allow_html=True)
