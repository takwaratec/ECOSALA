# AGENTS.md — ECOSALA

## Identidade

Coletivo de **12 pesquisadores, professores e profissionais** que atuam na retaguarda técnica de comunidades da reforma agrária, APAs e periferias urbanas. Formação, pesquisa e ação em agroecologia, bioconstrução e tecnologias sociais.

**Site:** https://takwaratec.github.io/ECOSALA/
**Repositório:** github.com/takwaratec/ECOSALA
**Acervo Científico:** https://takwaratec.github.io/Analises-e-escrita-cientifica/

---

## Objetivo do Agente

1. **Manter documentação do coletivo** — atas, projetos, editais, fichas dos membros
2. **Processar materiais dos membros** — áudios, PDFs, DOCX, imagens → converter para .md
3. **Acompanhar editais** — verificar prazos, criar fichas, preparar rascunhos
4. **Produzir conteúdo** — minutas, ofícios, atas, relatórios, propostas
5. **Manter o site atualizado** — mkdocs gh-deploy --clean após alterações

---

## Ferramentas Instaladas

| Ferramenta | Função | Status | Caminho |
|---|---|---|---|
| **Pandoc** | DOCX/ODT → MD | ✅ | `/usr/local/bin/pandoc` |
| **PyMuPDF** (fitz) | Extração de texto de PDFs | ✅ | Python `import fitz` |
| **python-docx** | Leitura/escrita DOCX | ✅ | Python `import docx` |
| **ffmpeg** | Conversão de áudio (opus → wav) | ✅ | `/Users/.../miniconda3/bin/ffmpeg` |
| **faster-whisper** | Transcrição de áudio | 🔄 Falha de rede — tentar novamente | `pip install faster-whisper` |
| **pdfplumber** | PDF tabular | ❌ Falha de rede — tentar novamente | `pip install pdfplumber` |

### Workaround para áudio
O gateway do Hermes (Telegram) já tem faster-whisper instalado. Áudios enviados pelo Telegram são transcritos automaticamente. Para áudios locais, converter com ffmpeg e transcrever com o gateway ou instalar whisper quando a rede estabilizar.

---

## Estrutura do Repositório

```
📂 docs/
├── index.md                  → Home do site GH Pages
├── ata-05-05-2026.md         → Memorial da reunião inaugural
├── ecosala-itinerante.md     → Projeto ECOSALA Móvel (c/ texto do Marcos Paron)
├── daniela-maciel.md         → Ficha da Daniela (consolidada)
├── 12_REUNIOES/              → Memoriais e transcrições
├── 10_BNDES_BIOINSUMOS/      → Proposta BNDES (minuta)
├── 11_ESTUDOS_TECNICOS/      → Notas técnicas
├── editais/
│   ├── painel-editais-ecosala.md   → 14 editais mapeados
│   ├── zayed-award-2027.md        → Regulamento Zayed
│   └── zayed-award-2027-dossie.md → Dossiê de nomeação
📂 TRIAGEM-BRUTA/             → Material original (não versionado)
📄 mkdocs.yml                 → Configuração do site
📄 AGENTS.md                  ← Este arquivo
📄 README.md                  → Instruções para os membros
```

---

## Convenções para o Agente

### Processamento de materiais

| Tipo | Ação |
|---|---|
| **Áudio (.opus, .mp3, .m4a)** | Converter com ffmpeg + transcrever (whisper quando disponível; via gateway Telegram como fallback) |
| **PDF** | Extrair texto com PyMuPDF → salvar como .md |
| **DOCX/ODT** | Converter com Pandoc → salvar como .md |
| **Imagens** | Analisar com visão computacional (se houver OCR disponível) |

### Fluxo de trabalho
1. `git pull` — sincronizar
2. Processar materiais
3. `git add + git commit -m "tipo: descrição"`
4. `git push`
5. `mkdocs gh-deploy --clean`

### Regras críticas
- ❌ NUNCA fabricar citações — usar paráfrase explícita quando não houver transcrição
- ❌ NUNCA inflar TRL em propostas
- ✅ Atribuir com honestidade
- ✅ Confirmar qual repositório antes de qualquer ação (ECOSALA, Vaga Lumen, MST, Acervo)

---

## Repositórios Irmãos

| Repositório | GH Pages | Conteúdo |
|---|---|---|
| `github.com/takwaratec/ECOSALA` | `takwaratec.github.io/ECOSALA/` | Coletivo 12 membros ← **estamos aqui** |
| `github.com/takwaratec/fundo-vaga-lumen-2026` | ❌ Só GitHub | Proposta FINEP |
| `github.com/takwaratec/plataforma-juventude-solidaria-2026` | ✅ GH Pages | MST Mário Lago |
| `github.com/takwaratec/Analises-e-escrita-cientifica` | ✅ GH Pages | Acervo ~80 fichas — **NÃO é ECOSALA** |

---

## Fichas dos Membros — Status

| Membro | Status | Histórico |
|---|---|---|
| Marcos Paron | ✅ Completa | Dr. Microbiologia IFSP |
| André Blanco | ✅ Completa | Arquiteto Labiapa |
| Fabio Takwara | ✅ Completa | Pesquisador autodidata IA + bambu |
| Gisele Vilela | ✅ Completa | Pesquisadora Embrapa |
| Joaquim Sando | ❌ **Pendente** | Aguardando histórico |
| Vicente Borges | ✅ Completa | Dr. Educação IFB |
| Raphaela Palma | ❌ **Pendente** | Aguardando histórico |
| Luci Okino | ❌ **Pendente** | Aguardando histórico |
| Murillo Miguel | ❌ **Pendente** | Aguardando histórico |
| Henrique Bueno | ❌ **Pendente** | Aguardando histórico |
| Luis Felipe | ❌ **Pendente** | Aguardando histórico |
| Daniela Maciel | ✅ Completa | Drª Embrapa Territorial |

---

*AGENTS.md mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
