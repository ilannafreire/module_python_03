# Análise do subject

## Visão geral

O módulo apresenta as principais collections do Python em uma sequência
progressiva. Cada exercício introduz uma estrutura ou técnica e a aplica a um
pequeno sistema de dados de jogos.

O foco não é apenas produzir uma saída específica: durante a avaliação, pode
ser necessário justificar a escolha da estrutura, demonstrar suas operações e
estender o programa.

## Regras gerais

- Usar Python 3.10 ou superior.
- Seguir o padrão `flake8`.
- Incluir type hints em todas as funções e métodos; verificar com `mypy`.
- Tratar exceções sem deixar o programa quebrar diante de entradas inválidas.
- Processar dados em memória, por argumentos de linha de comando ou por entrada
  interativa, sem operações de I/O em arquivos.
- Demonstrar operações básicas e técnicas avançadas da estrutura introduzida.
- Respeitar a lista de imports e funções autorizados de cada exercício.
- Entregar somente os arquivos solicitados dentro do repositório.

## Progressão conceitual

| Exercício | Tema principal | Entrada | Resultado esperado |
| --- | --- | --- | --- |
| 0 | `sys.argv` e listas | Linha de comando | Inspeção dos argumentos |
| 1 | Listas e tratamento de erros | Scores na linha de comando | Estatísticas dos scores válidos |
| 2 | Tuplas | Coordenadas 3D via `input()` | Distâncias entre posições |
| 3 | Conjuntos | Dados gerados aleatoriamente | Comparação de conquistas |
| 4 | Dicionários | Itens e quantidades na linha de comando | Análise do inventário |
| 5 | Geradores | Eventos aleatórios | Fluxo sob demanda e consumo |
| 6 | List/dict comprehensions | Lista de jogadores | Transformações e filtragem |

## Exercício 0: Command Quest

Arquivo: `ex0/ft_command_quest.py`  
Autorizado: `import sys`, `sys.argv`, `len()`, `print()`.

Objetivo: observar como o programa recebe os argumentos. A saída deve
identificar o nome do programa, a quantidade de argumentos recebidos, cada
argumento por índice e o total incluindo o nome do programa. É importante
considerar também a execução sem argumentos e argumentos com espaços.

Ponto de estudo: `sys.argv` é uma lista de strings; o primeiro elemento é o
nome do programa.

## Exercício 1: Score Cruncher

Arquivo: `ex1/ft_score_analytics.py`  
Autorizado: `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()`.

Objetivo: converter os scores válidos para uma lista e calcular quantidade,
total, média, maior valor, menor valor e intervalo. Entradas não numéricas
devem ser reportadas e descartadas. Sem scores, o programa deve mostrar uma
mensagem de uso em vez de tentar calcular estatísticas de uma lista vazia.

Ponto de estudo: separar validação, acumulação e cálculo evita chamar funções
estatísticas quando não há dados válidos.

## Exercício 2: Position Tracker

Arquivo: `ex2/ft_coordinate_system.py`  
Autorizado: `import math`, `math.sqrt()`, `input()`, `round()`, `print()`.

Objetivo: implementar a leitura repetida de coordenadas no formato `x,y,z`,
retornando uma tupla de três floats. O programa deve exibir os componentes,
calcular a distância até `(0, 0, 0)` e depois a distância entre duas posições.

Ponto de estudo: tuplas representam uma posição fixa; entradas com sintaxe ou
valores inválidos precisam ser rejeitadas e solicitadas novamente.

## Exercício 3: Achievement Hunter

Arquivo: `ex3/ft_achievement_tracker.py`  
Autorizado: `len()`, `print()`, `random`, `set()`, `union()`, `intersection()`,
`difference()`.

Objetivo: gerar conquistas aleatórias para pelo menos quatro jogadores e usar
conjuntos para encontrar todas as conquistas distintas, as compartilhadas por
todos, as exclusivas de cada jogador e as que faltam para cada jogador atingir
o conjunto total.

Ponto de estudo: conjuntos eliminam duplicatas e tornam operações de união,
interseção e diferença expressivas. A aleatoriedade também exige aceitar que
alguns resultados possam variar entre execuções.

## Exercício 4: Inventory Master

Arquivo: `ex4/ft_inventory_system.py`  
Autorizado: `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`,
`dict.keys()`, `dict.values()`, `dict.update()`.

Objetivo: interpretar parâmetros no formato `<item>:<quantity>`, rejeitar
sintaxe inválida, quantidades inválidas e itens repetidos, e guardar os itens
válidos em um dicionário. Depois, exibir itens, quantidade total, percentual de
cada item, item mais abundante, item menos abundante e o inventário atualizado
com um novo item.

Ponto de estudo: dicionários associam cada nome a uma quantidade. Em empates,
deve prevalecer o primeiro item recebido na linha de comando.

## Exercício 5: Stream Wizard

Arquivo: `ex5/ft_data_stream.py`  
Autorizado: `next()`, `range()`, `len()`, `print()`, `typing.Generator`,
`random`.

Objetivo: criar um gerador infinito que produza eventos `(jogador, ação)` sob
demanda, consumir mil eventos e depois criar uma lista de dez eventos. Um
segundo gerador deve escolher e remover eventos dessa lista até esvaziá-la, e
ser usado diretamente em um `for`.

Ponto de estudo: `yield` permite produzir valores sem materializar um fluxo
inteiro em memória. O tipo do gerador deve ser declarado.

## Exercício 6: Data Alchemist

Arquivo: `ex6/ft_data_alchemist.py`  
Autorizado: `random`, `print()`, `len()`, `sum()`, `round()`.

Objetivo: criar uma lista com nomes em diferentes capitalizações e usar uma
list comprehension para normalizar todos os nomes e outra para filtrar apenas
os originalmente capitalizados. Em seguida, criar um dicionário de scores
aleatórios e um segundo dicionário contendo apenas scores acima da média,
ambos com comprehensions.

Ponto de estudo: cada comprehension deve ficar em uma única linha, salvo se o
tamanho exigir quebra. A média deve ser calculada antes do filtro de scores.

## Estratégia de estudo

1. Ler o enunciado e listar as entradas, saídas, casos inválidos e funções
   autorizadas do exercício.
2. Escrever exemplos manuais de casos normais, vazios, inválidos e limites.
3. Implementar somente depois de conseguir explicar a collection escolhida.
4. Rodar `flake8` e `mypy` em cada arquivo.
5. Fazer uma revisão por pares e preparar uma explicação das decisões tomadas.

## Checklist de entrega

- [ ] Todos os nomes de pastas e arquivos correspondem ao subject.
- [ ] Nenhum import ou recurso não autorizado foi usado.
- [ ] Funções têm type hints.
- [ ] Entradas inválidas são tratadas sem crash.
- [ ] Não há leitura ou escrita de arquivos.
- [ ] `flake8` não reporta problemas.
- [ ] `mypy` não reporta problemas.
- [ ] A implementação consegue ser explicada durante a avaliação.