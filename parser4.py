import ply.yacc as yacc
import os
import codecs
import re
from sys import stdin
from lexer5 import tokens
"""
tokens = lexer5.tokens
"""
precedence = (
	('right','IF'),

	('left','NE'),
	('left','LT','LTE','GT','GTE'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),

	('left','LPAREN','RPAREN'),
)


def p_PROGRAM(p):
    '''PROGRAM : PROGRAM statement'''

    pass

def p_PROGRAM_statement(p):
    '''PROGRAM  : statement'''
    p[0] = PROGRAM(p[1],"PROGRAM")





def p_statement(p):
    '''statement : INTEGER command'''
    P[0] = statement(p[2],"statement")


def p_statement_command(p):
    '''statement : command'''
    p[0] = statament_command(p[1],"statement command")

#-------------------------------

#GO TO STATEMENT
def p_command_GOTO(p):
    '''command : GOTO LPAREN intlist RPAREN ',' variable'''
    p[0] = command_GOTO(p[3],p[6],"GOTO")


def p_command_GOTO_INTEGER(p):
    '''command : GOTO INTEGER'''
    P[0] = command_GOTO_INTEGER(p[2],"goto INTEGER")



# READ statement
def p_command_read(p):
    '''command : READ LPAREN INTEGER ',' INTEGER RPAREN varlist'''
    p[0] = commad_read(p[7],"comand read")

def p_command_read_a(p):
    '''command :  READ LPAREN '*' RPAREN varlist'''
    p[0] = command_read_a(p[7],"command_read_a")


# IF statement

def p_command_if(p):
    '''command : IF LPAREN relexpr RPAREN INTEGER COMMA INTEGER COMMA INTEGER'''
    p[0] = comand_if(p[3],"command if")

# END statement

def p_command_end(p):
    '''command : END'''
    p[0] = command_end(END(p[1]),"command end")

# FORMAT statement ??
def p_comand_format(p):
    ''' command : FORMAT LPAREN RPAREN'''
    p[0] = command_format(FORMAT[1],LPAREN[2],RPAREN[3],"COMAND FORMAT")
# STOP statement

def p_command_stop(p):
    '''command : STOP stopoption'''
    p[0] = comand_stop(p[2])

def p_stopoption(p):
    '''stopoption : INTEGER'''
    pass

def p_stopoption_a(p):
        '''stopoption : empty'''


# PAUSE statement

def p_command_pause(p):
    '''command : PAUSE INTEGER'''
    pass

def p_command_pause_a(p):
    '''command : PAUSE'''
    pass


#CONTINUE statement

def p_command_continue(p):
    '''command : CONTINUE'''
    pass


#call statement

def p_command_call(p):
    '''command : CALL ID LPAREN numlist RPAREN'''
    pass

def p_command_assign(p):
    '''command : variable EQ expr'''
    pass

def p_command_write(p):
    '''command : WRITE LPAREN INTEGER ',' INTEGER RPAREN varlist'''

def p_command_write_a(p):
    '''command : WRITE LPAREN '*' RPAREN varlist'''
    pass

def p_command_do(p):
     '''command :   DO INTEGER variable EQ INTEGER ',' INTEGER ',' INTEGER'''


def p_command_do_a(p):
    '''command : DO INTEGER variable EQ INTEGER ',' INTEGER '''
    pass
def p_command_call_a(p):
    '''command : CALL'''




def p_expr_operations(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr POWER expr'''

    pass



def p_expr_number(p):
    '''expr : INTEGER
            | REAL'''
    pass


def p_expr_variable(p):
    '''expr : variable'''
    pass


def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    pass


def p_expr_unary(p):
    '''expr : MINUS expr '''
    pass

# Relational expressions


def p_relexpr_aritmetic(p):
    '''relexpr : expr LT expr
               | expr LE expr
               | expr GT expr
               | expr GE expr
               | expr EQ expr
               | expr NE expr
               | expr LTE expr
               | expr GTE expr '''
    pass

def p_relexpr_and(p):
     '''relexpr : relexpr AND relexpr'''
     pass

def p_relexpr_or(p):
    '''relexpr : relexpr OR relexpr'''
    pass



def p_relexpr_not(p):
    '''relexpr : NOT relexpr'''
    pass

# Variables


def p_variable(p):
    '''variable : ID
              | ID LPAREN expr RPAREN
              | ID LPAREN expr COMMA expr RPAREN'''
    if len(p) == 2:
        p[0] = (p[1], None, None)
    elif len(p) == 5:
        p[0] = (p[1], p[3], None)
    else:
        p[0] = (p[1], p[3], p[5])

# Builds a list of variable targets as a Python list


def p_varlist(p):
    '''varlist : varlist COMMA variable
               | variable'''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


# Builds a list of numbers as a Python list

def p_numlist(p):
    '''numlist : numlist COMMA number
               | number'''

    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


def p_number(p):
    '''number  : INTEGER
               | REAL'''

    p[0] = eval(p[1])

# A signed number.


def p_number_signed(p):
    '''number  : MINUS INTEGER
               | MINUS REAL'''
    p[0] = eval("-" + p[2])

# List of targets for a print statement
# Returns a list of tuples (label,expr)


def p_intlist(p):
    '''intlist : intlist ',' INTEGER'''


def p_intlist_a(p):
    '''intlist : INTEGER'''
    pass


# Catastrophic error handler

def p_empty(p):
    '''empty : '''
    ##
    pass

def p_error(p):
    print "SYNTAX ERROR AaaaT EOF ", p








def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta == False:
		numArchivo = raw_input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print "Has escogido \"%s\" \n" %files[int(numArchivo)-1]

	return files[int(numArchivo)-1]

directorio = '/home/mauricio/Documents/Compiladores/comprimido2/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print result
