from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from axe_selenium_python import Axe
import json
import time
import os

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
    # Configurações do Robô (Chrome)
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Tire o # se quiser que o navegador rode "escondido"

    # Inicia o Robô
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        print(f"🤖 Robô iniciando análise em: {url}")
        driver.get(url)
        time.sleep(2) # Espera carregar

        # Inicia o Cérebro (Axe)
        axe = Axe(driver)
        axe.inject()

        print("🧠 Cérebro analisando acessibilidade...")
        resultados = axe.run()

        # Pega a lista de erros
        violacoes = resultados["violations"]
        print(f"🚨 Total de violações encontradas: {len(violacoes)}")

        # --- SALVANDO OS DADOS (A Parte dos Arquivos) ---
        
        if not os.path.exists("reports"):
            os.makedirs("reports")

        # 1. Salva o JSON Técnico (Para devs/backup)
        with open("reports/dados_tecnicos_axe.json", "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

        # 2. GERA O RELATÓRIO HUMANIZADO (O PDF)
        print("📄 Gerando Relatório Humanizado em PDF...")
        
        # Aqui a gente chama a sua função e passa a URL e a lista de erros
        criar_pdf_humanizado(url, violacoes)
        
        print("-" * 30)
        print("✅ PROCESSO FINALIZADO COM SUCESSO!")
        print("Verifique o arquivo 'Relatorio_GuiaAcesso.pdf' na pasta.")
        print("-" * 30)

        return resultados

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

    finally:
        driver.quit() # Fecha o navegador

if __name__ == "__main__":
    print("--- API GUIAACESSO (Versão Beta) ---")
    url_alvo = input("Digite a URL do site para analisar (ex: https://www.google.com): ")
    
    if not url_alvo.startswith("http"):
        url_alvo = "https://" + url_alvo
        
    avaliar_acessibilidade(url_alvo)