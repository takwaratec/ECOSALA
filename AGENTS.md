# AGENTS.md — ECOSALA

## Identidade

Coletivo de **11 pesquisadores, professores e profissionais** que atuam na retaguarda técnica de comunidades da reforma agrária, APAs e periferias urbanas. Formação, pesquisa e ação em agroecologia, bioconstrução e tecnologias sociais.

**Missão:** Articular formação, pesquisa e ação em agroecologia, construindo demandas a partir da base para depois buscar chancela institucional e financiamento.

---

## Objetivo do Agente

Ao ser acionado neste repositório, seu papel é:

1. **Apoiar a produção científica** — fichas dos membros, revisão bibliográfica, normatização ABNT
2. **Estruturar propostas** — FINEP, BNDES, Fundo Casa, editais estaduais/federais
3. **Organizar reuniões e ATAs** — converter memoriais para .md, extrair decisões e encaminhamentos
4. **Manter documentação técnica** — notas sobre bioinsumos, bambu, PU vegetal, MPTDF
5. **Produzir conteúdo** — artigos, relatórios, apresentações

---

## Estrutura do Repositório

```
📂 docs/
├── ata-05-05-2026.md              → Memorial da reunião inaugural
├── ecosala-itinerante.md          → Projeto ECOSALA Itinerante
├── editais/                       → Editais ativos e fichas
├── 12_REUNIOES/                   → Memoriais de reuniões
├── 10_BNDES_BIOINSUMOS/           → Proposta BNDES (biochar + pirolenhoso)
└── 11_ESTUDOS_TECNICOS/           → Notas técnicas
```

---

## Convenções para o Agente

### Documentos
- Converter originais (.docx, .odt, .pdf) para .md antes de versionar
- NUNCA commitar binários grandes (PDF, DOCX, imagens) — vão para TRIAGEM-BRUTA/
- Incluir fonte, data e contexto no topo de cada documento

### Fluxo de trabalho
1. `git pull` — sincronizar com remoto
2. Fazer alterações
3. `git add <arquivos> && git commit -m "tipo: descrição" && git push`

### Produção científica
- Todo material citacional deve ter DOI verificado
- NUNCA fabricar citações — usar parafrase explícita quando não houver transcrição literal
- Referências em formato ABNT

---

## Repositórios Irmãos

| Repositório | Conteúdo | Público |
|---|---|---|
| `github.com/takwaratec/plataforma-juventude-solidaria-2026` | Viveiro-Educador Terra Viva (MST) | MST Mário Lago |
| `github.com/takwaratec/fundo-vaga-lumen-2026` | Proposta FINEP Mais Inovação | FINEP/avaliadores |
| `github.com/takwaratec/Analises-e-escrita-cientifica` | Acervo científico — fichas, artigos, TRL | Acadêmico |

---

## Acervo Científico

👉 https://takwaratec.github.io/Analises-e-escrita-cientifica/

Fichas individuais dos 11 membros: `docs/analyses/ecosala/` no repositório de análises científicas.

---

*AGENTS.md mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
