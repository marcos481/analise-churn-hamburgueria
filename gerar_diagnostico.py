import os
import json
import time
import pandas as pd
import matplotlib.pyplot as plt
from google import genai
from google.genai import types

# 1. Conecta à IA usando a variável de ambiente salva no terminal
client = genai.Client()

print("Lendo os dados brutos de vendas e reclamações...")
df = pd.read_excel("vendas_e_reclamacoes.xlsx")

# 2. Cálculos Financeiros pelo Pandas (Maio vs Junho)
df['Data'] = pd.to_datetime(df['Data'])
df['Mes'] = df['Data'].dt.strftime('%B')

faturamento_maio = df[df['Mes'] == 'May']['Valor_Gasto'].sum()
faturamento_junho = df[df['Mes'] == 'June']['Valor_Gasto'].sum()
queda_faturamento = faturamento_maio - faturamento_junho

# 3. Consultoria Cognitiva com o Gemini
prompt_sistema = """
Você é um consultor analista de Churn focado em restaurantes. 
Com base nos dados de faturamento e na lista de comentários de clientes fornecida, 
gere um parecer executivo curto para o dono da hamburgueria contendo:
1. Resumo financeiro do impacto (Maio vs Junho).
2. A causa-raiz que mais fez clientes abandonarem a marca em Junho.
3. Duas ações urgentes e de baixo custo para reverter isso imediatamente nesta semana.
Tone de voz: Direto, profissional e focado em soluções.
"""

# Junta todos os feedbacks para a IA ler de uma vez só e gerar o parecer consolidado
todos_feedbacks = "\n".join(df['Feedback_Cliente'].tolist())
dados_consolidados = f"Faturamento Maio: R${faturamento_maio} | Faturamento Junho: R${faturamento_junho}\nFeedbacks:\n{todos_feedbacks}"

print("Solicitando à Inteligência Artificial a criação do diagnóstico executivo...")
resposta = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[prompt_sistema, dados_consolidados]
)

# Salva o texto da assessoria
with open("relatorio_churn.txt", "w", encoding="utf-8") as f:
    f.write(resposta.text)

print("Relatório salvo em 'relatorio_churn.txt'!")

# 4. Geração do Gráfico Comercial com Matplotlib
print("Gerando gráfico financeiro de evolução...")
meses_grafico = ["Maio", "Junho"]
valores_grafico = [faturamento_maio, faturamento_junho]

plt.figure(figsize=(6, 4))
# Cria o gráfico de barras comparativo
barras = plt.bar(meses_grafico, valores_grafico, color=['#2ca02c', '#d62728'], width=0.5)

plt.title("Queda de Faturamento (Impacto Operacional)", fontsize=14, fontweight='bold', pad=15)
plt.ylabel("Faturamento Bruto (R$)", fontsize=11)
plt.ylim(0, max(valores_grafico) + 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adiciona o valor em cima de cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 15, f"R$ {altura:.2f}", ha='center', va='bottom', fontweight='bold')

plt.savefig("grafico_churn.png", dpi=300, bbox_inches='tight')
print("[SUCESSO] Gráfico 'grafico_churn.png' gerada com sucesso!")
