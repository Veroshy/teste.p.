# gerador_relatorio.py
from fpdf import FPDF
from datetime import datetime

# Importamos nosso dicionário (certifique-se de que o arquivo tradutor_regras.py está na mesma pasta)
# Se você ainda não criou o arquivo separado, pode colar o dicionário DICIONARIO_TRADUCAO aqui em cima para testar.
from tradutor_regras import DICIONARIO_TRADUCAO, buscar_traducao

class RelatorioPDF(FPDF):
    def header(self):
        # Cabeçalho (Logo e Título)
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'GUIAACESSO - Relatório de Auditoria de Acessibilidade (VIA)', 0, 1, 'C')
        self.ln(5)
        
        # Linha divisória
        self.set_line_width(0.5)
        self.line(10, 25, 200, 25)
        self.ln(10)

    def footer(self):
        # Rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def criar_pdf_humanizado(url_analisada, lista_erros_tecnicos):
    pdf = RelatorioPDF()
    pdf.add_page()
    
    # --- Informações Gerais ---
    pdf.set_font("Arial", "B", 12)
    pdf.cell(40, 10, "Data:", 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, datetime.now().strftime("%d/%m/%Y"), 0, 1)
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(40, 10, "Site Analisado:", 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, url_analisada, 0, 1)
    
    pdf.ln(10) # Espaço

    # --- Loop para gerar os "Cards" de Erro ---
    for erro in lista_erros_tecnicos:
        
        # 1. Pega o ID do erro técnico (ex: "color-contrast")
        # (No teste manual, a lista pode ser só strings. No Axe real, seria um dicionário)
        if isinstance(erro, dict):
            erro_id = erro.get('id')
        else:
            erro_id = erro # Para nosso teste simples

        # 2. Traduz usando nosso Dicionário
        traducao = buscar_traducao(erro_id)
        
        # 3. Desenha o Bloco do Erro (Visual)
        
        # Título com Cor (Vermelho para A, Laranja para AA)
        if traducao['nivel_selo'] == 'A':
            pdf.set_text_color(200, 0, 0) # Vermelho
        else:
            pdf.set_text_color(255, 100, 0) # Laranja
            
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, f"[ERRO] {traducao['titulo_humanizado']}", 0, 1)
        
        # Reset da cor para preto
        pdf.set_text_color(0, 0, 0)
        
        # Norma Oficial
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 8, f"Norma Violada: {traducao['norma_oficial']}", 0, 1)
        
        pdf.ln(2)
        
        # Seção Gerente
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, "[GESTAO] O QUE ISSO SIGNIFICA:", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 6, traducao['explicacao_gerente'])
        
        pdf.ln(3)
        
        # Seção Dev
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, "[DEV] ACAO TECNICA:", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 6, traducao['explicacao_dev'])
        
        pdf.ln(10) # Espaço entre erros
        
        # Linha separadora suave
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(10)

    # Salva o arquivo
    nome_arquivo = "Relatorio_GuiaAcesso.pdf"
    pdf.output(nome_arquivo)
    print(f"✅ Relatório '{nome_arquivo}' gerado com sucesso!")

# --- PEQUENO TESTE PARA RODAR AGORA ---
if __name__ == "__main__":
    # Vamos fingir que o Axe encontrou estes erros:
    erros_teste = ["color-contrast", "image-alt", "label", "document-title"]
    
    criar_pdf_humanizado("www.site-teste.com.br", erros_teste)