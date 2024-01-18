import streamlit as st
import json

def load_json(file):
    try:
        data = json.load(file)
        questions_answers = data.get('perguntas', [])
        return questions_answers
    except Exception as e:
        st.error(f"Erro ao carregar perguntas e respostas: {str(e)}")
        return []

def check_answer(user_answer, question):
    type = question.get('tipo')
    correct_answer = question.get('resposta_correta', [])

    if correct_answer is None or user_answer is None:
        return False

    if type == 'verdadeiro_falso' or type == 'multipla_escolha':
        return correct_answer.lower() == user_answer.lower()
    else:
        return correct_answer.lower() == user_answer.lower()

def show_question(questions_answers, question_index):
    question_answer = questions_answers[question_index]

    type = question_answer.get('tipo')
    question_text = question_answer.get('texto')
    user_answer = ""

    if type == 'verdadeiro_falso':
        st.text(f"Chico: {question_text}")
        user_answer = st.radio("Escolha uma opção:", ["Verdadeiro", "Falso"], key=f"resposta_{question_index}", index=None)
    elif type == 'multipla_escolha':
        st.text(f"Chico: {question_text}")
        options = question_answer.get('opcoes', [])
        user_answer = st.selectbox("Escolha a opção correta:", ["Clique aqui para selecionar sua resposta"] + options)
    else:
        st.text(f"Chico: {question_text}")
        user_answer = st.text_input("Sua Resposta:", key=f"resposta_{question_index}", value=user_answer)

    return user_answer

def main():
    st.title("Bem Vindo ao Bot Chico! 🤖")

    assistant_message = st.empty()
    with assistant_message:
        st.write("Olá, você gostaria de realizar um questionário? 🤓 ")

    radio = st.empty()
    with radio:
        response_invite = st.radio("Maque aqui ⬇️ ", ["Sim", "Não"], index=None)

    if response_invite == "Sim":
        assistant_message.empty()
        radio.empty()
        assistant_message_2 = st.empty()
        with assistant_message_2:
            st.write("Que ótimo! 😍 Carregue um arquivo JSON clicando em Browse files para iniciar.")

        uploaded_file = st.file_uploader("Carregar arquivo JSON", type=["json"])
        current_file = st.session_state.get('current_file', None)
        if uploaded_file:
            assistant_message_2.empty()

        if uploaded_file is not None and uploaded_file != current_file:
            st.session_state.question_index = 0
            st.session_state.quiz_completed = False
            st.session_state.score = 0
            st.session_state.user_answers = []
            st.session_state.current_file = uploaded_file

        if uploaded_file is not None:
            questions_answers = load_json(uploaded_file)
            if not questions_answers:
                st.warning("Arquivo JSON inválido ou sem perguntas. Por favor, carregue um arquivo válido.")

            total_questions = len(questions_answers)
            question_index = st.session_state.get('question_index', 0)
            quiz_completed = st.session_state.get('quiz_completed', False)

            user_answer = ""

            if not quiz_completed:
                if question_index < total_questions:
                    user_answer = show_question(questions_answers, question_index)

                    if st.button(f"Confirmar Resposta {question_index + 1}"):
                        st.session_state.user_answers.append(user_answer)

                        question_index += 1
                        st.session_state.question_index = question_index

                        if question_index == total_questions:
                            calculate_score(questions_answers)
                            st.session_state.quiz_completed = True
                        st.experimental_rerun()
            else:
                st.text(f"Chico: Questionário concluído! 🎉 A sua Pontuação é: {st.session_state.score}")

                results = {
                    'questions_answers': questions_answers,
                    'user_answers': st.session_state.user_answers,
                    'score': st.session_state.score
                }

                json_string = json.dumps(results, indent=2, ensure_ascii=False)

                if st.button("Baixar Respostas em JSON"):
                    st.download_button(
                        label='Baixar respostas',
                        data=json_string,
                        file_name='respostas.json',
                        mime='application/json'
                    )
                if st.button("Refazer Questionário"):
                    st.session_state.question_index = 0
                    st.session_state.quiz_completed = False
                    st.session_state.score = 0
                    st.session_state.current_file = None
                    st.experimental_rerun()
        else:
            if st.session_state.get('first_run', True):
                st.session_state.first_run = False
                st.session_state.question_index = 0

def calculate_score(questions_answers):
    for i, user_answer in enumerate(st.session_state.user_answers):
        if check_answer(user_answer, questions_answers[i]):
            st.session_state.score += 1

if __name__ == "__main__":
    main()
