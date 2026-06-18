import pandas as pd

print("Gerando base de dados simulada para o Projeto Hamburgueria...")

dados_vendas = {
    "ID_Pedido": list(range(101, 121)),
    "Data": [
        "2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02", "2026-05-03",
        "2026-05-04", "2026-05-05", "2026-05-05", "2026-05-06", "2026-05-07",
        "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03", "2026-06-04",
        "2026-06-05", "2026-06-06", "2026-06-06", "2026-06-07", "2026-06-07"
    ],
    "Cliente": [
        "Marcos Almeida", "Sofia Rodrigues", "Lucas Nogueira", "Beatriz Lima", "Thiago Silva",
        "Amanda Rocha", "Rodrigo Souza", "Larissa Dias", "Gabriel Jesus", "Camila Alves",
        "Roberto Carlos", "Daniela Mercury", "Fabio Assuncao", "Gisele Bundchen", "Neymar Junior",
        "Ivete Sangalo", "Caetano Veloso", "Anitta Spfc", "Gilberto Gil", "Luisa Sonza"
    ],
    "Item_Pedido": [
        "Combo Smash Burger", "Duplo Bacon", "X-Salada Clássico", "Combo Monster", "Batata Suprema",
        "Combo Smash Burger", "Duplo Bacon", "X-Burger", "Combo Monster", "Combo Smash Burger",
        "Combo Smash Burger", "Duplo Bacon", "Combo Monster", "X-Salada Clássico", "Duplo Bacon",
        "Combo Smash Burger", "Batata Suprema", "Combo Monster", "X-Burger", "Duplo Bacon"
    ],
    "Valor_Gasto": [
        45.00, 38.00, 28.00, 55.00, 22.00, 45.00, 38.00, 25.00, 55.00, 45.00,
        45.00, 38.00, 55.00, 28.00, 38.00, 45.00, 22.00, 55.00, 25.00, 38.00
    ],
    "Feedback_Cliente": [
        "Muito bom! Hambúrguer suculento e entrega no prazo.",
        "O bacon estava perfeito, bem crocante. Recomendo.",
        "Lanche simples, mas bem feito. Preço honesto.",
        "Amei o molho da casa, parabéns pelo capricho.",
        "Batata frita deliciosa e quentinha.",
        "O ponto da carne veio perfeito, voltarei a pedir.",
        "Tudo ótimo, entrega super rápida pelo app.",
        "Lanche gostoso, mas achei que veio pouca batata.",
        "Gostei bastante, combo bem completo.",
        "O lanche é gostoso, mas a maionese veio errada.",
        "O lanche é maravilhoso, mas o motoqueiro demorou quase 1 hora para entregar e chegou frio.",
        "Tentei mandar mensagem no WhatsApp para reclamar do atraso e ninguém respondeu o dia todo. Desisti.",
        "Péssima experiência em Junho. O motoboy foi extremamente grosseiro e a embalagem veio rasgada.",
        "Comprei o combo e a carne veio totalmente torrada e seca. Impossível de comer.",
        "Sempre pedi aqui, mas o lanche deste mês veio sem o queijo e o refrigerante veio quente. O padrão caiu.",
        "A comida é boa, mas esperar 1h20 por um hambúrguer em plena terça-feira não dá.",
        "O atendimento do suporte foi péssimo quando perguntei sobre a demora do meu pedido.",
        "Fiquei decepcionada. O lanche veio errado e frio. O serviço de entrega de vocês piorou muito.",
        "Infelizmente o pedido veio trocado. Pedi X-Burger e veio outra coisa. Demorou para trocar.",
        "O hambúrguer estava frio e o motoboy não queria subir até a portaria."
    ]
}

df = pd.DataFrame(dados_vendas)
df.to_excel("vendas_e_reclamacoes.xlsx", index=False)
print("[SUCESSO] Planilha 'vendas_e_reclamacoes.xlsx' gerada!")
