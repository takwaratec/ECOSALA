#!/usr/bin/env python3
"""
Sentinel Script — ECOSALA
Monitoramento Generico de Editais e Geracao de Fichas de Inscricao
Cobre o escopo dos 11 membros: agroecologia, bioconstrucao, microbiologia,
saude, gestao comunitaria, TI, arquitetura, educacao do campo, bambu, bioinsumos
"""

def formatar_ficha_inscricao(edital_nome, teto, prazo, eixos, membros):
    template = f"""# Gabarito de Inscricao: {edital_nome}
**Teto:** {teto} | **Prazo:** {prazo}
**Eixos:** {', '.join(eixos)}
**Membros envolvidos:** {', '.join(membros)}

## [CAMPO 1] IDENTIFICACAO DO PROJETO
- Titulo: [Inserir]
- Proponente: [A definir — cooperativa/associacao/ICT]

## [CAMPO 2] JUSTIFICATIVA
[Contexto territorial especifico do edital]

## [CAMPO 3] METODOLOGIA
[Metodologia ECOSALA — ecoformacao em 5 etapas]

## [CAMPO 4] METAS E RESULTADOS
[Metricas especificas do edital]

## ANEXOS NECESSARIOS
- [ ] Carta de anuencia das ICTs
- [ ] Carta de anuencia dos territorios
- [ ] Orcamento detalhado
- [ ] Cronograma fisico-financeiro
- [ ] CVs da equipe
"""
    return template

def gerar_boletim(editais):
    boletim = "# Boletim Sentinel — ECOSALA\n"
    boletim += "> Monitoramento generico para os 11 membros\n\n"
    boletim += "## Areas de Atuacao\n"
    boletim += "- Agroecologia e producao organica (Paron, Vilela, Sando)\n"
    boletim += "- Bioconstrucao e arquitetura sustentavel (Blanco, Araujo)\n"
    boletim += "- Microbiologia e bioinsumos (Paron, Takwara)\n"
    boletim += "- Saude integral e desertos alimentares (Palma)\n"
    boletim += "- Gestao comunitaria e politicas publicas (Okino, Sando)\n"
    boletim += "- TI e documentacao (Miguel, Bueno, Takwara)\n"
    boletim += "- Educacao do campo (Borges)\n"
    boletim += "- Bambu, biochar, PU vegetal (Borges, Takwara)\n\n"

    for i, e in enumerate(editais, 1):
        boletim += f"---\n### {i}. {e['nome']}\n"
        boletim += f"**Teto:** {e['teto']} | **Prazo:** {e['prazo']}\n"
        boletim += f"**Eixos:** {', '.join(e['eixos'])}\n"
        boletim += f"**Membros:** {', '.join(e['membros'])}\n"
        boletim += f"{e['descricao']}\n\n"
    return boletim

if __name__ == '__main__':
    editais = [
        {
            "nome": "FINEP Mais Inovacao — Rodada 2",
            "teto": "R$ 5.000.000 a R$ 20.000.000",
            "prazo": "Fluxo continuo (24 meses)",
            "eixos": ["Economia Circular", "Cidades Sustentaveis", "Agua/Esgoto", "Moradia"],
            "membros": ["Paron", "Blanco", "Takwara", "Borges", "Vilela", "Sando"],
            "descricao": "Vaga Lumen: laboratorio itinerante. Documentos em github.com/takwaratec/fundo-vaga-lumen-2026"
        },
        {
            "nome": "BNDES Bioinsumos",
            "teto": "A definir",
            "prazo": "A confirmar",
            "eixos": ["Bioinsumos", "Biochar", "Pirolenhoso", "Bambu"],
            "membros": ["Takwara", "Paron", "Borges"],
            "descricao": "Biochar + acido pirolenhoso + bambu. Minuta em docs/10_BNDES_BIOINSUMOS/"
        },
        {
            "nome": "FEHIDRO — Fundo Estadual de Recursos Hidricos",
            "teto": "A consultar",
            "prazo": "A confirmar",
            "eixos": ["Agua", "Saneamento", "Nascentes", "APA Guarani"],
            "membros": ["Sando", "Okino", "Palma"],
            "descricao": "Recuperacao de nascentes e saneamento rural na APA Guarani. Referencias em 04_REFERENCIAS_FEHIDRO/"
        },
        {
            "nome": "Fundo Casa Socioambiental",
            "teto": "R$ 20.000 a R$ 60.000",
            "prazo": "30/jun e 14/jul/2026",
            "eixos": ["Juventude", "Clima", "Agroecologia"],
            "membros": ["Miguel", "Sando"],
            "descricao": "Editais de base comunitaria. Parceria com Coletivo Terra Viva."
        },
        {
            "nome": "CNPq — Bolsas de Extensao (DTI, EXP)",
            "teto": "Variavel",
            "prazo": "Fluxo continuo",
            "eixos": ["Formacao", "Pesquisa", "Extensao"],
            "membros": ["Paron", "Borges", "Vilela"],
            "descricao": "Bolsas para bolsistas do projeto. Lei de Inovacao 10.973/2004."
        }
    ]

    print("=== SENTINEL ECOSALA — MONITORAMENTO DE EDITAIS ===")
    print(gerar_boletim(editais))

    print("\n=== GABARITO: Edital prioritario ===")
    gab = formatar_ficha_inscricao(editais[0]["nome"], editais[0]["teto"],
                                    editais[0]["prazo"], editais[0]["eixos"],
                                    editais[0]["membros"])
    print(gab[:300])
