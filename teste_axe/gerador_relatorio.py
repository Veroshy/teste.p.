# gerador_relatorio.py
from fpdf import FPDF
from datetime import datetime
import sys
import re

sys.path.append(".") 
from tradutor_regras import DICIONARIO_TRADUCAO, buscar_traducao

class RelatorioPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'GUIAACESSO - Relatorio de Auditoria (VIA)', 0, 1, 'C')
        self.ln(5)
        self.set_line_width(0.5)
        self.line(10, 25, 200, 25)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

def criar_pdf_humanizado(url_analisada, lista_erros_tecnicos):
    pdf = RelatorioPDF()
    pdf.add_page()
    
    # --- Título do Relatório ---
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Site Analisado: {url_analisada}", 0, 1)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, f"Data da Auditoria: {datetime.now().strftime('%d/%m/%Y %H:%M')}", 0, 1)
    pdf.ln(10)

    # --- Loop dos Erros ---
    for erro in lista_erros_tecnicos:
        
        if isinstance(erro, dict):
            erro_id = erro.get('id')
        else:
            erro_id = erro 

        traducao = buscar_traducao(erro_id)
        
        # DESTAQUE: Título do Erro
        pdf.set_font("Arial", "B", 14)
        if traducao.get('nivel_selo') == 'A':
            pdf.set_text_color(200, 0, 0) # Vermelho para erros críticos
            pdf.cell(0, 10, f"[CRITICO] {traducao['titulo_humanizado']}", 0, 1)
        else:
            pdf.set_text_color(200, 100, 0) # Laranja para alertas
            pdf.cell(0, 10, f"[ALERTA] {traducao['titulo_humanizado']}", 0, 1)
        
        pdf.set_text_color(0, 0, 0) # Volta para preto

        # DESTAQUE: Norma Oficial (Caixa de destaque simples)
        pdf.set_font("Arial", "B", 10)
        pdf.cell(40, 8, "NORMA OFICIAL:", 0, 0)
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 8, traducao.get('norma_oficial', 'N/A'), 0, 1)
        
        pdf.ln(2)
        
        # Bloco: Impacto no Usuário (Gerente)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, "IMPACTO NO USUARIO (Por que corrigir?):", 0, 1)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 6, traducao['explicacao_gerente'])
        
        pdf.ln(3)
        
        # Bloco: Ação Técnica (Dev)
        pdf.set_font("Arial", "B", 11)
        pdf.cell(0, 8, "COMO CORRIGIR (Tecnico):", 0, 1)
        pdf.set_font("Courier", "", 10) # Fonte tipo código
        pdf.multi_cell(0, 6, traducao['explicacao_dev'])
        
        pdf.ln(8)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(8)

    # Salva
    nome_limpo = re.sub(r'[^a-zA-Z0-9]', '_', url_analisada)
    nome_arquivo = f"Relatorio_{nome_limpo}.pdf"
    if len(nome_arquivo) > 50: nome_arquivo = nome_arquivo[:50] + ".pdf"
    
    pdf.output(nome_arquivo)
    print(f"✅ Relatório Gerado: {nome_arquivo}")