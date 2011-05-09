#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple

Filme = namedtuple('Filme', 'titulo diretor genero')
Diretor = namedtuple('Diretor', 'nome pais')

FILMES = [
    Filme('Central do Brasil', 'Walter Salles', 'drama'),
    Filme('Tropa de Elite', 'José Padilha', 'drama'),
    Filme('1941', 'Steven Spielberg', 'comédia'),
    Filme('O Bem Amado', 'Guel Arraes', 'comédia'),
    Filme('O Beijo da Mulher Aranha', 'Hector Babenco', 'drama'),
    Filme('Indiana Jones e o Tempo da Perdição', 'Steven Spielberg', 'aventura'),
    Filme('De Pernas pro Ar', 'Roberto Santucci', 'comédia'),
    Filme('A Lista de Schindler', 'Steven Spielberg', 'drama'),
]

DIRETORES = [
    Diretor('Guel Arraes', 'BR'),
    Diretor('Hector Babenco', 'AR'),
    Diretor('Walter Salles', 'BR'),
    Diretor('Roberto Santucci', 'BR'),
    Diretor('José Padilha', 'BR'),
    Diretor('Steven Spielberg', 'US'),
]    

def eh_chave(colecao, atrib):
    return len(colecao) == len(set(getattr(d, atrib) for d in colecao))
    
def existe(colecao, atrib, valor):
    return valor in (getattr(t, atrib) for t in colecao)

assert eh_chave(FILMES, 'titulo')
    
assert eh_chave(DIRETORES, 'nome')

# verificar integridade referencial
for f in FILMES:
    assert existe(DIRETORES, 'nome', f.diretor), '%s nao encontrado em DIRETORES' % f.diretor

print '1. Obter os diretores do filme “Central do Brasil”'

## nome do diretor
print [f.diretor for f in FILMES if f.titulo=='Central do Brasil']
    
## tupla do diretor
print [d for d in DIRETORES 
         for f in FILMES 
         if d.nome==f.diretor and f.titulo=='Central do Brasil']


print '2. Obter os nomes dos diretores brasileiros que fizeram algum filme cujo gênero é “comédia”.'

print [d.nome for d in DIRETORES 
              for f in FILMES 
              if d.nome==f.diretor and f.genero=='comédia' and d.pais=='BR']


print '3. Obter os nomes dos diretores que não fizeram nenhum filme no gênero “aventura”.'

print [d.nome for d in DIRETORES
              if d.nome not in 
                  [f.diretor for f in FILMES if f.genero=='aventura']]
                  
print '4. Obter os nomes dos diretores que fizeram pelo menos um filme de cada gênero presente na tabela FILME.'




                  

