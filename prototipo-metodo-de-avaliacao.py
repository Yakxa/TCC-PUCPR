# -*- coding: UTF-8 -*-
import re, itertools

def readFile(fileName):
    f = open(fileName,"r")
    palavras = f.read().splitlines()
    f.close()
    return palavras

class Rubrica():
    
    def __init__(self):
        gabarito = []
        nota = 0.0
        notaFinal = 0.0
        textoParaAvaliar = []
        checkedWords = []
        pesoUm = 0.0
        pesoDois = 0.0
        pesoTres = 0.0
        
        
        
    gabarito = readFile("C:\\Users\\Megaware\\Desktop\\OrganiZen\\Tudo-em-um 01\\09\\2020\\TCC\\ocurrences.txt")
    nota = 0.0
    notaFinal = 0.0
    textoParaAvaliar = []
    checkedWords = []
    
    """
    def getText(texto):
        textoAvaliado = text
        return textoAvaliado
    """
    
    def avaliar(self, texto):
        for i in range(len(self.gabarito)):
            if(self.gabarito[i] != "@seq"):
                for j in range(len(texto)):
                    if self.gabarito[i].lower() == texto[j].lower():
                        if self.gabarito[i] not in self.checkedWords:
                            print("Associou o conceito: " + self.gabarito[i])
                            self.nota = self.nota + 1
                            self.checkedWords.append(self.gabarito[i])
            else: break
        return self.nota

    def ponderar(self, checkedWords):
        for i in range(len(self.gabarito)):
            if (self.gabarito[i] == "@seq"):
                for z in range(len(self.checkedWords)):
                    if self.gabarito[i+1].lower() == self.checkedWords[z].lower() and self.gabarito[i+2].lower() == self.checkedWords[z+1].lower() and self.gabarito[i+3].lower() == self.checkedWords[z+2].lower():
                        print("Voce encadeou 3 de 3 conceitos, a mesma sequencia do Gabarito parabens!")
                        break
                    elif self.gabarito[i+1].lower() == self.checkedWords[z].lower() and self.gabarito[i+2].lower() == self.checkedWords[z+1].lower():
                        self.nota = self.nota - self.pesoUm
                        print("Voce encadeou 2 de 3 conceitos")
                        break
                    elif self.gabarito[i+1].lower() == self.checkedWords[z].lower():
                        self.nota = self.nota - self.pesoDois
                        print("Voce encadeou 1 de 3 conceitos")
                        break
                    else:
                        self.nota = self.nota - self.pesoTres
                        print("Reveja a ordem do seu resumo")
                        break

    def resultadoFinal(self, nota):
        self.ponderar(self.checkedWords)
        self.gabarito.pop()
        self.gabarito.pop()
        self.gabarito.pop()
        #print(self.ponderacao)
        self.notaFinal = self.nota
        return self.notaFinal
    
    def atribuirPesos(self):
        self.pesoUm = input("Digite o valor a se atribuir ao primeiro conceito da sequencia: ")
        self.pesoDois = input("Digite o valor a se atribuir ao segundo conceito da sequencia: ")
        self.pesoTres = input("Digite o valor a se atribuir ao terceiro conceito da sequencia: ")
        return self.pesoUm, self.pesoDois, self.pesoTres
    
    def getTextForAvaliation(self, path):
        f = open(path,"r")
        
        self.textoParaAvaliar = f.readlines()
        
        self.textoParaAvaliar = [w.replace('á', 'a') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('ã', 'a') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('ç', 'c') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('í', 'i') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace(',', ' ') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('"', ' ') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('ú', 'u') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('ê', 'e') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('é', 'e') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('ó', 'o') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('õ', 'o') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('(', ' ') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace(')', ' ') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('.', ' ') for w in self.textoParaAvaliar]
        self.textoParaAvaliar = [w.replace('-', ' ') for w in self.textoParaAvaliar]
        
        self.textoParaAvaliar = self.textoParaAvaliar[0].split()
        
        return self.textoParaAvaliar
        f.close()
        
        
    
    
r = Rubrica()

teste = r.getTextForAvaliation("C:\\Users\\Megaware\\Desktop\\OrganiZen\\Tudo-em-um 01\\09\\2020\\TCC\\textoReformaPrevidencia1.txt")
r.atribuirPesos()
r.avaliar(r.textoParaAvaliar)
r.resultadoFinal(r.nota)
print("Nota final: " + str(r.notaFinal))