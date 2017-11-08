import ply.lex as lex
import re
import codecs
import os
import sys

keywords = [
        'INTEGER', 'REAL',

        'READ', 'WRITE', 'FORMAT',
        'END', 'STOP',
        'CALL', 'CONTINUE',
          'DO',
        'PAUSE',

        'IF',

    	]

tokens = keywords + [
        'POWER', 'RPAREN','LPAREN', 'TIMES', 'MINUS',
        'PLUS','COMMA','DIVIDE',
        # Operadores logicos
        'LT', 'LE', 'GT', 'GE', 'EQ','GTE','LTE','NE',

        # Literales

        'ID', 'GOTO','AND','OR','NOT'
    ]

literals = '+-*/(),**'

t_ignore = '\t | \r'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\*\*'
#t_ODD = r'ODD'###

t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

t_INTEGER = r'\d+'
t_REAL = r'\d+\.\d*(E[-+]?[1-9][0-9]?)?'
t_GOTO = r'GO\s?TO'

# Ignorar Comentarios
def t_comment( t):
    r'C.*'
    pass

# Constantes Reales
def t_RCONST( t):
    r'\d+\.\d*(E[-+]?[1-9][0-9]?)?'
    t.value = float(t.value)
    return t

# Constantes Enteras
def t_ICONST( t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para identificadores
def t_ID( t):
    r'[A-Z][A-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t

# Regla para seguimiento a las lineas
def t_newline( t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error( t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)





analizador = lex.lex()
