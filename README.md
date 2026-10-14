# Análise Geoespacial de Segurança Pública: João Pessoa / PB

Estudo analítico e mapeamento interativo dos Crimes Violentos Letais Intencionais (CVLI) nos 64 bairros do município de João Pessoa, combinando dados de segurança pública com informações demográficas do Censo IBGE 2022.

---

## Acesso Rápido

- **Mapa Interativo (GitHub Pages):** [joaoedupb.github.io/JampaPy](https://joaoedupb.github.io/JampaPy/)
- **Repositório do Código:** [github.com/JoaoEduPB/JampaPy](https://github.com/JoaoEduPB/JampaPy)

---

## Visão Geral do Projeto

O objetivo principal deste projeto é investigar a distribuição territorial da criminalidade na capital paraibana através de métricas relativas (padronizadas por população), superando distorções provocadas pela simples contagem de ocorrências absolutas em bairros de portes populacionais distintos.

### Principais Destaques Metodológicos

1. **Normalização por Habitantes:** Integração dos registros de CVLI com a contagem populacional do Censo IBGE 2022. A métrica adotada foi a Taxa de CVLI por 10.000 habitantes:
   
   Taxa = (Ocorrências / População) * 10.000

2. **Tratamento de Outlier Espacial:** O bairro de Barra de Gramame apresentou uma taxa atípica (99,75 por 10k hab.) em razão da baixa população residente registrada em relação às ocorrências no período. Para evitar que essa variação distorcesse a escala de cores dos demais 63 bairros no mapa coroplético, foram definidos intervalos de classe customizados (`bins=[0, 1, 2, 4, 8, 20, 100]`).

3. **Visualização Dinâmica:** Construção de um mapa web interativo com suporte a balões explicativos (*tooltips* em *hover*), permitindo consultar bairro, população, volume absoluto de casos e taxa por 10 mil habitantes.

---

## Estrutura do Repositório

```text
JampaPy/
├── index.html                 # Aplicação web final (Hospedada no GitHub Pages)
├── .gitattributes             # Configuração de linguagens do repositório
├── README.md                  # Documentação do projeto
└── ProjetoJampa/
    ├── Etapa1/                # Ingestão e exploração inicial dos dados
    ├── Etapa2/                # Malha espacial dos 64 bairros (GeoJSON)
    ├── Etapa3/                # Processamento dos dados demográficos (IBGE 2022)
    ├── Etapa4/                # Consolidação das ocorrências policiais (SESP-PB)
    ├── Etapa5/                # Cruzamento, limpeza e cálculo da TAXA_10K
    └── Etapa6/                # Visualização de dados (Ranking estático e Mapa Folium)

Foi o truque dos blocos de código aninhados! Quando coloquei o código dentro do código, a visualização cortou o restante.

Aqui está o bloco limpo usando quatro crases de proteção. É só clicar no botão **"Copy"** no canto do bloco abaixo e colar direto no seu `README.md`:

## Tecnologias Utilizadas

- **Python 3.12**
- **Pandas**: Manipulação e agregação de dados tabulares.
- **GeoPandas**: Leitura, manipulação e fusão de dados vetoriais geográficos.
- **Matplotlib & Seaborn**: Geração de visualizações estatísticas e rankings.
- **Folium / Leaflet.js**: Renderização e interatividade da cartografia web em HTML/JS.
- **Esri Light Gray Canvas**: Camada base de mapa neutra para destaque das cores do coroplético.

---

## Como Executar o Projeto Localmente

1. Clone o repositório:
```bash
git clone [https://github.com/JoaoEduPB/JampaPy.git](https://github.com/JoaoEduPB/JampaPy.git)
cd JampaPy
```

2. Instale as dependências necessárias:
```bash
pip install pandas geopandas folium matplotlib seaborn
```

3. Execute o script de geração do mapa:
```bash
python3 ProjetoJampa/Etapa6/etapa6_mapa.py
```

4. Abra o arquivo `index.html` em qualquer navegador web.

---

## Fontes de Dados

- **Dados Populacionais:** IBGE — Censo Demográfico 2022 (Malha territorial e contagem populacional por bairros).
- **Dados de Segurança Pública:** SESP-PB / SISP 2025 (Ocorrências de Crimes Violentos Letais Intencionais - CVLI).

```
