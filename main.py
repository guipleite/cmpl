import sys

reserved_words = ["printf","and","or","!","if","while","else","scanf","true","false","func","return"]
declared_funcs = []

class PrePro():

    @staticmethod
    def filter(text):

        text = list(text)

        i = 0

        while(i!=len(text)):
            if text[i]=="\n":
                text[i] = ''
            if text[i]=="}": ##
                text[i] = "};"
            if text[i]=="/" and text[i+1]=="*":
                j=i
                while True:
                    i+=1
                    if text[i]=="*" and text[i+1]=="/":
                        break
                for k in range(j,i+2):
                    text[k] = ''

            if text[i] == '\t':
                text[i]=''
            i+=1

        text = "{"+"".join(text)+"} "

        return text

class Token():

    def __init__(self,tokenType,tokenValue):
        self.tokenType = tokenType
        self.tokenValue = tokenValue

class Node():

    def __init__(self):
        self.value = 0
        self.children = []
        self.Evaluate()

    def Evaluate(self):
        return self.value

class Tokenizer():

    def __init__(self,origin):
        self.origin = origin
        self.positon = 0
        self.actual = None
        self.counter = 0
        self.counterb = 0

        self.selectNext()
    
    def selectNext(self):
        if self.origin[self.positon] == " " :
            b4 = False
            if self.origin[self.positon-1].isdigit():
                b4 = True
            while self.positon<(len(self.origin)) and  self.origin[self.positon] == " ":
                self.positon+=1
            if b4 and self.positon<(len(self.origin)):
                if self.origin[self.positon].isdigit():
                    raise Exception("Erro, espaco entre numeros")        

        if self.positon==(len(self.origin)):
            self.actual = Token('' , 'EOF')
            return None
            
        if self.origin[self.positon] == "+":
            self.actual = Token('operator' , '+')
            self.positon+=1

        elif self.origin[self.positon] == "-":
            self.actual = Token('operator' , '-')
            self.positon+=1

        elif self.origin[self.positon] == "*":
            self.actual = Token('operator' , '*')
            self.positon+=1

        elif self.origin[self.positon] == "/":
            self.actual = Token('operator' , '/')
            self.positon+=1
        
        elif self.origin[self.positon] == ">":
            self.actual = Token('operator' , '>')
            self.positon+=1

        elif self.origin[self.positon] == "<" and self.origin[self.positon+1] != "?":
            self.actual = Token('operator' , '<')
            self.positon+=1

        elif self.origin[self.positon] == "{":
            self.actual = Token('command' , '{')
            self.positon+=1
            self.counterb-=1

        elif self.origin[self.positon] == "}":
            self.actual = Token('command' , '}')
            self.positon+=1
            self.counterb+=1

            if self.counterb>0:
                raise Exception("Erro, verifique a exprecao }")      

        elif self.origin[self.positon] == ";":
            self.actual = Token('endline' , ';')
            self.positon+=1

        elif self.origin[self.positon] == "!":
            self.actual = Token('un' , '!')
            self.positon+=1

        elif self.origin[self.positon] == ".":
            self.actual = Token('concat' , '.')
            self.positon+=1

        elif self.origin[self.positon] == ",":
            self.actual = Token('comma' , ',')
            self.positon+=1

        elif self.origin[self.positon] == '"':
            string = ''
            self.positon+=1

            while self.origin[self.positon]!='"':
                string+=self.origin[self.positon]
                self.positon+=1
                
            self.positon+=1
            self.actual = Token('str', string)

        elif self.origin[self.positon].isalpha():
            var = self.origin[self.positon]
            self.positon+=1
            while (self.origin[self.positon].isalnum() or self.origin[self.positon]=="_") and self.origin[self.positon] != "(":
                var+=self.origin[self.positon]
                
                if self.positon==(len(self.origin)-1):
                    break
                else:
                    self.positon+=1

            if var.lower() in reserved_words:
                self.actual = Token('res', var.lower())
                if self.actual.tokenValue == "func":
                    func = ''

                    self.positon+=1

                    while (self.origin[self.positon].isalnum() or self.origin[self.positon]=="_") and self.origin[self.positon] != "(":
                        func+=self.origin[self.positon]

                        if self.positon==(len(self.origin)-1):
                            break
                        else:
                            self.positon+=1

                    declared_funcs.append(func)

                    self.actual = Token('function_d', func)
            
            elif (var in declared_funcs):
                self.actual = Token('function_c', var)

            else:
                self.actual = Token('iden', var)

        elif self.origin[self.positon] == "=":
            if (self.origin[self.positon+1]=="="):
                self.actual = Token('eq' , '==')
                self.positon+=2
            else:
                self.actual = Token('assignment' , '=')
                self.positon+=1

        elif self.origin[self.positon] == ")" :
            self.actual = Token('close(' , ')')
            self.positon+=1
            self.counter-=1
            if self.counter<0:
                raise Exception("Erro, verifique a exprecao 1")      

        elif self.origin[self.positon] == "(" :
            self.actual = Token('open(' , '(')
            self.positon+=1
            self.counter+=1

        elif self.origin[self.positon].isdigit():

            num = ''
            
            while self.origin[self.positon].isdigit():
                num+=self.origin[self.positon]
                
                if self.positon==(len(self.origin)-1):
                    break
                else:
                    self.positon+=1

            self.actual = Token('int', int(num))  

        else:
            raise Exception("Erro, token invalido",self.origin[self.positon])        

class BinOp(Node):
    
    def __init__(self, value, child):
        self.value = value
        self.children = child
        
    def Evaluate(self,table):
        if self.value == '+':
            result = self.children[0].Evaluate(table)[0] + self.children[1].Evaluate(table)[0]
            return (result,"int")

        elif self.value == '-':
            result = self.children[0].Evaluate(table)[0] - self.children[1].Evaluate(table)[0]
            return (result,"int")

        elif self.value == '*':
            result = self.children[0].Evaluate(table)[0] * self.children[1].Evaluate(table)[0]
            return (result,"int")

        elif self.value == '/':
            result = self.children[0].Evaluate(table)[0] // self.children[1].Evaluate(table)[0]
            return (result,"int")

        elif self.value == '==':
            result = self.children[0].Evaluate(table)[0] == self.children[1].Evaluate(table)[0]
            return (result,"bool")
        
        elif self.children[0].Evaluate(table)[1]!="str" and  self.children[1].Evaluate(table)[1]!="str":
            if self.value == '>':
                result = self.children[0].Evaluate(table)[0] > self.children[1].Evaluate(table)[0]
                return (result,"bool")

            elif self.value == '<':
                result = self.children[0].Evaluate(table)[0] < self.children[1].Evaluate(table)[0]
                return (result,"bool")

            elif self.value == 'and':
                result = self.children[0].Evaluate(table)[0] and self.children[1].Evaluate(table)[0]
                return (result,"bool")
            
            elif self.value == 'or':
                result = self.children[0].Evaluate(table)[0] or self.children[1].Evaluate(table)[0]
                return (result,"bool")
        
        elif self.value == '.':
            result = str(self.children[0].Evaluate(table)[0]) + str(self.children[1].Evaluate(table)[0])
            return (result,"str")

        else:
             raise Exception("Erro, verifique a exprecao operacao nao permitida")

class UnOp(Node):

    def __init__(self, value, child):
        self.value = value
        self.children = child

    def Evaluate(self,table):
        if self.value == '-':
            result = -self.children[0].Evaluate(table)[0]
            return (result,self.children[0].Evaluate(table)[1])

        if self.value == '!':
            result = not self.children[0].Evaluate(table)[0]
            return (result,self.children[0].Evaluate(table)[1])

        else:
            return self.children[0].Evaluate(table)

class IntVal(Node):
    def __init__(self, value, child):
        self.value = value
        #self.children = child

    def Evaluate(self,table):
        return (self.value,"int")

class BoolVal(Node):
    def __init__(self, value, child):
        self.value = value
        self.children = child

    def Evaluate(self,table):
        if self.value == "true":
            return (1,"bool")
        else:
            return (0,"bool")

class StringVal(Node):
    def __init__(self, value, child):
        self.value = value

    def Evaluate(self,table):
        return (self.value,"str")

class NoOp(Node):
    def __init__(self, value, child):
        self.value = value

    def Evaluate(self,table):
        pass

class SymbolTable():
    def __init__(self):
        self.id_dict = {}
        self.func_dict = {}
   
    ret_dict = {}

    def getter(self, iden):
        if iden in self.id_dict:
            return self.id_dict[iden]
        else:
            print(iden)
            raise Exception("Erro, verifique a exprecao identificador nao declarado")

    def setter(self, iden, value):
        self.id_dict[iden] = value

    def func_getter(self,iden):
        if iden in self.func_dict:
            return self.func_dict[iden]
        elif iden != 'return':
            print(iden)
            raise Exception("Erro, verifique a exprecao funcao nao declarada")

    def func_setter(self,iden, value):
        if iden not in self.func_dict or iden !="func":
            self.func_dict[iden] = value

    @staticmethod
    def ret_getter( iden):
        if iden in SymbolTable.ret_dict:
            return SymbolTable.ret_dict[iden]
        elif iden != 'return':
            print(iden)
            raise Exception("Erro, verifique a exprecao funcao nao declarada")

    @staticmethod
    def ret_setter(iden, value):
        if iden not in SymbolTable.ret_dict or iden !="func":
            SymbolTable.ret_dict[iden] = value

class FuncDec(Node):
    def __init__(self, value, child):
        self.value = value
        self.children = child

    def Evaluate(self,table):
        table.func_setter(self.value,self.children)

class FuncCall(Node):
    def __init__(self, value, child):
        self.value = value
        self.children = child
    
    def Evaluate(self, table):

        nodes = table.func_getter(self.value)
    
        func_table = SymbolTable()

        for var in range(len(nodes[0])):
            func_table.setter(nodes[0][var],self.children[var].Evaluate(table))

        for node in nodes[1]:

            node.Evaluate(func_table) ##

        try:
            return func_table.ret_getter("return")
        except:
            pass

class ReturnOp(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,table):

        return table.ret_setter("return",self.value.Evaluate(table))

class AssignOp(Node):
    def __init__(self, value, child):
        self.value = value
        self.children = child

    def Evaluate(self,table):
        table.setter(self.value,self.children.Evaluate(table))

class IdenVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,table):
        result = table.getter(self.value)
        return result

class CommandOp(Node):
    def __init__(self,child):
        self.children = child
    
    def Evaluate(self,table):
        for child in self.children:
            child.Evaluate(table)

class EchoOp(Node):
    def __init__(self,child):
        self.children = child
        
    def Evaluate(self,table):
        print(self.children.Evaluate(table)[0])

class WhileOp(Node):
    def __init__(self,child):
        self.children = child

    def Evaluate(self,table):
        while self.children[0].Evaluate(table)[0]:
            self.children[1].Evaluate(table)

class IfOp(Node):
    def __init__(self, child):
        self.children = child

    def Evaluate(self,table):
        if self.children[0].Evaluate(table)[0]:
            return self.children[1].Evaluate(table)

        else:

            if len(self.children) == 3:
                return self.children[2].Evaluate(table)

            else:
                pass

class ReadlineOP(Node):
    def __init__(self):
        pass

    def Evaluate(self, table):
        inp = input()
        return (int(inp),"int")

class Parser():

    def __init__(self,tokens):
        self.tokens = tokens

    @staticmethod
    def parseProgram():
       
            r = Parser.parseCommand()
            return r

    @staticmethod
    def parseCommand():
        if Parser.tokens.actual.tokenValue!="{" :

            if Parser.tokens.actual.tokenType== "iden":
                var = Parser.tokens.actual.tokenValue
                Parser.tokens.selectNext()

                if Parser.tokens.actual.tokenValue== "=":
                    Parser.tokens.selectNext()
                    
                    result = AssignOp(var,Parser.parseRelExpression(Parser.tokens))

                else:
                    print(Parser.tokens.actual.tokenValue)
                    raise Exception("Erro, verifique a exprecao =") 

            elif Parser.tokens.actual.tokenValue== "printf":
                Parser.tokens.selectNext()
                result = EchoOp(Parser.parseRelExpression(Parser.tokens))
                if Parser.tokens.actual.tokenValue== "}":
                    print(Parser.tokens.actual.tokenValue)
                    raise Exception("Erro, verifique a exprecao: funcao mal declarada")  

                return result

            elif Parser.tokens.actual.tokenValue == "if":
                Parser.tokens.selectNext()
                children = []
                if Parser.tokens.actual.tokenValue == "(":

                    while Parser.tokens.actual.tokenValue != ")":
                        Parser.tokens.selectNext()
                        node = Parser.parseRelExpression(Parser.tokens)
                        children.append(node)

                    if Parser.tokens.actual.tokenValue == ")":
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.tokenValue=="{":
                            children.append(Parser.parseBlock())
                          
                            Parser.tokens.selectNext()
                            if Parser.tokens.actual.tokenValue == "else":
                                Parser.tokens.selectNext()
                                
                                if Parser.tokens.actual.tokenValue == "{":
                                    children.append(Parser.parseBlock())

                                elif Parser.tokens.actual.tokenValue == "if":
                                    children.append(Parser.parseCommand())
                                
                            return IfOp(children)
                else:
                    raise Exception("Erro, verifique a exprecao: nao abriu (")        

            elif Parser.tokens.actual.tokenValue == "while":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.tokenValue == "(":

                    while Parser.tokens.actual.tokenValue != ")":
                        Parser.tokens.selectNext()
                        node = Parser.parseRelExpression(Parser.tokens)

                    if Parser.tokens.actual.tokenValue == ")":
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.tokenValue=="{":
                            result = WhileOp([node,Parser.parseBlock()])

                return result

            elif Parser.tokens.actual.tokenType == "function_d":

                func_name = Parser.tokens.actual.tokenValue
                Parser.tokens.selectNext()

                if  Parser.tokens.actual.tokenValue == "(":
                    arg_list = []
                    children = []

                    Parser.tokens.selectNext()

                    while Parser.tokens.actual.tokenValue != ")":

                        if Parser.tokens.actual.tokenType== "iden" or  Parser.tokens.actual.tokenType == "comma":
                            if Parser.tokens.actual.tokenType== "iden":
                                arg_list.append(Parser.tokens.actual.tokenValue)
                            Parser.tokens.selectNext()

                        else:
                            raise Exception("Erro, verifique a exprecao: funcao mal declarada")    

                    Parser.tokens.selectNext()

                    if Parser.tokens.actual.tokenValue=="{":
                        children.append(Parser.parseCommand())

                        return FuncDec(func_name, (arg_list,children))

                    else:
                        raise Exception("Erro, verifique a exprecao: funcao mal declarada")    

                else:
                    raise Exception("Erro, verifique a exprecao: funcao mal declarada")    

            elif Parser.tokens.actual.tokenType == "function_c":
                func_name = Parser.tokens.actual.tokenValue
                Parser.tokens.selectNext()

                if  Parser.tokens.actual.tokenValue == "(":
                    arg_list = []
                    Parser.tokens.selectNext()
                   
                    while Parser.tokens.actual.tokenValue != ")":

                        arg_list.append(Parser.parseRelExpression(Parser.tokens.actual))
          
                    Parser.tokens.selectNext()

                    return FuncCall(func_name, arg_list)
                
                else:
                    print(Parser.tokens.actual.tokenValue)
                    raise Exception("Erro, verifique a exprecao: funcao mal declarada")    

            elif Parser.tokens.actual.tokenValue == "return":

                Parser.tokens.selectNext()
                result = Parser.parseRelExpression(Parser.tokens)
                
                return ReturnOp(result)

            if Parser.tokens.actual.tokenValue== ";":
                
                return result

            if Parser.tokens.actual.tokenValue== "else":
                raise Exception("Erro, verifique a exprecao: else sem if")        

        if Parser.tokens.actual.tokenValue=="{" :
            return Parser.parseBlock()
    
    @staticmethod
    def parseBlock():
        if Parser.tokens.actual.tokenValue== "{" :
            commands = []

            while Parser.tokens.actual.tokenValue != "}":

                Parser.tokens.selectNext()
                c = Parser.parseCommand()

                if c != None:
                    commands.append(c)
                    
            if Parser.tokens.actual.tokenValue== "}":
                c = Parser.parseCommand()

                if c != None:
                    commands.append(c)

                C =CommandOp(commands)

                Parser.tokens.selectNext() ##

                return C

            else :
                raise Exception("Erro, verifique a exprecao nao fechou }") 
        else:
            raise Exception("Erro, verifique a exprecao nao abriu {") 

    @staticmethod
    def parseFactor():
        if Parser.tokens.actual.tokenValue == ",":
            Parser.tokens.selectNext()

        if str(Parser.tokens.actual.tokenValue).isdigit():
            result = IntVal(Parser.tokens.actual.tokenValue, [])
            return result

        elif Parser.tokens.actual.tokenValue == "true" or Parser.tokens.actual.tokenValue == "false":
            result = BoolVal(Parser.tokens.actual.tokenValue, [])
            return result

        elif Parser.tokens.actual.tokenType == "iden":
            result = IdenVal(Parser.tokens.actual.tokenValue)
            return result
        
        elif str(Parser.tokens.actual.tokenType)== "str":
            result = StringVal(Parser.tokens.actual.tokenValue, [])
            return result

        elif str(Parser.tokens.actual.tokenValue)== "+":
            Parser.tokens.selectNext()
            child = [Parser.parseFactor()]
            result =  UnOp('+', child)
            return result

        elif str(Parser.tokens.actual.tokenValue)== "-":
            Parser.tokens.selectNext()
            child = [Parser.parseFactor()]
            result =  UnOp('-', child)
            return result

        elif str(Parser.tokens.actual.tokenValue)== "!":
            Parser.tokens.selectNext()
            child = [Parser.parseFactor()]
            result =  UnOp('!', child)
            return result
        
        elif Parser.tokens.actual.tokenValue=="(":
            Parser.tokens.selectNext()
            result = Parser.parseRelExpression(Parser.tokens)

            if Parser.tokens.actual.tokenValue!=")":
                raise Exception("Erro, verifique a exprecao nao fechou )") 
            else:
                return result

        elif Parser.tokens.actual.tokenValue == "scanf":
            Parser.tokens.selectNext()
            if Parser.tokens.actual.tokenValue == "(":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.tokenValue == ")":
                    result = ReadlineOP()

                    return result

        elif  Parser.tokens.actual.tokenType == "function_c":
            func_name = Parser.tokens.actual.tokenValue
            Parser.tokens.selectNext()

            if  Parser.tokens.actual.tokenValue == "(":
                arg_list = []
                Parser.tokens.selectNext()
                
                while Parser.tokens.actual.tokenValue != ")":

                    arg_list.append(Parser.parseRelExpression(Parser.tokens.actual))
        
                return FuncCall(func_name, arg_list)
            
            else:
                raise Exception("Erro, verifique a exprecao: funcao mal declarada")    
    
        else: 
            print((Parser.tokens.actual.tokenValue),(Parser.tokens.actual.tokenType))
            raise Exception("Erro, verifique a exprecao a")        
       
    @staticmethod
    def parseTerm():
        node = Parser.parseFactor()
        Parser.tokens.selectNext()
        
        while Parser.tokens.actual.tokenValue == "*" or Parser.tokens.actual.tokenValue == "/" or Parser.tokens.actual.tokenValue == "and":

            if Parser.tokens.actual.tokenValue =="*":
                Parser.tokens.selectNext()
                child = [node, Parser.parseFactor()]
                node = BinOp('*', child)

            elif Parser.tokens.actual.tokenValue =="/":
                Parser.tokens.selectNext()
                child = [node, Parser.parseFactor()]
                node = BinOp('/', child)

            elif Parser.tokens.actual.tokenValue =="and":
                Parser.tokens.selectNext()
                child = [node, Parser.parseFactor()]
                node = BinOp('and', child)

            Parser.tokens.selectNext()

        return node

    @staticmethod
    def parseExpression():
        node = Parser.parseTerm()
      
        while Parser.tokens.actual.tokenValue == "+" or Parser.tokens.actual.tokenValue == "-" or Parser.tokens.actual.tokenValue == "or"  or Parser.tokens.actual.tokenValue == "." :
            if Parser.tokens.actual.tokenValue =="+":
                Parser.tokens.selectNext()
                child = [node, Parser.parseTerm()]
                node = BinOp('+', child)

            elif Parser.tokens.actual.tokenValue =="-":
                Parser.tokens.selectNext()
                child = [node, Parser.parseTerm()]
                node = BinOp('-', child)

            elif Parser.tokens.actual.tokenValue =="or":
                Parser.tokens.selectNext()
                child = [node, Parser.parseTerm()]
                node = BinOp('or', child)

            elif Parser.tokens.actual.tokenValue ==".":
                Parser.tokens.selectNext()
                child = [node, Parser.parseTerm()]
                node = BinOp('.', child)

        return node

    @staticmethod
    def parseRelExpression(tokens):
        node = Parser.parseExpression()
      
        while Parser.tokens.actual.tokenValue == ">" or Parser.tokens.actual.tokenValue == "<" or Parser.tokens.actual.tokenValue == "==":
            if Parser.tokens.actual.tokenValue ==">":
                Parser.tokens.selectNext()
                child = [node, Parser.parseExpression()]
                node = BinOp('>', child)

            elif Parser.tokens.actual.tokenValue =="<":
                Parser.tokens.selectNext()
                child = [node, Parser.parseExpression()]
                node = BinOp('<', child)

            elif Parser.tokens.actual.tokenValue =="==":
                Parser.tokens.selectNext()
                child = [node, Parser.parseExpression()]
                node = BinOp('==', child)
        
        return node
    
    @staticmethod
    def run(code):
        code = PrePro.filter(code)
        Parser.tokens = Tokenizer(code)
        table = SymbolTable()
        parsed = Parser.parseProgram()
        return parsed.Evaluate(table)

def main():

    try:
        fileobj = open(sys.argv[1], 'r')
    except IndexError:
        fileobj = open("./test.cmpl",'r')

    with fileobj:
        data = fileobj.read()

    try:
        Parser.run(data)
            
    except :
        raise Exception("Erro, verifique a exprecao")        

if __name__ == '__main__':
    main()