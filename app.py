# app.pyという名前で保存

import streamlit as st

def main():
    st.title('こんにちは！Streamlit')
    if st.button('押してね'):
        st.write('ボタンが押されました！')

if __name__ == '__main__':
    main()