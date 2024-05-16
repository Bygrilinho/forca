% Regras de inferência

% Retorna um vetor com todas as palavras da base de conhecimento
todas_palavras(Palavras) :-
  findall(Palavra, palavra(Palavra), Palavras).

% Verifica se uma letra está presente em uma palavra
letra(Palavra, Letra) :-
  atom_chars(Palavra, Letras),
  member(Letra, Letras).

% Verifica quais palavras possuem uma letra em uma posição específica
letra_em_posicao(Letra, Posicao, Lista, Palavras) :-
  findall(Palavra, (member(Palavra, Lista), posicao(Palavra, Letra, Posicao)), Palavras).

% Verifica quais palavras não possuem uma letra
nao_letra(Letra, Lista, Palavras) :-
  findall(Palavra, (member(Palavra, Lista), not(letra(Palavra, Letra))), Palavras).

% Verifica quais palavras não possuem uma letra em uma posição específica
nao_letra_em_posicao(Letra, Posicao, Lista, Palavras) :-
  findall(Palavra, (member(Palavra, Lista), not(posicao(Palavra, Letra, Posicao))), Palavras).

% Verifica qual é a posição de uma letra em uma palavra
posicao(Palavra, Letra, Posicao) :-
  atom_chars(Palavra, Letras),
  nth1(Posicao, Letras, Letra).

% Verifica se uma palavra tem um tamanho específico
tamanho(Palavra, Tamanho) :-
  atom_chars(Palavra, Letras),
  length(Letras, Tamanho).

% Retorna todas as palavras com um tamanho específico
palavras_tamanho(Lista, Tamanho, Palavras) :-
  findall(Palavra, (member(Palavra, Lista), tamanho(Palavra, Tamanho)), Palavras).

% Conta quantas vezes uma letra aparece em uma lista de palavras
contar_letra_base(Letra, Lista, Contagem) :-
  findall(Cont, (member(Palavra, Lista), contar_letra(Letra, Palavra, Cont)), Contagens),
  sum_list(Contagens, Contagem).

% Conta quantas vezes uma letra aparece em uma palavra
contar_letra(Letra, Palavra, Contagem) :-
  atom_chars(Palavra, ListaLetras), % Transforma a palavra em uma lista de letras
  contar(Letra, ListaLetras, Contagem). 

% Conta quantas vezes uma letra aparece em uma lista de letras
contar(_, [], 0).
contar(Letra, [H|T], Contagem) :-
  (H = Letra -> contar(Letra, T, ContagemRestante), Contagem is ContagemRestante + 1;
    contar(Letra, T, Contagem)).