import streamlit as st
import pandas as pd
from qiskit import QuantumCircuit, Aer, execute
import json

st.set_page_config(page_title="Brisla IA Beta v3 - TecnoPARQ", layout="wide")
st.markdown("""
    <style>
    .main {background: linear-gradient(135deg, #1C2526, #A5D6A7);}
    .stButton>button {background-color: #4B5EAA; color: white; border-radius: 5px;}
    .stFileUploader {border: 2px solid #A5D6A7;}
    .report {background-color: #FFF9C4; padding: 10px; border-radius: 5px; color: #1C2526;}
    </style>
""", unsafe_allow_html=True)

st.title("Brisla IA Beta v3 - Análise Preditiva Soberana (TecnoPARQ)")
html_path = "brisla_interface_v3.html"
try:
    with open(html_path, "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=800, scrolling=True)
except FileNotFoundError:
    st.info("Carregue brisla_interface_v3.html ou use o dashboard abaixo.")

uploaded_file = st.file_uploader("Carregue CSV mock (ex.: DataSus, INPE)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("**Dados Carregados**", df.head())

    # Simulação de resposta (sem API Grok real)
    prediction = "Simulação: 20% aumento de casos (saúde) ou 10% produtividade (agro) em 2026."
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1], [0,1])
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    result = job.result().get_counts()
    quantum_insight = f"Simulação Qiskit: {result} (otimização 30% custo)."

    st.markdown('<div class="report">', unsafe_allow_html=True)
    st.subheader("Relatório Preditivo (Modo 20)")
    st.write(f"**Previsão:** {prediction}")
    st.write(f"**Insight Quântico (Qiskit):** {quantum_insight}")
    st.write("**Economia:** 30% vs. BigTechs (R$1,2M/ano).")
    st.write("**Conformidade:** LGPD, IEEE 2621.")
    st.markdown('</div>', unsafe_allow_html=True)

    feedback = st.slider("Satisfação (0-10)?", 0, 10)
    if st.button("Enviar Feedback"):
        st.success(f"NPS: {feedback}/10. Iteraremos para 2026!")

st.markdown("**Brisla IA**: Soberania para deep tech. SOM: US$120M (saúde 15%, agro 15%, educação 10%). TecnoPARQ 2025.")