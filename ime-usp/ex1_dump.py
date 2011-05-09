#!/usr/bin/env python
# coding: utf-8

from collections import namedtuple
from pprint import pprint

Filme = namedtuple('filme', 'titulo nome_do_diretor genero')
Diretor = namedtuple('diretor', 'nome pais')

FILME = [
    Filme('Central do Brasil', 'Walter Salles', 'drama'),
    Filme('Tropa de Elite', 'José Padilha', 'drama'),
    Filme('1941', 'Steven Spielberg', 'comédia'),
    Filme('O Bem Amado', 'Guel Arraes', 'comédia'),
    Filme('O Beijo da Mulher Aranha', 'Hector Babenco', 'drama'),
    Filme('Indiana Jones e o Tempo da Perdição', 'Steven Spielberg', 'aventura'),
    Filme('De Pernas pro Ar', 'Roberto Santucci', 'comédia'),
    Filme('A Lista de Schindler', 'Steven Spielberg', 'drama'),
]

DIRETOR = [
    Diretor('Guel Arraes', 'BR'),
    Diretor('Hector Babenco', 'AR'),
    Diretor('Walter Salles', 'BR'),
    Diretor('Roberto Santucci', 'BR'),
    Diretor('José Padilha', 'BR'),
    Diretor('Steven Spielberg', 'US'),
]


def dump_rdb():
    ''' Dump data in WinRDBI .rdb format

    Example schema from WinRDBI distribution:

    @employee(eID/char,eLast/char,eFirst/char,eTitle/char,eSalary/numeric):eID
    '''

    keys = {'filme':'titulo', 'diretor':'nome'}

    for rel in (Filme, Diretor):
        nome = rel.__name__
        atribs = ','.join('{0}/char'.format(field) for field in rel._fields)
        key = keys[nome]
        print '@{nome}({atribs}):{key}'.format(**locals())
        for tup in globals()[nome.upper()]:
            print ','.join("'%s'" % atr for atr in tup)


def dump_prolog():
    ''' Dump data as Prolog facts '''

    for rel in (Filme, Diretor):
        nome = rel.__name__.lower()
        for tup in globals()[nome.upper()]:
            print "%s(%s)." % (nome, ','.join("'%s'" % atr for atr in tup))

dump_prolog()


