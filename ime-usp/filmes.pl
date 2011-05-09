/********************************************************************
IME/USP
MAC426 – Lista de Exercícios: Consultas ao modelo relacional
Prof. Marcelo Finger
Primeiro Semestre de 2011

Exercício 1

Considere os seguintes esquemas:

FILME(Título, Nome do Diretor, Gênero)

DIRETOR(Nome, Nacionalidade)

Assuma que títulos identificam univocamente filmes e nomes identificam
univocamente diretores. Suponha também que cada filme tem exatamente
um diretor. Expresse cada uma das consultas abaixo em álgebra
relacional, em cálculo relacional de domínio e tuplas, em Datalog e em
SQL.
*********************************************************************/

filme('Central do Brasil','Walter Salles','drama').
filme('Tropa de Elite','José Padilha','drama').
filme('1941','Steven Spielberg','comédia').
filme('O Bem Amado','Guel Arraes','comédia').
filme('O Beijo da Mulher Aranha','Hector Babenco','drama').
filme('Indiana Jones e o Tempo da Perdição','Steven Spielberg','aventura').
filme('De Pernas pro Ar','Roberto Santucci','comédia').
filme('A Lista de Schindler','Steven Spielberg','drama').
diretor('Guel Arraes','BR').
diretor('Hector Babenco','AR').
diretor('Walter Salles','BR').
diretor('Roberto Santucci','BR').
diretor('José Padilha','BR').
diretor('Steven Spielberg','US').

/* 1. Obter os diretores do filme “Central do Brasil”. */

resp1(Diretor) :- filme('Central do Brasil', Diretor, _).

/* 2. Obter os nomes dos diretores brasileiros que fizeram algum filme
      cujo gênero é “comé́dia”. */

brasileiro(Diretor) :- diretor(Diretor,'BR').
comedia(Titulo) :- filme(Titulo, Diretor, 'comédia').

resp2(Diretor) :- diretor(Diretor,'BR'),
         filme(_, Diretor, 'comédia').

/* 3. Obter os nomes dos diretores que não fizeram nenhum filme no
      gênero “aventura”. */

resp3(Diretor) :- diretor(Diretor,_),
                  \+ filme(_, Diretor, 'aventura').

/* 4. Obter os nomes dos diretores que fizeram pelo menos um filme de
      cada gênero presente na tabela FILME. */

