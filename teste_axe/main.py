from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
import json
import time
import os

# NOVA IMPORTAÇÃO: Trazer o gerador que criamos
from gerador_relatorio import criar_pdf_humanizado

def gerar_relatorio_resumido(resultados):
    resumo = []
    for violacao in resultados["violations"]:
        item = {
            "regra": violacao.get("id"),
            "impacto": violacao.get("impact"),
            "descricao": violacao.get("description"),
            "ajuda": violacao.get("help"),
            "elementos_afetados": len(violacao.get("nodes", []))
        }
        resumo.append(item)
    return resumo

def avaliar_acessibilidade(url):
    # Configuração do Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Descomente se não quiser ver o navegador abrindo

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print(f"Acessando a seguinte url: {url}")
        driver.get(url)
        time.sleep(2) 

        axe = Axe(driver)
        axe.inject()

        print("Fazendo análise de acessibilidade...")
        resultados = axe.run()

        violacoes = resultados["violations"]
        print(f"Total de violações encontradas: {len(violacoes)}")

        # Cria pasta para relatórios
        if not os.path.exists("reports"):
            os.makedirs("reports")

        # Salva os JSONs (Dados técnicos)
        relatorio_completo = "reports/resultado_axe_completo.json"
        relatorio_resumido = "reports/resultado_axe_resumido.json"

        with open(relatorio_completo, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        resumo = gerar_relatorio_resumido(resultados)
        with open(relatorio_resumido, "w", encoding="utf-8") as f:
            json.dump(resumo, f, ensure_ascii=False, indent=2)

        print(f"Dados técnicos salvos na pasta 'reports'.")

        # --- AQUI A MÁGICA ACONTECE ---
        # Chama o seu gerador para criar o PDF com base nas violações encontradas
        print("Gerando Relatório Humanizado em PDF...")
        criar_pdf_humanizado(url, violacoes)
        # ------------------------------

        return resultados

    finally:
        driver.quit()

if __name__ == "__main__":
    url = input("Digite a URL que você deseja avaliar: ")
    avaliar_acessibilidade(url)