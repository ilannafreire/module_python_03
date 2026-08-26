# Guia de estudos: Python Collections

Este guia acompanha o `module03.pdf` e explica o que estudar, como pensar e
como começar cada exercício. Ele não contém implementações prontas.

## 1. Como estudar este módulo

Para cada exercício, siga sempre este ciclo:

1. Reescreva o pedido com suas próprias palavras.
2. Separe entrada, processamento e saída.
3. Liste os casos normais, vazios e inválidos.
4. Escolha a collection que representa melhor os dados.
5. Escreva o algoritmo em pseudocódigo antes do Python.
6. Implemente uma parte pequena e execute-a.
7. Compare a saída com o exemplo do PDF.
8. Explique cada linha sem consultar o código de outra pessoa.

Não tente fazer os sete exercícios de uma vez. A ordem foi desenhada para
introduzir uma ideia por vez.

## 2. Fundamentos que você precisa dominar

### 2.1 Programa, função e fluxo

Um programa Python executa instruções de cima para baixo. Uma função agrupa um
processamento e pode receber dados e devolver um resultado.

Você precisa reconhecer:

- atribuição: guardar um valor em uma variável;
- chamada de função: pedir que uma operação seja executada;
- `if`/`else`: escolher um caminho;
- `for`: repetir para cada item de uma sequência;
- `while`: repetir enquanto uma condição for verdadeira;
- `return`: devolver um resultado e sair da função;
- `None`: ausência de valor.

Antes de escrever, pergunte: qual dado entra nesta etapa, qual transformação
acontece e qual valor sai?

### 2.2 Tipos e conversão

Os tipos centrais são `str`, `int`, `float`, `list`, `tuple`, `set` e `dict`.
Argumentos de terminal e valores de `input()` chegam como texto. Portanto, um
score precisa ser convertido antes de participar de uma soma, e uma coordenada
precisa virar `float` antes de entrar na fórmula.

Conversão pode falhar. Esse é o motivo para usar `try`/`except` ao redor da
operação de conversão, tratando o erro e permitindo que o programa continue.

### 2.3 Type hints

Toda função criada deve declarar os tipos dos parâmetros e do retorno. O
retorno de uma função que lê uma posição, por exemplo, deve deixar claro que é
uma tupla de três números. O type hint documenta a intenção e permite que
`mypy` encontre inconsistências antes da execução.

Não use type hints para esconder uma decisão que você ainda não tomou. Primeiro
decida qual dado a função recebe e devolve; depois escreva a anotação.

### 2.4 Índices, fatias e mutabilidade

Listas são ordenadas e mutáveis: podem crescer, perder itens e ter elementos
alterados. Tuplas também são ordenadas, mas não devem ser modificadas depois de
criadas. Em ambos os casos, a posição começa no índice zero.

Ao percorrer uma coleção, escolha entre:

- precisar do item: percorrer os valores;
- precisar da posição: percorrer índices;
- precisar dos dois: usar uma forma que produza índice e valor.

Essa escolha afeta diretamente os exercícios 0, 1 e 2.

### 2.5 Exceções

Uma exceção é um sinal de que uma operação não pôde ser concluída. O padrão
mental é: tentar somente a operação que pode falhar, capturar o erro esperado,
informar o usuário e decidir se deve ignorar a entrada ou pedir outra.

Evite capturar qualquer erro sem critério. Um bloco amplo pode esconder um bug
seu. Neste módulo, os casos mais importantes são conversões inválidas e
formatos de entrada incorretos.

## 3. Collections em uma página

| Estrutura | Use quando | Propriedade essencial |
| --- | --- | --- |
| Lista | Há uma sequência de valores | Ordenada, indexada e mutável |
| Tupla | Um grupo fixo de valores | Ordenada e imutável |
| Conjunto | Só importam valores únicos | Não permite duplicatas |
| Dicionário | Há uma relação chave-valor | Consulta por chave |
| Gerador | Valores devem surgir sob demanda | Produz com `yield` |

Escolher uma collection é parte da solução. Não transforme tudo em lista por
força: o exercício está avaliando justamente a representação dos dados.

## 4. Exercício 0: Command Quest

### O que está sendo pedido

Usar `sys.argv` para mostrar o nome do programa, quantos argumentos o usuário
passou, cada argumento numerado e o total de elementos da lista completa.

### O que o exercício ensina

Ensina que argumentos de linha de comando chegam como uma lista de strings e
que o primeiro elemento dessa lista é o nome do programa.

### Como começar

1. Importe apenas o que o subject autoriza.
2. Observe separadamente o primeiro elemento e os elementos restantes.
3. Calcule a quantidade de argumentos do usuário.
4. Trate o caso em que não existe nenhum argumento além do nome.
5. Para a enumeração, mantenha o número exibido alinhado com a posição real.
6. Reproduza a ordem e os rótulos da saída do exemplo.

Pseudocódigo:

```text
ler a lista de argumentos
mostrar o nome do programa
se não houver argumentos do usuário:
    mostrar mensagem de ausência
senão:
    mostrar quantidade
    percorrer os argumentos do usuário
    mostrar índice e valor de cada um
mostrar total da lista completa
```

### Testes para fazer

- executar sem argumentos;
- passar um argumento;
- passar três argumentos;
- passar uma string entre aspas contendo espaços.

Pergunta de avaliação: por que o total é uma unidade maior que a quantidade de
argumentos recebidos?

## 5. Exercício 1: Score Cruncher

### O que está sendo pedido

Receber scores pela linha de comando, aceitar os numéricos, descartar os
inválidos com mensagem e calcular quantidade, soma, média, maior score, menor
score e intervalo.

### O que o exercício resolve

Resolve uma pequena etapa de limpeza e análise de dados: entradas humanas são
imprevisíveis, mas os cálculos só devem usar dados válidos.

### Conceitos necessários

- lista de scores válidos;
- conversão de texto para inteiro;
- `try`/`except`;
- acumulador em um loop;
- diferença entre maior e menor;
- prevenção de `max()`/`min()` em lista vazia.

### Como começar

1. Separe o nome do programa dos parâmetros.
2. Crie a lista que receberá somente os scores convertidos.
3. Percorra cada texto e tente convertê-lo.
4. Ao falhar, imprima o parâmetro inválido e continue.
5. Depois do loop, verifique se a lista ficou vazia.
6. Só então calcule as estatísticas e formate a saída.

Pseudocódigo:

```text
criar lista vazia de scores
para cada parâmetro:
    tentar converter para inteiro
    se funcionar, adicionar à lista
    se falhar, informar e ignorar
se a lista estiver vazia:
    mostrar instrução de uso
senão:
    calcular quantidade, total, média, máximo, mínimo e intervalo
```

### Testes para fazer

- nenhum argumento;
- todos válidos;
- todos inválidos;
- mistura de válidos e inválidos;
- um único score;
- scores iguais, para conferir intervalo zero.

Pergunta de avaliação: por que a validação precisa terminar antes de chamar
`max()` e `min()`?

## 6. Exercício 2: Position Tracker

### O que está sendo pedido

Ler coordenadas no formato `x,y,z`, repetir a pergunta enquanto a entrada for
inválida, guardar cada posição como tupla de floats e calcular duas distâncias.

### O que o exercício resolve

Modela a posição de um jogador em um espaço 3D e demonstra como uma tupla pode
representar um registro pequeno e fixo.

### Conceitos necessários

- `input()` e strings;
- separação de texto por vírgula;
- remoção de espaços nas partes;
- conversão para `float`;
- `while` para novas tentativas;
- retorno de uma tupla;
- fórmula de distância euclidiana em três dimensões.

### Como começar

1. Desenhe a função de leitura: entrada textual entra, tupla sai.
2. Dentro de um loop, leia a linha e separe os três componentes.
3. Verifique a quantidade de componentes antes de convertê-los.
4. Converta cada componente; se falhar, mostre o erro e repita.
5. Quando válido, retorne a tupla.
6. No fluxo principal, chame a função duas vezes e use a fórmula indicada no
   PDF para o centro e para as duas posições.
7. Arredonde somente na apresentação, não durante o cálculo.

Pseudocódigo da leitura:

```text
enquanto a entrada não for válida:
    pedir x,y,z
    separar em três partes
    tentar converter as três partes para float
    se falhar, explicar o problema e repetir
retornar (x, y, z)
```

### Testes para fazer

- texto sem vírgulas;
- duas ou quatro partes;
- uma parte não numérica;
- espaços ao redor dos valores;
- ponto de origem;
- duas posições iguais.

Pergunta de avaliação: por que a função deve devolver uma tupla, e não três
variáveis independentes?

## 7. Exercício 3: Achievement Hunter

### O que está sendo pedido

Gerar conquistas aleatórias para pelo menos quatro jogadores e comparar os
conjuntos para obter união, interseção e diferenças.

### O que o exercício resolve

Resolve consultas sobre pertencimento e sobreposição: quais conquistas existem,
quais todos têm, quais são exclusivas e quais faltam para cada jogador.

### Conceitos necessários

- conjunto e remoção automática de duplicatas;
- escolha aleatória;
- união de conjuntos;
- interseção de conjuntos;
- diferença entre conjuntos;
- conjunto vazio e sua representação;
- repetição sobre jogadores.

### Como começar

1. Crie uma coleção fixa de nomes de conquistas.
2. Pense na função geradora: ela recebe a coleção disponível, escolhe uma
   quantidade e devolve um conjunto.
3. Crie pelo menos quatro jogadores e associe um conjunto a cada um.
4. Comece o conjunto de todas as conquistas com um jogador e faça união com os
   demais.
5. Comece as conquistas comuns com um jogador e faça interseção sucessiva.
6. Para exclusividade, compare o conjunto do jogador com a união dos outros.
7. Para ausências, subtraia o conjunto do jogador do conjunto total possível.

Pseudocódigo das análises:

```text
todas = união dos conjuntos dos jogadores
comuns = interseção dos conjuntos dos jogadores
para cada jogador:
    outros = união dos conjuntos dos demais
    exclusivas = conquistas do jogador menos outros
    faltantes = conjunto possível menos conquistas do jogador
```

### Testes para fazer

- execute várias vezes e observe a aleatoriedade;
- use conjuntos pequenos para verificar manualmente;
- confira se nenhuma conquista se repete no mesmo jogador;
- confira o caso de interseção vazia;
- confira o caso em que um jogador tem todas as conquistas.

Pergunta de avaliação: qual operação você usaria para descobrir o que um
jogador tem e todos os outros também têm?

## 8. Exercício 4: Inventory Master

### O que está sendo pedido

Interpretar argumentos no formato `item:quantidade`, rejeitar parâmetros
inválidos ou repetidos, armazenar os dados em um dicionário e produzir uma
análise do inventário.

### O que o exercício resolve

Transforma texto de entrada em dados estruturados e calcula distribuição,
percentuais e extremos de um inventário.

### Conceitos necessários

- dicionário e acesso por chave;
- separação de chave e valor;
- conversão para inteiro;
- detecção de chave repetida;
- `dict.keys()` e `dict.values()`;
- soma e percentual;
- preservação da ordem de inserção para desempate.

### Como começar

1. Crie um dicionário vazio.
2. Para cada parâmetro, valide o formato antes de converter a quantidade.
3. Extraia nome e quantidade, convertendo apenas a parte numérica.
4. Verifique se o item já existe antes de inseri-lo.
5. Depois da leitura, crie a lista de itens e calcule o total.
6. Só calcule percentuais se houver inventário e total adequado.
7. Determine maior e menor respeitando o primeiro item em caso de empate.
8. Use `update()` para acrescentar o item final pedido pelo subject.

Pseudocódigo da entrada:

```text
para cada parâmetro:
    se não tiver exatamente item e quantidade:
        informar erro
    senão se item já estiver no dicionário:
        informar redundância
    senão tentar converter quantidade
        se funcionar, inserir
        se falhar, informar erro
```

### Testes para fazer

- nenhum parâmetro;
- item válido;
- parâmetro sem `:`;
- quantidade não numérica;
- item repetido;
- empate no maior e no menor;
- total igual a zero, se o subject permitir esse caso.

Pergunta de avaliação: por que um dicionário é mais apropriado que uma lista
de pares para consultar se um item já existe?

## 9. Exercício 5: Stream Wizard

### O que está sendo pedido

Criar um gerador infinito de eventos aleatórios, consumir mil eventos, guardar
dez eventos em uma lista e criar outro gerador que os remove aleatoriamente até
a lista ficar vazia.

### O que o exercício resolve

Mostra como processar um fluxo potencialmente grande sem criar todos os dados
antecipadamente e como consumir uma fonte de dados progressivamente.

### Conceitos necessários

- função geradora;
- `yield` versus `return`;
- `next()`;
- `Generator` nos type hints;
- lista mutável;
- remoção por índice;
- `for` sobre um gerador.

### Como começar

1. Defina listas de jogadores e ações.
2. Faça a função de evento entrar em um loop infinito.
3. A cada passagem, escolha um jogador e uma ação e produza uma tupla com
   `yield`.
4. Crie uma instância do gerador; não chame a função repetidamente para cada
   evento.
5. Use um loop com mil repetições e `next()` para exibir os eventos.
6. Monte uma lista separada com dez chamadas ao gerador.
7. O segundo gerador deve continuar enquanto houver itens, escolher uma posição,
   remover o item e produzi-lo.
8. Consuma o segundo gerador diretamente em um `for`.

Pseudocódigo do consumidor:

```text
enquanto a lista não estiver vazia:
    escolher uma posição aleatória
    remover o evento dessa posição
    produzir o evento removido
```

### Testes para fazer

- chamar `next()` várias vezes e observar que o gerador não termina;
- conferir exatamente mil eventos no primeiro fluxo;
- conferir dez eventos na lista inicial;
- conferir que cada evento aparece uma vez no consumo;
- conferir que a lista termina vazia.

Pergunta de avaliação: qual seria o custo de guardar um fluxo infinito inteiro
em uma lista?

## 10. Exercício 6: Data Alchemist

### O que está sendo pedido

Usar list comprehensions para transformar e filtrar nomes e dict comprehensions
para criar um mapa de scores e outro mapa somente com scores acima da média.

### O que o exercício resolve

Resolve transformações e filtros compactos sobre dados tabulares, mantendo a
relação entre cada jogador e seu score.

### Conceitos necessários

- expressão de transformação;
- condição de filtro;
- list comprehension;
- dict comprehension;
- `str.capitalize()`;
- média de uma lista de valores;
- comparação com a média;
- aleatoriedade e resultados variáveis.

### Como começar

1. Crie a lista inicial exatamente com nomes em capitalizações diferentes.
2. Escreva em palavras a transformação “capitalizar cada nome”.
3. Converta essa transformação em uma list comprehension.
4. Para o segundo resultado, filtre a lista original usando a condição pedida.
5. Crie o dicionário de scores a partir da lista totalmente capitalizada.
6. Calcule a média dos valores desse dicionário.
7. Crie o segundo dicionário mantendo somente os pares cujo score supera a
   média.
8. Mantenha cada comprehension em uma única linha, como pede o subject.

Pseudocódigo:

```text
nomes_normalizados = transformar cada nome da lista inicial
nomes_que_já_estavam_capitalizados = filtrar lista inicial pela condição
scores = criar um score aleatório para cada nome normalizado
média = soma dos scores dividida pela quantidade
scores_altos = manter pares cujo score seja maior que a média
```

### Testes para fazer

- conferir que a quantidade de nomes não muda na normalização;
- conferir que o filtro usa a lista inicial, não a normalizada;
- verificar que nenhum score igual à média entra nos scores altos;
- executar mais de uma vez e observar novos scores;
- conferir o caso de uma lista com um único nome em um teste isolado.

Pergunta de avaliação: qual é a diferença entre transformar todos os nomes e
selecionar somente nomes que já satisfaziam uma condição?

## 11. Plano de execução recomendado

### Sessão 1: base e terminal

Estude funções, listas, índices, `sys.argv` e saída formatada. Faça o ex. 0 e
teste todos os formatos de argumentos.

### Sessão 2: validação e análise

Revise conversões, `try`/`except`, acumuladores e valores extremos. Faça o ex.
1 começando pelos casos vazios.

### Sessão 3: dados fixos

Estude tuplas, parsing de strings e a fórmula de distância. Faça o ex. 2 com
uma função de leitura isolada.

### Sessão 4: operações de conjuntos

Desenhe quatro círculos ou tabelas de conquistas no papel e simule união,
interseção e diferença antes do ex. 3.

### Sessão 5: chave e valor

Pratique converter `nome:quantidade` e detectar duplicatas. Depois faça o ex. 4
em duas fases: montagem e análise.

### Sessão 6: fluxo sob demanda

Pratique uma função com `yield`, `next()` e um `for`. Depois implemente os dois
geradores do ex. 5.

### Sessão 7: síntese

Revise a forma geral de comprehensions e faça o ex. 6. Por fim, explique como
cada exercício escolheria uma collection diferente.

## 12. Checklist antes da entrega

- [ ] Consigo explicar a função principal de cada arquivo.
- [ ] Sei dizer qual collection cada exercício exige e por quê.
- [ ] Testei entradas válidas, vazias e inválidas.
- [ ] Não usei imports fora da lista autorizada.
- [ ] Todas as funções têm type hints.
- [ ] Não usei leitura ou escrita de arquivos.
- [ ] A saída segue a ordem e os rótulos do PDF.
- [ ] Executei `flake8`.
- [ ] Executei `mypy`.
- [ ] Consigo justificar minhas escolhas sem depender de código gerado.

O objetivo final é conseguir reconstruir cada solução a partir do enunciado,
do pseudocódigo e dos conceitos, e não memorizar uma resposta pronta.