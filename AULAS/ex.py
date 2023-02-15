###############################################################################
#n1 = int (input ('Digite um valor: '))                                       #
#n2 = int (input ('Digite um valor: '))                                       #
#s= n1+n2                                                                     # 
#print ('A soma entre', n1, 'e' , n2 ,'vale {}'.format (s))                   #
#print( 'A soma entre {} e {} vale {}'.format(n1, n2, s))                     #
###############################################################################


#n = (input('Digite qualquer coisa: '))
#print(type (n))
#print ('tem espaços: ',n.isspace())
#print ('é um numero: ', n.isnumeric())
##print('é alfabetico: ',n.isalpha())
#print('é alfanumerico: ', n.isalnum())
#print('esta´em maiúsculas: ', n.isupper())
#print('esta em minuscula: ', n.islower())
#print('está capitalizada: ', n.istitle())
###############################################################################
# ORDEM DE PRECEDÊNCIA#
#1 ()
#2 **
#3 *,/,//,%
#4 +,-
###############################################################################
#EXEMPLOS
#5+3*2 == 11
#3*5+4**2 == 31
#3*(5+4)**2 == 243
###############################################################################

n1= int (input('Digite um numero: '))
n2= int (input('Digite Outro Valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e Potência {}'.format(di, e))

