import random

# Converte valor booleano em "V" (Verdadeiro) ou "F" (Falso)
def valor_para_str(b):
    return "V" if b else "F"

# Converte string "V" ou "F" para valor booleano True ou False
def str_para_valor(str):
    return str.upper() == "V"

# === Funções para as expressões lógicas ===
def expr_and(p, q, r): return p and q
def expr_or(p, q, r): return p or q
def expr_notp_or_q(p, q, r): return (not p) or q
def expr_impl(p, q, r): return (not p) or q
def expr_bicond(p, q, r): return p == q
def expr_not_p(p, q, r): return not p
def expr_not_q(p, q, r): return not q
def expr_and_notq(p, q, r): return p and not q
def expr_xor(p, q, r): return p != q
def expr_and_or(p, q, r): return (p and q) or r
def expr_and_qorr(p, q, r): return p and (q or r)

# Matriz de expressões com funções nomeadas
expressoes = [
    # Cada item da lista é uma expressão lógica representada por:
    # [Texto da expressão, função que avalia a expressão, variáveis utilizadas]

    # Expressão: P AND Q
    ["P AND Q",        expr_and,       ["P", "Q"]],        # Verdadeira somente se P e Q forem verdadeiros

    # Expressão: P OR Q
    ["P OR Q",         expr_or,        ["P", "Q"]],        # Verdadeira se pelo menos um entre P ou Q for verdadeiro

    # Expressão: (NOT P) OR Q
    ["(NOT P) OR Q",   expr_notp_or_q, ["P", "Q"]],        # Equivalente à implicação P → Q

    # Expressão: P -> Q (implicação)
    ["P -> Q",         expr_impl,      ["P", "Q"]],        # Também representa P → Q (mesmo comportamento da anterior)

    # Expressão: P <-> Q (bicondicional)
    ["P <-> Q",        expr_bicond,    ["P", "Q"]],        # Verdadeira se P e Q tiverem o mesmo valor (ambos V ou ambos F)

    # Expressão: NOT P
    ["NOT P",          expr_not_p,     ["P"]],             # Verdadeira se P for falso

    # Expressão: NOT Q
    ["NOT Q",          expr_not_q,     ["Q"]],             # Verdadeira se Q for falso

    # Expressão: P AND (NOT Q)
    ["P AND (NOT Q)",  expr_and_notq,  ["P", "Q"]],        # Verdadeira se P for verdadeiro e Q for falso

    # Expressão: P XOR Q
    ["P XOR Q",        expr_xor,       ["P", "Q"]],        # Verdadeira se apenas um entre P ou Q for verdadeiro (exclusivo)

    # Expressão: (P AND Q) OR R
    ["(P AND Q) OR R", expr_and_or,    ["P", "Q", "R"]],   # Verdadeira se P e Q forem verdadeiros ou se R for verdadeiro

    # Expressão: P AND (Q OR R)
    ["P AND (Q OR R)", expr_and_qorr,  ["P", "Q", "R"]],   # Verdadeira se P for verdadeiro e pelo menos um entre Q ou R também for
]


# Gera valores aleatórios para P, Q e R
def gerar_valores():
    return {
        "P": random.choice([True, False]),
        "Q": random.choice([True, False]),
        "R": random.choice([True, False])
    }

# Monta a pergunta a ser exibida
def montar_pergunta(variaveis, valores, texto):
    partes = []
    for v in variaveis:
        partes.append(f"{v} = {valor_para_str(valores[v])}")
    return f"{', '.join(partes)}, qual o resultado de {texto}?"

# Função principal do jogo
def jogar():
    pontos = 0
    rodadas = 5

    print("Bem-vindo ao Jogo da Tabela Verdade!\n")
    print("Responda se a expressão lógica é Verdadeira (V) ou Falsa (F).\n")

    for i in range(rodadas):
        print(f"--- Rodada {i+1}/{rodadas} ---")

        valores = gerar_valores()
        texto, func, usados = random.choice(expressoes)

        pergunta = montar_pergunta(usados, valores, texto)
        print(pergunta)

        p = valores.get("P", False)
        q = valores.get("Q", False)
        r = valores.get("R", False)
        resultado = func(p, q, r)

        while True:
            resposta = input("Sua resposta (V/F): ").strip().upper()
            if resposta in ["V", "F"]:
                break
            print("Digite apenas V ou F.")

        if str_para_valor(resposta) == resultado:
            print("Correto!")
            pontos += 1
        else:
            print(f"Errado. A resposta correta era {valor_para_str(resultado)}.")

        print("-" * 30)

    print("\nFim do Jogo!")
    print(f"Pontuação final: {pontos}/{rodadas}")

    if pontos == rodadas:
        print("Parabéns! Você acertou todas! Você é mesmo um mestre da lógica!")
    elif pontos >= rodadas * 0.7:
        print("Muito bem! Você está indo bem.")
    elif pontos >= rodadas * 0.4:
        print("Continue praticando!")
    else:
        print("Não desanime! Estude mais e tente de novo.")

    print("Obrigado por jogar!\n")

# Inicia o jogo
jogar()
