#!/usr/bin/env python3
"""
Sentinel Script — ECOSALA
Monitoramento Generico de Editais

FLUXO OBRIGATORIO PARA CADA EDITAL:
1. BAIXAR o PDF do regulamento para TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/
2. CONVERTER o regulamento para .md em docs/editais/[edital]/regulamento.md
3. CONVERTER documentos de apoio e formulario oficial para .md
4. ANALISAR compativelidades (TRL, valores, prazos, contrapartida, escopo)
5. ESCREVER orientacoes no boletim semanal
"""

import os
from datetime import date

CAMINHOS = {
    "regulamentos": "TRIAGEM-BRUTA/05_EDITAIS_REGULAMENTOS/",
    "editais_docs": "docs/editais/",
}

AREAS_ECOSALA = [
    "Agroecologia e producao organica",
    "Bioconstrucao e arquitetura sustentavel",
    "Microbiologia e bioinsumos",
    "Saude integral e desertos alimentares",
    "Gestao comunitaria e politicas publicas",
    "TI e documentacao",
    "Educacao do campo",
    "Bambu, biochar, PU vegetal",
]


def baixar_regulamento(url, edital_nome):
    """Passo 1: Baixar o PDF do regulamento."""
    destino = os.path.join(CAMINHOS["regulamentos"], f"{edital_nome}_regulamento.pdf")
    print(f"[1/5] BAIXAR regulamento de: {url}")
    print(f"      Salvar em: {destino}")
    print(f"      Status: PENDENTE (wget/curl)")
    return destino


def converter_para_md(arquivo_pdf, edital_nome):
    """Passo 2: Converter PDF do regulamento para .md."""
    destino_md = os.path.join(CAMINHOS["editais_docs"], f"{edital_nome}_regulamento.md")
    print(f"[2/5] CONVERTER regulamento para .md:")
    print(f"      De: {arquivo_pdf}")
    print(f"      Para: {destino_md}")
    print(f"      Comando: textutil -convert txt -output /tmp/{edital_nome}.txt {arquivo_pdf}")
    return destino_md


def converter_formulario(arquivo_original, edital_nome):
    """Passo 3: Converter formulario oficial e docs de apoio para .md."""
    destino = os.path.join(CAMINHOS["editais_docs"], f"{edital_nome}_formulario.md")
    print(f"[3/5] CONVERTER formulario/documentos de apoio para .md:")
    print(f"      De: {arquivo_original}")
    print(f"      Para: {destino}")
    return destino


def analisar_regulamento(edital_nome):
    """Passo 4: Extrair requisitos e verificar compativelidade."""
    hoje = date.today().isoformat()
    print(f"\n[4/5] ANALISE DE REGULAMENTO: {edital_nome} — {hoje}")
    print("=" * 60)
    print("[ ] TRL minima exigida: _____")
    print("[ ] Valor minimo: R$ _____")
    print("[ ] Valor maximo: R$ _____")
    print("[ ] Contrapartida: _____%")
    print("[ ] Prazo maximo: _____ meses")
    print("[ ] Documentos obrigatorios listados: _____")
    print("[ ] Criterios eliminatórios identificados: [ ]")
    print("[ ] Criterios classificatórios identificados: [ ]")
    print("=" * 60)

    print("\nCOMPATIBILIDADE COM ECOSALA:")
    for area in AREAS_ECOSALA:
        print(f"  [ ] {area}")
    print("\nMEMBROS ENVOLVIDOS:")
    for m in ["Paron", "Blanco", "Takwara", "Vilela", "Sando",
              "Borges", "Palma", "Okino", "Miguel", "Bueno", "Araujo"]:
        print(f"  [ ] {m}")


def gerar_boletim_semanal(editais):
    """Passo 5: Boletim semanal com orientacoes."""
    boletim = f"# Boletim Sentinel ECOSALA — Semana {date.today().strftime('%d/%m/%Y')}\n\n"
    boletim += f"## Areas de Atuacao ({len(AREAS_ECOSALA)} areas)\n\n"
    for a in AREAS_ECOSALA:
        boletim += f"- {a}\n"

    boletim += f"\n## Editais em Analise ({len(editais)})\n\n"

    for i, e in enumerate(editais, 1):
        boletim += f"### {i}. {e['nome']}\n"
        boletim += f"**Situacao:** {e['status']}\n"
        boletim += f"**Prazo:** {e['prazo']}\n"
        boletim += f"**Valor:** {e['teto']}\n"
        boletim += f"**Regulamento baixado?** {e['reg_baixado']}\n"
        boletim += f"**Regulamento convertido?** {e['reg_convertido']}\n"
        boletim += f"**Formulario convertido?** {e['form_convertido']}\n"
        boletim += f"**Compatibilidade:** {e['compativel']}\n"
        boletim += f"**Orientacao:** {e['orientacao']}\n\n"

    boletim += "---\n"
    boletim += "> Proximo boletim: " + date.today().isoformat() + "\n"
    return boletim


if __name__ == '__main__':
    print("=" * 60)
    print("  SENTINEL ECOSALA — MONITORAMENTO GENERICO DE EDITAIS")
    print("  Escopo: 11 membros, 8 areas de atuacao")
    print("=" * 60)

    # Simular analise dos 5 editais mapeados
    editais = [
        {
            "nome": "FINEP Mais Inovacao — Rodada 2",
            "status": "REGULAMENTO CONVERTIDO",
            "prazo": "Fluxo continuo (24 meses)",
            "teto": "R$ 5.000.000 a R$ 20.000.000",
            "reg_baixado": "✅",
            "reg_convertido": "✅ (docs/regulamento-finep-mais-inovacao.md)",
            "form_convertido": "✅ (docs/editais/finep-mais-inovacao-checklist.md)",
            "compativel": "✅ PARCIAL — Falta proponente CNPJ e contrapartida",
            "orientacao": "Avancar com definicao da empresa proponente."
        },
        {
            "nome": "BNDES Bioinsumos",
            "status": "REGULAMENTO NAO BAIXADO",
            "prazo": "A confirmar",
            "teto": "A definir",
            "reg_baixado": "⬜",
            "reg_convertido": "⬜",
            "form_convertido": "⬜",
            "compativel": "PENDENTE",
            "orientacao": "Buscar regulamento e converter para .md."
        },
        {
            "nome": "FEHIDRO — Fundo Estadual de Recursos Hidricos",
            "status": "NAO INICIADO",
            "prazo": "A confirmar",
            "teto": "A consultar",
            "reg_baixado": "⬜",
            "reg_convertido": "⬜",
            "form_convertido": "⬜",
            "compativel": "PENDENTE",
            "orientacao": "Baixar regulamento do site da FEHIDRO."
        },
        {
            "nome": "Fundo Casa Socioambiental",
            "status": "REGULAMENTO NAO BAIXADO",
            "prazo": "30/jun e 14/jul/2026",
            "teto": "R$ 20.000 a R$ 60.000",
            "reg_baixado": "⬜",
            "reg_convertido": "⬜",
            "form_convertido": "⬜",
            "compativel": "PENDENTE",
            "orientacao": "PRAZO URGENTE! Baixar regulamento e verificar elegibilidade do Coletivo Terra Viva."
        },
        {
            "nome": "CNPq — Bolsas DTI/EXP",
            "status": "NAO INICIADO",
            "prazo": "Fluxo continuo",
            "teto": "Variavel",
            "reg_baixado": "⬜",
            "reg_convertido": "⬜",
            "form_convertido": "⬜",
            "compativel": "PENDENTE",
            "orientacao": "Regulamento da RN CNPq 028/2015. Converter para .md."
        }
    ]

    for e in editais:
        print(f"\n>>> PROCESSANDO: {e['nome']} <<<")
        baixar_regulamento("https://exemplo.com/edital", e['nome'][:30])
        converter_para_md("regulamento.pdf", e['nome'][:30])
        converter_formulario("formulario.pdf", e['nome'][:30])
        analisar_regulamento(e['nome'][:30])

    print("\n\n" + "=" * 60)
    print("BOLETIM SEMANAL GERADO:")
    print(gerar_boletim_semanal(editais))
