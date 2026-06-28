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
| **faster-whisper** | Transcrição de áudio | ✅ | via `conda run -n whisper_env` |
| **pdfplumber** | PDF tabular | ⏳ Pendente (rede) | `pip install pdfplumber` |
| **ffmpeg** (conda) | Conversão de áudio (opus → wav) | ✅ | `/Users/.../miniconda3/bin/ffmpeg` |

### Uso do faster-whisper
Para transcrever áudios, usar:
```bash
conda run -n whisper_env python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, info = model.transcribe('caminho/do/audio.wav', language='pt')
for seg in segments:
    print(seg.text)
"
```

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

### ❌ Regras para fichas científicas
- **NUNCA** criar fichas de artigos/teses/PDFs sem autor, DOI/ISBN/ISSN identificados
- **NUNCA** publicar documentos incompletos — se faltam dados essenciais, alertar o usuário
- **Sempre** extrair conteúdo do PDF original antes de criar qualquer ficha
- **Toda ficha** deve seguir o método Cavichioli (2025): 8 seções obrigatórias (Dados Gerais, Estrutura, Problema, Referencial Teórico, Metodologia, Achados, Avaliação Crítica, Inserção no Estado da Arte)

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

## Gestão de Frentes de Trabalho

Consulte o arquivo `FRENTES_DE_TRABALHO.md` no repositório mestre (`Mentoria_Tecnologia_Takwara`) para o mapa completo de todas as frentes, seus repositórios, escopo, triagem e regras de fronteira.

**Regra:** Toda conversa começa com a consulta a este documento para situar o contexto.

---

## Protocolo de Governança (Geral)

Trabalhos de campo que envolvam comunidades parceiras só podem ser iniciados após observância das diretrizes de consentimento, proteção de dados e soberania territorial (Salvaguardas de Cancún — REDD+).
Referência: [GOV_PROTOCOLO_SEGURANCA_CANCUN.md](https://github.com/takwaratec/Mulheres-Tecem-Amazonia/blob/main/docs/01_GOVERNANCA/GOV_PROTOCOLO_SEGURANCA_CANCUN.md)

## Regras de Conduta para Documentos Públicos

- **Filtro público vs. interno:** Codinomes internos (Frente X, "cozinha", etc.) NUNCA aparecem em documentos públicos. Parceiros externos veem apenas o nome real das tecnologias.
- **MQTF** (Mulheres Que Tecem a Floresta) é sigla de uso interno. Em docs públicos, referenciar como "projeto de bioeconomia amazônica do consórcio UnB/UFAC/UFRR" com link ao repositório.
- **Atribuição correta:** Cada autor com seu crédito. Conteúdo de chat/áudio/e-mail é delegado ao agente e atribuído ao autor correspondente.
- **NUNCA fabricar citações.** Usar paráfrase explícita quando não houver transcrição literal verificada.

---

*AGENTS.md mantido pelo Hermes Agent · Tecnologia Takwara · 2026*
