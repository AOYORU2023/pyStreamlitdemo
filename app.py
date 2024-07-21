import streamlit as st
import random

# クイズデータ
quiz_data = [
    {
        "question": "VBAとは何の略称ですか？",
        "choices": ["Visual Basic Algorithm", "Visual Basic for Applications", "Visual Basic Analysis"],
        "correct": 1,
        "explanation": "VBAは「Visual Basic for Applications」の略称です。これはMicrosoft Office製品に組み込まれたプログラミング言語です。"
    },
    {
        "question": "マクロ記録とは何ですか？",
        "choices": ["手動で書いたコードを実行すること", "Excelの操作を自動的に記録する機能", "VBAコードをデバッグする機能"],
        "correct": 1,
        "explanation": "マクロ記録は、ユーザーが行った操作をVBAコードとして自動的に記録する機能です。これにより、繰り返し行う操作を自動化できます。"
    },
    # 他の質問をここに追加...
]

def main():
    st.title("VBAベーシック検定クイズ")

    # セッション状態の初期化
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = len(quiz_data)
    if 'answered' not in st.session_state:
        st.session_state.answered = False

    # 進捗表示
    st.write(f"問題 {st.session_state.current_question + 1} / {st.session_state.total_questions}")

    # 現在の問題を表示
    quiz = quiz_data[st.session_state.current_question]
    st.write(quiz["question"])

    # 選択肢を表示
    choice = st.radio("選択してください:", quiz["choices"], key=f"quiz_{st.session_state.current_question}")

    if st.button("回答する"):
        st.session_state.answered = True
        if quiz["choices"].index(choice) == quiz["correct"]:
            st.success("正解！")
            st.session_state.score += 1
        else:
            st.error(f"不正解。正解は「{quiz['choices'][quiz['correct']]}」です。")
        st.info(quiz["explanation"])

        if st.session_state.current_question < st.session_state.total_questions - 1:
            if st.button("次の問題へ"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.experimental_rerun()
        else:
            st.write("クイズ終了！")
            st.write(f"あなたのスコア: {st.session_state.score} / {st.session_state.total_questions}")
            if st.button("最初からやり直す"):
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.experimental_rerun()

if __name__ == "__main__":
    main()
