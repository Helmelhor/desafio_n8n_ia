import streamlit as st
import requests
import json

# Configuração da página
st.set_page_config(page_title="Doutor Agendas", page_icon="🤖")
st.title("🤖 Doutor Agendas - Facilit Tecnologia")
st.caption("Seu assistente de IA para consulta de agendas da Facilit.")


N8N_WEBHOOK_URL = "http://n8n_automations:5678/webhook/3abb36e0-3571-490f-8208-46b31b5c976b"


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Olá! Como posso ajudar com as agendas da empresa de hoje?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Qual evento você gostaria de consultar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analisando agendas..."):
            try:
                payload = {"pergunta": prompt}
                headers = {"Content-Type": "application/json"}
                response = requests.post(N8N_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
                response.raise_for_status()
                api_response = response.json()
                if isinstance(api_response, list) and api_response:
                    assistant_response = api_response[0].get("resposta", "Não obtive uma resposta clara.")
                elif isinstance(api_response, dict):
                    assistant_response = api_response.get("resposta", "Não obtive uma resposta clara.")
                else:
                    assistant_response = "Recebi uma resposta em um formato inesperado."
            except Exception as e:
                assistant_response = f"Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente."
                st.error(f"Detalhes do erro: {e}")

        st.markdown(assistant_response)
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})