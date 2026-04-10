# otimizacao

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

---

`otimizacao` é uma biblioteca Python educacional voltada à validação e ao aprendizado do **Método Simplex**, passo-a-passo, em portugués, pensada para as aulas de otimização dentro do território brasileiro.

Diferente de solvers do tipo 'caixa-preta', este projeto tem sido desenhado para estudantes, professores e autodidatas que desejam compreender como o algoritmo funciona internamente através do Tableau, com suas matrizes, vetores e fluxo iterativo. O objetivo principal é **transparência e educação**

---

🇧🇷 Português | 🇲🇽 Español | 🇺🇸 English

## Início Rápido - Quick Start

### Instalação - Installation

#### Do PyPI
```bash
pip install otimizacao
```

#### Do GitHub
```bash
pip install git+https://github.com/chem-montenegroemilio-eq/otimizacao.git
```
#### Teste 
```python
from otimizacao import Otimizador

# Executa um exemplo interno do método Simplex mostrando os calculos
teste = Otimizador()
# Roda um exemplo Simplex com saída passo-a-passo
teste.simplex(calculo_visivel=True)
```

## 🇧🇷 Português

Implementação educacional do algoritmo do método Simplex em Python. Este projeto foi desenvolvido para aprendizado e ensino do funcionamento interno do método Simplex, de fácil uso e implementação.

### Características (v 0.1.0)

- Passo-a-passo do tableau do Simplex
- Visualização de vetores e matrizes entre iterações
- Desenvolvido para aprendizado e ensino em otimização
- Versão: 0.1.0 - Lançamento educacional inicial (em desenvolvimento)

### Limitações atuais (v 0.1.0)

- Não detecta problemas inviáveis
- Não suporta variáveis inteiras
- Não inclui análise de sensibilidade

---

## 🇪🇸 Español

Implementación educativa del algoritmo del método Simplex en Python. Este proyecto fue diseñado para el aprendizaje y enseñanza del funcionamiento interno del método Simplex, de fácil uso e implementación.

### Características (v 0.1.0)

- Paso-a-paso del tableau del método Simplex
- Visualización de matrices y vectores entre iteraciones
- Diseñado para aprendizaje y enseñanza en optimización
- Versión: 0.1.0 – Lanzamiento educacional inicial (en desarrollo)

### Limitaciones actuales (v 0.1.0)

- No detecta problemas inviables.
- No trabaja con variables inteiras
- No incluye análise de sensibilidade

---

## 🇺🇸 English

Educational implementation of the Simplex optimization algorithm in Python. This project is designed to be easy to use and suitable for teaching and learning optimization concepts.

### Features (v 0.1.0)

- Step-by-step Simplex tableau
- Visualization of matrices and vectors between iterations
- Designed for learning and teaching optimization
- Version: 0.1.0 – Initial educational release (under development)

### Limitaciones actuales (v 0.1.0)

- No detecta problemas inviables.
- No trabaja con variables inteiras
- No incluye análise de sensibilidade

---
## Estrutura do Projeto - Project Structure

```
otimizacao/
├── README.md                           # O arquivo que vc esta lendo agora
├── pyproject.toml                      # Metadados e dependências do projeto
├── LICENSE                             # AGPL v3
│
├── src/                                
│    │
│    ├── otimizacao/                    # Pasta do projeto
│    │   ├── __init__.py
│    │   ├── exemplo_Simplex.py         # Exemplo para caso .simplex() sem definir f.o. e restricoes
│    │   ├── otimizador.py              # Arquivo principal do projeto 
│    │
│    └── core/            
│        ├── __init__.py
│        ├── algoritmo_simplex.py       # Solucionador passo-a-passo do algoritmo Simplex
│        ├── determinador_fase.py       # Determina se Fase 1 ou Fase 2
│        └── parser.py                  # Tratamento dos strings para converter em matrizes e vetores
│
└── exemplos/
     │
     ├── exemplo_chem_eng.py            # Exemplo do livro de Himmelblau
     ├── exemplo_compras.py             # Exemplo de compras de um mestrado
     ├── exemplo_livro_Gut.py           # Exemplo do livro de Gut
     ├── exemplo_vazio.py               # Exemplo para caso vazio
     └── exemplo_youtube.py             # Exemplo para caso encontrado passo-a-passo no YouTube
```

---
## Autor - Author

- **Emilio Fernando Montenegro Alvarado** - [chem.montenegro.eq@gmail.com](mailto:chem.montenegro.eq@gmail.com)

---

## Referências - References

**Método Simplex (explicação didática):**
- https://www.youtube.com/watch?v=btjxqq-vMOg

## Exemplos - Examples References
Alguns exemplos incluídos neste projeto foram baseados em referências da literatura:
- EDGAR, T. F.; HIMMELBLAU, D. M.; LASDON, L. S. Optimization of chemical processes. 2. ed. New York: McGraw-Hill, 2001.
- GUT, J. A. W. Programação matemática para otimização de processos. São Paulo: Edusp, 2021.

**Análise de Sensibilidade** 
- Em breve

**Programação Linear Fuzzy** 
- Em breve

---

## Contribuições - Contributions

- 🇧🇷 Neste momento (v0.1.0), contribuições externas ainda não estão abertas.
- 🇲🇽 Por ahora (v0.1.0), contribuciones externas no serán recibidas.
- 🇺🇸 At this stage (v0.1.0), external contributions are not yet open.

---

## Links

- **Site**: [https://github.com/chem-montenegroemilio-eq/otimizacao](https://github.com/chem-montenegroemilio-eq/otimizacao)
- **PyPI**: Em breve
- **Documentação**: Em breve
