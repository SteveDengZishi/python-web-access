from sys import *

command = []
content = []
var_dic = {}

def lex(data):
	tok = ""
	special = ['(',')','\n']

	data = list(data)
	#print(data)
	for char in data:
		if char not in special:
			tok+=char
			if tok == " ":
				tok = ""
		elif char == "(":
			command.append(tok)
			tok=""
		elif char == ")":
			content.append(tok)
			tok=""

def execute():
	for i in range(len(command)):
		if command[i]=="show":
			if content[i][0] == '\"':
				print(content[i].strip('\"'))
			else:
				print(var_dic[content[i]])
		elif command[i]=="assign":
			assign=content[i].split(':')
			var_dic[assign[0]]=assign[1]


def run():
	#print(len(argv), argv[0])
	data = open(argv[1],"r").read()
	lex(data)
	execute()

run()