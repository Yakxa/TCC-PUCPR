# -*- coding: UTF-8 -*-

#
# Source : https://github.com/willf/dmap-python
#
import ast
# instancias de conceitos(?)
class Frame(object):
    pass

# checa pra ver se e uma classe mesmo
def is_class(x):
    return isinstance(x, type)

# realmente e uma instancia?    
def is_instance(x):
    if isinstance(x, type):
        return 0
    else:
        return 1
    
# a classe e uma subclasse de...?
# x.__bases__

# definicao de atributos
# instancia --x.__dict__ tem atributos da instancia + valores
#  classe   --x.__dict__ tem atributos da classe + valores(?)

def attribute_value(obj, attribute):
    for abstraction in all_abstractions(obj):
        val = None
        try:
            val = abstraction.__dict__.get(attribute, None)
        except AttributeError:
            pass
        if val is not None:
            return val
    return None




# tenta pegar o nome da classe x.__name__
def name(x):
    name = x
    try:
        name = x.__name__
    finally:
        return name
    

def set_name(x, name):
    if is_instance(x):
        x.__name__ = name
        
# checa se "e um"
def isa(child, parent):
    if (child == parent):
        return 1
    elif is_class(parent) and isinstance(child, parent):
        return 1
    elif is_class(child) and is_class(parent) and issubclass(child, parent):
        return 1
    else:
        return 0
    
# pais do objeto
def parents(x):
    if is_class(x):
        return list(x.__bases__)
    else:
        return [x.__class__]
    
def allparents(x):
    if is_class(x):
        return list(x.__mro__)
    else:
        return list(type(x).__mro__)
    

# Descricao = classe
def all_abstractions(x):
    if isinstance(x, Description):
        return all_abstractions(x.base)
    elif is_class(x):
        return list(x.__mro__)
    else:
        return [x] + list(type(x).__mro__)

# subclasses da propria classe pai

def subclasses_of(parent):
    return filter(
        lambda x: is_class(x) and x != parent and issubclass(x, parent),
        globals().itervalues()
    )

# instancias da classe pai

def instances_of(parent):
    return filter(
        lambda x: isinstance(x, parent), globals().itervalues()
    )

def is_attribute_specifier(x):
    return type(x) == tuple

def attribute_specifier(x):
    return x[0]

def make_attribute_specifier(x):
    return(x, )

class Feature(object):
    """
    Feature:
    Atributos:
    
    attribute:     --
    value:     --
    """
    def __init__(self, attribute=None, value=None):
        self.__attribute = attribute
        self.__value = value
        # caso a Description n tenha features continua
        if isinstance(value, Description) and value.features == []:
            self.__value = value.base
    
    # accessors do Feature (setters e getters)
    def get_attribute(self):
        return self.__attribute
    
    def set_attribute(self, attribute):
        self.__attribute = attribute

    attribute = property(set_attribute, get_attribute)    

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value

    value = property(set_value, get_value)
    
    def __repr__(self):
        return '<Feature: ' + repr(self.attribute) + ':' + repr(self.value) + '>'


class Description(object):
    """
    Descrption:
    Atributos:
    
    base:   --
    features:   --
    
    """
    
    def __init__(self, base=None, features=list()):
        self.__base = base
        self.__features = list(features)
    
    #  accessors para Description (setters e getters)
    def get_base(self):
        return self.__base
    
    def set_base(self, base):
        self.__base = base
        
    base = property(get_base, set_base)
    
    def get_features(self):
        return self.__features
    
    def set_features(self, features):
        self.__features
        
    features = property(get_features, set_features)
    
    def all_abstractions(self):
        return all_abstractions(self.base)
    
    def __repr__(self):
        return '<Description: ' + repr(self.base) + ' ' + repr(self.features) + '>'
    
class Prediction(object):
    """
    Prediction:
    Atributos:
    
    base:     --
    pattern:     --
    start:     --
    next:     --
    description:     --
    """
    
    def __init__(self, base=None, pattern=None, start=None, next=None, features=list()):
        self.__base = base
        self.__pattern = pattern
        self.__start = start
        self.__next = next
        self.__features = list(features)
    
    # accessors pra Prediction (setters e getters)
    def get_base(self):
        return self.__base
    
    def set_base(self, base):
        self.__base = base
    
    base = property(get_base, set_base)
    
    def get_pattern(self):
        return self.__pattern
    
    def set_pattern(self, pattern):
        self.__pattern = pattern
    
    pattern = property(get_pattern, set_pattern)
    
    def get_start(self):
        return self.__start
    
    def set_start(self, start):
        self.__start = start

    start = property(get_start, set_start)

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    next = property(get_next, set_next)

    def get_features(self):
        return self.__features

    def set_features(self, features):
        self.__features = features

    features = property(get_features, set_features)
    
    # "conceito alvo"
    def target(self):
        spec = self.pattern[0]
        if is_attribute_specifier(spec):
            base = self.base
            attribute = attribute_specifier(spec)
            value = attribute_value(base, attribute)
            if (attribute is None):
                Exception("Not an attribute")
            else:
                return value
        else:
            return spec

class DMAP(object):
    """
    DMAP:

    Atributos:
    anytime_predictions:     --
    dynamic_predictions:     --
    position:     --
    call_backs:     --
    seen:     --
    complete:     --
    """
    
    def __init__(self):
        self.__anytime_predictions = {}
        self.__dynamic_predictions = {}
        self.__position = 0
        self.__call_backs = {}
        self.__seen = list()
        self.__complete = list()
        
    # accessors DMAP (setters e getters)
    def get_anytime_predictions(self):
        return self.__anytime_predictions

    def set_anytime_predictions(self, anytime_predictions):
        self.__anytime_predictions = anytime_predictions

    anytime_predictions = property(get_anytime_predictions,
                                   set_anytime_predictions)

    def get_dynamic_predictions(self):
        return self.__dynamic_predictions

    def set_dynamic_predictions(self, dynamic_predictions):
        self.__dynamic_predictions = dynamic_predictions

    dynamic_predictions = property(get_dynamic_predictions,
                                   set_dynamic_predictions)

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    position = property(get_position, set_position)

    def get_call_backs(self):
        return self.__call_backs

    def set_call_backs(self, call_backs):
        self.__call_backs = call_backs

    call_backs = property(get_call_backs, set_call_backs)
    
    def add_call_back(self, klass, procedure):
        callbacks = self.call_backs.get(klass, [])
        if procedure in callbacks:
            callbacks.remove(procedure)
        self.call_backs[klass] = callbacks + [procedure]
    
    def get_seen(self):
        return self.__seen

    def set_seen(self, seen):
        self.__seen = seen

    seen = property(get_seen, set_seen)

    def get_complete(self):
        return self.__complete

    def set_complete(self, complete):
        self.__complete = complete

    complete = property(get_complete, set_complete)
    
    def parse(self, sentence):
        for word in sentence:
            self.position = self.position + 1
            self.reference(word, self.position, self.position)
            
    def reference(self, item, start, end):
        for abstraction in all_abstractions(item):
            for prediction in self.anytime_predictions.get(abstraction, list()):
                self.advance(prediction, item, start, end)
            for prediction in self.dynamic_predictions.get(abstraction, list()):
                self.advance(prediction, item, start, end)
            for callback in self.call_backs.get(abstraction, list()):
                callback(item, start, end)
            
    def advance(self, prediction, item, start, end):
        if (prediction.next is None) or (prediction.next == start):
            # inicializar os valores do prediction
            base = prediction.base
            pattern = prediction.pattern[1:]
            start = start
            if (prediction.start is not None):
                start = prediction.start
            features = self.extend(prediction, item)
            # referencia se nao cria uma nova referencia
            if(pattern == []):
                self.reference(self.find(base, features), start, end)
            else:
                self.index_dynamic(Prediction(base, pattern, start, (self.position + 1), features))
                
                
                
    def find(self, base, features):
        return Description(base, features)
    
    def extend(self, prediction, item):
        specialization = prediction.pattern[0]
        if is_attribute_specifier(specialization):
            itemIs = item
            if isinstance(itemIs, Description):
                itemIs = itemIs.base
            if isa(prediction.target(), itemIs):
                return features
            else:
                fea = Feature(attribute_specifier(specialization), item)
                prediction.features.append(fea)
                return prediction.features
        else:
            return prediction.features
    
    def associate(self, base, pattern):
        if base == pattern[0]:
            pass
        else:
            prediction = Prediction(base=base, pattern=pattern)
            self.index_anytime(prediction)
            
    def index_anytime(self, prediction):
        target = prediction.target()
        predictions = self.anytime_predictions.get(target, list())
        predictions.append(prediction)
        self.anytime_predictions[target] = predictions
        
    def index_dynamic(self, prediction):
        target = prediction.target()
        predictions = self.dynamic_predictions.get(target, list())
        predictions.append(prediction)
        self.dynamic_predictions[target] = predictions

#Cria novas instancias a princípio genéricas
class AddInstances(object):     
    
    def __init__(self):
        pass
    
    def get_instance(self, name):
        return self.name 
      
    def new_instance(self, name):
        self.name = name
        return name
    

        
if __name__ == '__main__':
    # Human eh um Frame, que eh um conceito(?)
    class Human(Frame):
        pass
    
    class FHuman(Human):
        pass
    
    class MHuman(Human):
        pass
              
    class Action(Frame):
        pass
    
    class Thing(Frame):
        pass
    
    class King(Thing):
        pass
    
    class Casa(Thing):
        pass
    
    class Alice(FHuman):
        pass

    class Bob(MHuman):
        pass
    
    class Maca(Thing):
        pass
    
    class Previdencia(Thing):
        pass
    
    class Reforma(Thing):
        pass
    
    class Aposentadoria(Thing):
        pass
    
    class Funcionario(Thing):
        pass
            
    class Contribuicao(Thing):
        pass
    
    class Diferenca(Thing):
        pass
    
    class Renda(Thing):
        pass
    
    class Trabalhador(Thing):
        pass
    
    class Governo(Thing):
        pass
    
    class Contribuir(Action):
        actor = Human
        object = Thing    
    
    class Is(Thing):
        actor = Human
        object = Thing
    
    class Loves(Action):
        actor = Human
        object = Human
    
    class Believes(Action):
        actor = Human
        object = Human
           
    class Conhece(Action):
        actor = Human
        object = Human    
    
    class Tem(Action):
        object = Thing
        actor = Human
    
    class Comer(Action):
        actor = Human
        object = Thing
    
    p = DMAP()
    resultados = []
    def reference_printer(frame, start, end):
        resultados.append( name(frame.base))
        #print("Referencing", name(frame.base))
        #print(resultados)
    
    p.add_call_back(Frame, reference_printer)
    #p.parse(lines)
    
    p.associate(Bob, ["Bob"])
    p.associate(Alice, ["Alice"])
    p.associate(Casa, ["Casa"])
    p.associate(Maca, ["maca"])
    p.associate(Maca, ["Maca"])
    p.associate(Previdencia, ["Previdencia"])
    p.associate(Previdencia, ["previdencia"])
    p.associate(Reforma, ["reforma"])
    p.associate(Reforma, ["Reforma"])
    p.associate(Aposentadoria, ["aposentadoria"])
    p.associate(Funcionario, ["funcionario"])
    p.associate(Funcionario, ["funcionarios"])
    p.associate(Contribuicao, ["Contribuicao"])
    p.associate(Contribuicao, ["contribuicao"])
    p.associate(Diferenca, ["Diferenca"])
    p.associate(Diferenca, ["diferenca"])
    p.associate(Contribuicao, ["Contribuicoes"])
    p.associate(Contribuicao, ["contribuicoes"])
    p.associate(Renda, ["renda"])
    p.associate(Trabalhador, ["trabalhador"])
    p.associate(Trabalhador, ["trabalhadores"])
    p.associate(Governo, ["Governo"])
    p.associate(Governo, ["governo"])
    
    p.associate(Conhece, [("actor", ), "conhece", ("object", )])
    p.associate(Tem,[("object", ), 'que', ("actor", ), 'tem', ])
    p.associate(Comer, [("actor", ), "come", ("object", ) ] )
    p.associate(Contribuir, [("actor", ), "contribui", ("object",)] )
    p.associate(Contribuir, [("actor", ), "contribuir", ("object",)] )
    p.associate(Contribuir, [("actor", ), "contribuiu", ("object",)] )
    p.associate(Contribuir, [("actor", ), "contribuira", ("object",)] )
    #p.associate(Believes, [("actor", ), 'believes', 'that', ("object", )])
        
    #p.parse('Bob conhece Alice'.split(' '))
    #p.parse('Casa que Alice tem'.split(' '))
    #p.parse('Alice come maca'.split(' '))
    p.parse('O que o texto nos mostra e que a ma distribuicao de renda no pais beneficia alguns e prejudica outros. Pretende-se com a reforma da previdencia fazer com que os funcionarios publicos e privados recebam, quando se aposentarem, o proporcional ao valor que o mesmo contribuiu durante a sua vida profissional. Diferente do que acontece hoje em dia, o funcionario privado contribui mais que recebe quando se aposenta, o que acaba gerando uma maior aposentadoria para os funcionarios publicos. Estes, alem, de receberem essa diferenca de contribuicao, se beneficiam pelos impostos que pagamos. O que precisa ser feito e uma reforma justa, onde funcionarios publicos e privados recebam justamente o valor que pagaram ao governo durante o periodo de sua contribuicao e que os impostos pagos pelos brasileiros sejam utilizados para outros setores, como educacao e saude, que acabaram sendo deixados de lado durante essa reforma da previdencia. Infelizmente as noticias sobre a previdencia dos trabalhadores nao sao muito satisfatorias, nao pelos rumos que a mesma podera seguir, mas por estar tao desorganizada que qualquer mudanca, por melhor que seja, acabara prejudicando alguem, em maioria o trabalhador assalariado, pois e este que sempre sofre as consequencias, as pessoas que possuem uma liquidez baixa, ja se acostumaram a viver com o minimo do minimo e estas mudancas acabam por nao afetar seu dia a dia, as pessoas com poder aquisitivo maior sempre apresentam outra oportunidade e tambem nao sao tao afetados. Agora aquele trabalhador que sempre paga seus impostos, suas contas em dia, seu aluguel, e coloca a gasolina no seu automovel usado, sao os que mais sofrem, nao so estas consequencias da reforma da previdencia, mas todas as mudancas do pais e do mundo, pois a globalizacao os atinge tambem. O que diferencia o povo brasileiro dos outros e o otimismo e o jeitinho brasileiro, que muitos criticam, mas e este que ja salvou muitas pessoas das situacoes desfavoraveis. O brasileiro e um povo esperancoso e alegre, mas o pais apresenta uma situacao que sempre acabara prejudicando a classe media-baixa, media-media e media-alta, que sao os que sustetam este pais.Como as aposentadorias dos funcionarios publicos sao maiores que as aposentadorias dos trabalhadores privados, fez-se necessaria uma Reforma da Previdencia, pois o Estado estava arrecadando menos e pagando mais, e assim o rombo ia aumentando cada vez mais. Para que um sistema de Previdencia seja equilibrado, seria necessario que se pagasse aos aposentados o mesmo valor que arrecadou deles quando trabalhavam. Uma pesquisa mostrou que funcionarios publicos pagam menos do que recebem, enquanto que os funcionarios privados pagam mais do que recebem, pois a diferenca e utilizada para cobrir as aposentadorias dos informais, que nao contribuem. Para descobrir se a Reforma realmente dara resultado positivo, foi realizada uma simulacao, aplicando regras contidas na Reforma Lula para todos os atuais trabalhadores, e o resultado foi satisfatorio, pois a aposentadoria paga ao funcionario publico ficou mais proxima ao montante distribuido. Portanto, a Reforma do governo nao tera impacto para funcionarios privados, pois estes ja estao tendo uma aposentaria dentro do que contribuem, mas sim para os que recebem muito mais do que contribuem, e assim reduziremos as diferencas de tratamento entre as duas categorias de trabalhadores.'.split(' '))
    
    sem_repeticoes = []
    sem_repeticoes = [i for n, i in enumerate(resultados) if i not in resultados[:n]]
    print(str(sem_repeticoes) + "\n")
    
    with open("C:\\Users\\Megaware\\Desktop\\OrganiZen\\Tudo-em-um 01\\09\\2020\\TCC\\ocurrences.txt", "w") as file:
        for y in sem_repeticoes:
            file.write("%s\n" % y)    
    file.close()

    