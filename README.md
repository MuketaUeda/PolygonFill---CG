# 🎨 Polygon Fill - Algoritmo ET/AET

Um projeto de Computação Gráfica que implementa o algoritmo de preenchimento de polígonos utilizando **coerência de arestas** (ET/AET - Edge Table/Active Edge Table).

## 🚀 Características

- ✅ **Algoritmo ET/AET completo** - Implementação fiel ao algoritmo de preenchimento de polígonos
- ✅ **Interface gráfica intuitiva** - Desenvolvida com Pygame
- ✅ **Controle de espessura** - Ajuste dinâmico da espessura das linhas
- ✅ **Seleção de cores** - Preenchimento em vermelho, verde ou azul
- ✅ **Casos especiais tratados** - Arestas horizontais, verticais e polígonos complexos
- ✅ **Preparado para OpenGL** - Estruturas de dados compatíveis para portabilidade futura

## 📋 Requisitos

- Python 3.7+
- Pygame

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/MuketaUeda/PolygonFill---CG.git
cd PolygonFill---CG
```

2. Instale as dependências:
```bash
pip install pygame
```

## 🎮 Como Usar

### Executar o Programa
```bash
python main.py
```

### Controles da Interface

#### 🖱️ Desenho do Polígono
- **Clique esquerdo**: Adiciona vértices ao polígono
- **Clique direito**: Finaliza o polígono (mínimo 3 vértices)

#### 🎛️ Botões de Controle
- **Limpar**: Remove todos os vértices e limpa a tela
- **Preencher**: Executa o algoritmo ET/AET para preencher o polígono
- **R/G/B**: Seleciona a cor de preenchimento (Vermelho/Verde/Azul)
- **+/-**: Aumenta ou diminui a espessura das linhas

#### 📊 Indicadores
- **Espessura: X**: Mostra a espessura atual das linhas
- **Quadrado colorido**: Indica a cor de preenchimento selecionada

## 🧮 Algoritmo ET/AET

### Conceitos Fundamentais

#### ET (Edge Table - Tabela de Arestas)
Organiza todas as arestas do polígono por coordenada Y, onde cada "cesto" Y contém arestas que começam naquele Y.

#### AET (Active Edge Table - Tabela de Arestas Ativas)
Contém apenas as arestas ativas na linha de varredura atual, mantida ordenada por coordenada X.

### Estrutura de uma Aresta
```python
@dataclass
class Aresta:
    x: float      # Coordenada X atual
    y_max: int    # Y máximo da aresta
    dx_dy: float  # Incremento X por unidade Y
```

### Algoritmo em 6 Passos

1. **Construção da ET**: Organiza arestas por Y mínimo
2. **Inicialização**: Y atual = Y mínimo, AET vazia
3. **Transferência**: Move arestas da ET para AET
4. **Remoção**: Remove arestas com Y máximo = Y atual
5. **Ordenação**: Ordena AET por coordenada X
6. **Preenchimento**: Desenha pixels entre pares de arestas

## 📁 Estrutura do Projeto

```
PolygonFill---CG/
├── main.py          # Interface gráfica principal
├── polygon.py       # Implementação do algoritmo ET/AET
├── README.md        # Este arquivo
└── LICENSE          # Licença do projeto
```

## 🔍 Casos Especiais Tratados

- ✅ **Arestas horizontais**: Ignoradas (não contribuem para preenchimento)
- ✅ **Arestas verticais**: Processadas com dx_dy = 0
- ✅ **Vértices duplicados**: Removidos automaticamente
- ✅ **Polígonos inválidos**: Verificação de mínimo 3 vértices
- ✅ **Bounds da tela**: Verificação de limites para evitar erros
- ✅ **AET com número ímpar**: Tratamento especial da última aresta

## 🎯 Objetivos Acadêmicos

Este projeto demonstra:
- Implementação do algoritmo de preenchimento de polígonos
- Uso de estruturas de dados eficientes (ET/AET)
- Tratamento de casos especiais em computação gráfica
- Interface gráfica intuitiva para demonstração
- Preparação para portabilidade com OpenGL

## 🚀 Funcionalidades Avançadas

### Controle de Espessura Dinâmico
- Funciona em tempo real durante o desenho
- Preserva preenchimento ao alterar espessura
- Range de 1 a 10 pixels

### Sistema de Estados
- **DESENHANDO**: Adicionando vértices
- **PRONTO**: Polígono fechado, pronto para preencher
- **PREENCHIDO**: Polígono preenchido pelo algoritmo ET/AET

### Otimizações de Performance
- Fonte criada uma vez (não recriada a cada frame)
- Limpeza seletiva de áreas da tela
- Algoritmo eficiente com complexidade O(n)

## 🔧 Desenvolvimento

### Arquitetura do Código

#### main.py
- Interface gráfica com Pygame
- Sistema de eventos e botões
- Gerenciamento de estados da aplicação
- Renderização da UI e polígonos

#### polygon.py
- Implementação pura do algoritmo ET/AET
- Classes e estruturas de dados
- Lógica de preenchimento de polígonos
- Tratamento de casos especiais

### Extensibilidade
O código foi estruturado para facilitar:
- Portabilidade para OpenGL
- Adição de novos algoritmos de preenchimento
- Modificação da interface gráfica
- Implementação de novos casos especiais

## 📚 Referências

- Fundamentos de Computação Gráfica
- Algoritmos de Rasterização
- Técnicas de Preenchimento de Polígonos
- Estruturas de Dados em Computação Gráfica

## 👨‍💻 Autor

Desenvolvido como trabalho acadêmico de Computação Gráfica.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**🎓 Trabalho de Computação Gráfica - Algoritmo ET/AET para Preenchimento de Polígonos**