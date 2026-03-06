# Explicação do conteúdo: Tipos Primitivos e Saída de Dados,
# utilizando um exemplo de soma entre dois números.

# Tipos primitivos:
# A função input() recebe dados digitados pelo usuário.
# O texto dentro das aspas é uma mensagem do tipo string
# que aparece para o usuário na tela.

# Tudo que o usuário digita precisa ser armazenado em algum lugar,
# por isso criamos variáveis.

# A variável valor1 recebe (=) o número digitado pelo usuário.
# Usamos o tipo primitivo int() para converter o valor digitado
# (que vem como string) em número inteiro.

valor1 = int(input("Digite o primeiro valor:\n"))

# A variável valor2 também recebe um número digitado pelo usuário,
# que é convertido para inteiro usando int().

valor2 = int(input("Digite o segundo valor:\n"))

# Criamos uma variável chamada "s" para armazenar o resultado da soma.
# Ela recebe (=) a soma das duas variáveis: valor1 + valor2.

s = valor1 + valor2

# A função print() mostra o resultado na tela.
# Usamos {} e .format(s) para inserir o valor da variável dentro da mensagem.

# print('O Resultado desta soma foi: {}'.format(s))


# type
# outros tipos primitivos

# int = valores inteiros
# Ex: 7 -4 0 5459

# float = valores com números decimais (ponto flutuante)
# Ex: 4.5 0.076 7.5

# bool = valores booleanos (lógicos)
# Ex: True ou False

# str = string (texto)
# Ex: "palavras"
# Todas as strings devem estar entre aspas simples (' ')
# ou aspas duplas (" ")

# Juntar string com string se chama concatenação


# Funções que começam com "is"
# Elas servem para verificar características de uma string.
# O resultado sempre será booleano: True ou False.

# isnumeric() verifica se o valor digitado possui apenas números
# Exemplo: "10" -> True | "10a" -> False

# isalpha() verifica se o valor digitado possui apenas letras
# Exemplo: "Ana" -> True | "Ana123" -> False

n = input("Digite algo: ")

# Aqui estamos verificando se o que foi digitado contém apenas letras
# O programa irá retornar True (verdadeiro) ou False (falso)

print(n.isalpha())