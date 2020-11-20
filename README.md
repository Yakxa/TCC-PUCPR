# TCC-PUCPR
TCC PUCPR

------------------------------DMAP------------------------------

Se você deseja adicionar novas classes no DMAP, caso seja um ator, ou objeto, basta adicionar da seguinte forma:

class Exemplo(FHuman):
	pass

Após isso, associe com uma string:

p.associate(Exemplo, ["Exemplo"])

Se você deseja adicionar uma classe que é uma ação, como um verbo, primeiro crie a classe:

class Exemplo(Action):
	actor = Human
	object = Thing

Para associar, associe todos os tempos verbais possíveis, sem acentos:

p.associate(Contribuir, [("actor", ), "contribui", ("object",)] )
p.associate(Contribuir, [("actor", ), "contribuir", ("object",)] )
p.associate(Contribuir, [("actor", ), "contribuiu", ("object",)] )
p.associate(Contribuir, [("actor", ), "contribuira", ("object",)] )

Redefina o caminho que você deseja exportar a Rubrica no final do arquivo.

----------------------------------------------------------------


-----------------------Método de Avaliação----------------------

Modifique no próprio txt, ao final dele com @seq, caso você queira que ele considere ordenação no método de avaliação (coloque a ordem que desejar):

Palavra1
Palavra2
Palavra3
Palavra4
@seq
Palavra1
Palavra2
Palavra3

Novamente, altere o caminho para extrair tanto a Rubrica quanto o texto para avaliação.
A base de dados possui atualmente 5 textos separados, mas você pode extrair dos arquivos txts originais, que contêm todos os textos.

Ao Atribuir os pesos, cada atribuição impactará o quanto cada peso removerá da nota final. 
Exemplo: caso o pesoUm seja de 2.0 e o texto a ser avaliado receber nota 6.0, mas falhar na ordenação do pesoUm, receberá nota 4.0.

----------------------------------------------------------------
