from ollama import Client
import sys
import os

# Inicializa Ollama
client = Client()

# Prompt para gerar testes pytest
PROMPT_TEMPLATE = """
Você é um assistente que gera testes unitários em Python usando pytest.
Gere um arquivo de teste completo para o seguinte código Python, incluindo:
- import pytest
- funções def test_* cobrindo casos de sucesso e falha

Código Python:
{codigo}

Retorne apenas o código do arquivo de teste.
"""

def gerar_testes(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        codigo = f.read()

    # Chamada ao modelo local Ollama (usando llama2)
    resposta = client.chat(
        model="llama2",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(codigo=codigo)}]
    )

    teste_gerado = resposta.message.content
    
    nome_arquivo = os.path.basename(caminho_arquivo).replace(".py", "")
    caminho_teste = f"tests/test_{nome_arquivo}.py"

    os.makedirs("tests", exist_ok=True)
    with open(caminho_teste, "w") as f:
        f.write(teste_gerado)
    
    print(f"Arquivo de teste gerado: {caminho_teste}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_arquivo_python>")
        sys.exit(1)
    
    gerar_testes(sys.argv[1])
