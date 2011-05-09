%---------------------------------------------------------------------
%
%  MAC 5760 - Bancos de dados
%  IME-USP - Primeiro Semestre de 2011
%
%  Consultas na linguagem: Álgebra Relacional
%
%  Lista 1
%
%  Luciano Gama de Sousa Ramalho    n.usp 1002101
%  Data de entrega: 2011-04-04
%
%---------------------------------------------------------------------
% Exercício 1
%
% filme(titulo, nome_do_diretor, genero)    key: titulo
% diretor(nome, pais)               key: nome
%---------------------------------------------------------------------
% 1. Obter os diretores do filme “Central do Brasil”

respDirCentral :=
    project nome_do_diretor (select titulo = 'Central do Brasil' (filme));

% 2. Obter os nomes dos diretores brasileiros que fizeram algum filme
%    cujo gênero é “comédia”.'

qDirBras(nome_do_diretor) :=
    project nome (select pais = 'BR' (diretor));

respDirBrasComedia :=
    project nome_do_diretor (
        qDirBras njoin (
            select genero = 'comédia' (filme)));

% 3. Obter os nomes dos diretores que não fizeram nenhum filme no gênero
%    “aventura”.

qDirAventuras(nome) :=
    project nome_do_diretor (select genero = 'aventura' (filme));

respDirNaoAventura :=
    (project nome (diretor)) difference qDirAventuras;

% 4. Obter os nomes dos diretores que fizeram pelo menos um filme de
%    cada gênero presente na tabela FILME.

qGeneros := project genero(filme);
qDiretoresGenerosTodos := (project nome, genero (diretor product qGeneros));
qDiretoresGenerosFeitos(nome, genero) := project nome_do_diretor, genero (filme);
qDiretoresSemUmGenero := project nome (qDiretoresGenerosTodos difference qDiretoresGenerosFeitos);
respDiretoresVersateis := project nome (diretor difference (diretor njoin qDiretoresSemUmGenero));


