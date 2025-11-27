# src/tradutor_regras.py

# Mapeia erros técnicos para a Norma ABNT NBR 17225 e explicações humanizadas.

DICIONARIO_TRADUCAO = {

    # ==============================================================================
    # NÍVEL A (ESSENCIAL) - Critérios Básicos de Acessibilidade
    # ==============================================================================

    # --- IMAGENS E VISUAL ---
    "image-alt": {
        "titulo_humanizado": "Falha Crítica: Imagem sem Descrição",
        "explicacao_gerente": "Imagens informativas estão sem texto alternativo. Leitores de tela não conseguem descrevê-las para usuários cegos.",
        "explicacao_dev": "Adicione o atributo alt='descrição' na tag <img>. Se for decorativa, use alt=''.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.2.1)",
        "nivel_selo": "A"
    },
    "image-redundant-alt": {
        "titulo_humanizado": "Falha Visual: Descrição de Imagem Repetitiva",
        "explicacao_gerente": "O texto alternativo da imagem é igual ao texto que está logo ao lado dela, criando uma leitura repetitiva.",
        "explicacao_dev": "Se o texto adjacente já descreve a imagem, use alt='' para torná-la decorativa.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.2.3)",
        "nivel_selo": "A"
    },
    "input-image-alt": {
        "titulo_humanizado": "Falha Crítica: Botão de Imagem sem Nome",
        "explicacao_gerente": "Um botão feito de imagem não tem texto explicando sua função. O usuário não saberá para que serve.",
        "explicacao_dev": "Input type='image' precisa de atributo alt descrevendo a ação (ex: 'Pesquisar').",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.2.2)",
        "nivel_selo": "A"
    },
    "color-contrast-enhanced": { 
        "titulo_humanizado": "Uso Inadequado de Cor",
        "explicacao_gerente": "Informações estão sendo transmitidas apenas pela cor (ex: 'erros em vermelho'), o que é invisível para daltônicos.",
        "explicacao_dev": "Não use apenas cor para indicar estado. Use ícones ou texto auxiliar.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.11.1)",
        "nivel_selo": "A"
    },
    "audio-caption": {
        "titulo_humanizado": "Falha de Mídia: Áudio sem Transcrição",
        "explicacao_gerente": "Conteúdos de áudio pré-gravados não possuem uma alternativa em texto.",
        "explicacao_dev": "Forneça uma transcrição textual completa para arquivos de áudio.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.14.1)",
        "nivel_selo": "A"
    },

    # --- TECLADO E NAVEGAÇÃO ---
    "keyboard-nav": {
        "titulo_humanizado": "Bloqueio de Navegação por Teclado",
        "explicacao_gerente": "Funcionalidades do site não podem ser acessadas apenas com o teclado, excluindo usuários com deficiência motora.",
        "explicacao_dev": "Garanta que todos os elementos interativos sejam focáveis e acionáveis por Enter/Space.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.1.13)",
        "nivel_selo": "A"
    },
    "focus-trap": {
        "titulo_humanizado": "Falha Grave: Armadilha de Teclado",
        "explicacao_gerente": "O foco do teclado fica preso em um elemento e o usuário não consegue sair dele sem usar o mouse.",
        "explicacao_dev": "Verifique modais que capturam o foco e não permitem a saída com TAB ou ESC.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.1.6)",
        "nivel_selo": "A"
    },
    "tabindex": {
        "titulo_humanizado": "Ordem de Foco Confusa",
        "explicacao_gerente": "A navegação com a tecla TAB pula pela página de forma desordenada.",
        "explicacao_dev": "Evite tabindex positivo. A ordem do foco deve seguir a ordem do DOM.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.1.4)",
        "nivel_selo": "A"
    },
    "skip-link": {
        "titulo_humanizado": "Ausência de Link 'Pular para Conteúdo'",
        "explicacao_gerente": "Falta um atalho para pular o menu e ir direto ao conteúdo principal.",
        "explicacao_dev": "Adicione um 'Skip Link' visível ao foco no topo da página.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.7.12)",
        "nivel_selo": "A"
    },
    "document-title": {
        "titulo_humanizado": "Página sem Título",
        "explicacao_gerente": "A página não tem um título na aba do navegador.",
        "explicacao_dev": "A tag <title> não pode estar vazia no <head>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.1)",
        "nivel_selo": "A"
    },
    "link-name": {
        "titulo_humanizado": "Link Vazio ou Vago",
        "explicacao_gerente": "Links como 'Clique aqui' ou links sem texto não explicam para onde levam.",
        "explicacao_dev": "Links devem ter texto discernível e descritivo.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.7.4)",
        "nivel_selo": "A"
    },

    # --- ESTRUTURA ---
    "html-has-lang": {
        "titulo_humanizado": "Idioma da Página não Definido",
        "explicacao_gerente": "O site não informa que está em Português. Leitores de tela lerão com sotaque errado.",
        "explicacao_dev": "Adicione o atributo lang='pt-BR' na tag <html>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.2)",
        "nivel_selo": "A"
    },
    "empty-heading": {
        "titulo_humanizado": "Cabeçalho Vazio",
        "explicacao_gerente": "Existem títulos na página que não contêm texto.",
        "explicacao_dev": "Tags h1-h6 não devem estar vazias.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.3.1)",
        "nivel_selo": "A"
    },
    "heading-order": {
        "titulo_humanizado": "Estrutura de Títulos Incorreta",
        "explicacao_gerente": "A hierarquia visual está quebrada (ex: pulando de h1 para h3).",
        "explicacao_dev": "Não pule níveis de cabeçalho. Mantenha a sequência lógica.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.3.5)",
        "nivel_selo": "A"
    },
    "list": {
        "titulo_humanizado": "Lista Mal Estruturada",
        "explicacao_gerente": "Itens que parecem uma lista visualmente não foram construídos como lista no código.",
        "explicacao_dev": "Use <ul>, <ol> e <li> para listas.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.5.1)",
        "nivel_selo": "A"
    },
    "duplicate-id": {
        "titulo_humanizado": "Erro de Código: IDs Duplicados",
        "explicacao_gerente": "Existem elementos com o mesmo nome técnico (ID), o que quebra a tecnologia assistiva.",
        "explicacao_dev": "O atributo 'id' deve ser único em toda a página.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.12)",
        "nivel_selo": "A"
    },

    # --- FORMULÁRIOS ---
    "label": {
        "titulo_humanizado": "Campo de Formulário sem Rótulo",
        "explicacao_gerente": "Um campo de digitação não tem etiqueta. O usuário não sabe o que preencher.",
        "explicacao_dev": "Todo <input> precisa de um <label> associado (for/id).",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.9.1)",
        "nivel_selo": "A"
    },
    "select-name": {
        "titulo_humanizado": "Caixa de Seleção sem Rótulo",
        "explicacao_gerente": "Uma caixa de seleção (dropdown) não tem etiqueta explicando sua função.",
        "explicacao_dev": "A tag <select> precisa de um nome acessível.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.9.1)",
        "nivel_selo": "A"
    },
    "button-name": {
        "titulo_humanizado": "Botão sem Texto",
        "explicacao_gerente": "Botões vazios (apenas ícones) são invisíveis para leitores de tela.",
        "explicacao_dev": "Botões devem ter texto interno ou aria-label.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.10)",
        "nivel_selo": "A"
    },
    "aria-allowed-role": {
        "titulo_humanizado": "Falha de Código: Papel ARIA Inválido",
        "explicacao_gerente": "Um elemento está tentando usar um recurso de acessibilidade que não é permitido.",
        "explicacao_dev": "O atributo 'role' não é válido para este elemento HTML.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.12)",
        "nivel_selo": "A"
    },
    "duplicate-id-active": {
        "titulo_humanizado": "Falha de Código: IDs Duplicados Ativos",
        "explicacao_gerente": "Existem elementos interativos com o mesmo ID na página.",
        "explicacao_dev": "O atributo 'id' deve ser único.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.12)",
        "nivel_selo": "A"
    },

    # ==============================================================================
    # NÍVEL AA (INTERMEDIÁRIO) - O Padrão de Mercado
    # ==============================================================================

    "color-contrast": {
        "titulo_humanizado": "Contraste de Cores Insuficiente",
        "explicacao_gerente": "O texto é difícil de ler devido à baixa diferença de cor com o fundo.",
        "explicacao_dev": "Garanta contraste de 4.5:1 para texto normal.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.11.3)",
        "nivel_selo": "AA"
    },
    "meta-viewport": {
        "titulo_humanizado": "Zoom Bloqueado em Celulares",
        "explicacao_gerente": "O site impede que o usuário dê zoom no celular.",
        "explicacao_dev": "Remova 'user-scalable=no' da tag meta viewport.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.13.5)",
        "nivel_selo": "AA"
    },
    "scrollable-region-focusable": {
        "titulo_humanizado": "Área de Rolagem Inacessível",
        "explicacao_gerente": "Áreas de texto com barra de rolagem não podem ser acessadas pelo teclado.",
        "explicacao_dev": "Elementos com 'overflow: scroll' devem ser focáveis (tabindex='0').",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.1.13)",
        "nivel_selo": "AA"
    },
    "focus-order-semantics": {
        "titulo_humanizado": "Indicador de Foco Oculto",
        "explicacao_gerente": "Não é possível ver onde o cursor do teclado está na tela.",
        "explicacao_dev": "Não use 'outline: none' no CSS sem fornecer alternativa.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.1.1)",
        "nivel_selo": "AA"
    },
    "video-caption": { # (Muitas vezes considerado A, mas essencial para AA)
        "titulo_humanizado": "Vídeo sem Legendas",
        "explicacao_gerente": "Vídeos pré-gravados não possuem legendas sincronizadas.",
        "explicacao_dev": "Elementos <video> precisam de uma trilha de legendas.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.14.2)",
        "nivel_selo": "AA"
    },
    "autocomplete-valid": {
        "titulo_humanizado": "Campo sem Autopreenchimento",
        "explicacao_gerente": "Campos comuns não sugerem preenchimento automático.",
        "explicacao_dev": "Use o atributo autocomplete com o valor correto.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.9.15)",
        "nivel_selo": "AA"
    },
    "landmark-one-main": {
        "titulo_humanizado": "Estrutura: Múltiplas Áreas Principais",
        "explicacao_gerente": "A página tem mais de uma área marcada como 'Principal', o que confunde a navegação.",
        "explicacao_dev": "A página deve ter apenas um elemento <main>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.4.4)",
        "nivel_selo": "AA"
    },
    "page-has-heading-one": {
        "titulo_humanizado": "Página sem Cabeçalho Principal (H1)",
        "explicacao_gerente": "A página não tem um título principal visível.",
        "explicacao_dev": "A página deve ter um elemento <h1>.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.3.3)",
        "nivel_selo": "AA"
    },
    "region": {
        "titulo_humanizado": "Conteúdo fora de Região",
        "explicacao_gerente": "Parte do conteúdo não está dentro de uma área marcada (cabeçalho, rodapé, principal).",
        "explicacao_dev": "Todo conteúdo deve estar contido em regiões ARIA (landmarks).",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.4.3)",
        "nivel_selo": "AA"
    },

    # ==============================================================================
    # NÍVEL AAA (AVANÇADO) - Excelência
    # ==============================================================================

    "color-contrast-aaa": { 
        "titulo_humanizado": "Contraste de Cores (Nível Ouro)",
        "explicacao_gerente": "Para atingir o nível máximo, o contraste precisa ser ainda maior (7:1).",
        "explicacao_dev": "Aumente o contraste para 7:1 para textos normais.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.11.2)",
        "nivel_selo": "AAA"
    },
    "no-autoplay-audio": {
        "titulo_humanizado": "Interrupção: Áudio Automático",
        "explicacao_gerente": "Áudios tocam sozinhos ao abrir a página.",
        "explicacao_dev": "Não use autoplay em tags de áudio ou vídeo.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.14.7)",
        "nivel_selo": "AAA"
    },
    "bypass": {
        "titulo_humanizado": "Falta de Blocos Ignoráveis",
        "explicacao_gerente": "Falta mecanismo para pular blocos repetidos em nível avançado.",
        "explicacao_dev": "Garanta mecanismos para pular blocos de conteúdo.",
        "norma_oficial": "ABNT NBR 17225 (Seção 5.7.12)",
        "nivel_selo": "AAA"
    }
}

# Função auxiliar para buscar a tradução segura
def buscar_traducao(id_erro):
    return DICIONARIO_TRADUCAO.get(id_erro, {
        "titulo_humanizado": f"Erro Técnico: {id_erro}",
        "explicacao_gerente": "Um erro de acessibilidade não catalogado foi encontrado. Consulte a equipe técnica.",
        "explicacao_dev": f"Verifique a documentação oficial da ferramenta Axe para a regra '{id_erro}'.",
        "norma_oficial": "WCAG Geral",
        "nivel_selo": "Desconhecido"
    })