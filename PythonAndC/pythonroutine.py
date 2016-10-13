import os

frequency_input = 50

print "Programa para chamada da Rotina em C para escrita de dados na porta serial."
print "\n"

print "Chamando a rotina em C com o valor da frequencia..."
print "\n"

os.system("./croutine " + str(frequency_input))

print "Fim da chamada.\n"