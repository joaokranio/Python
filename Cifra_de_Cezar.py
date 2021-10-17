'''
    cifra de cezar
'''
#alfabeto original
alf = {'0':' ','1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'x','24':'w','25':'y','26':'z'}
#alfabeto cifrado com 3 casas
cif = {'0':' ','1':'y','2':'z','3':'a','4':'b','5':'c','6':'d','7':'e','8':'f','9':'g','10':'h','11':'i','12':'j','13':'k','14':'l','15':'m','16':'n','17':'o','18':'p','19':'q','20':'r','21':'s','22':'t','23':'u','24':'v','25':'x','26':'w'}
a = list(input('Digite uma palavra: '))
#print(a) #usado para testar
#chave: recebe a key do alf
chave = []
#cripto: recebe mensagem cifrada com os espaços
cripto = []
#sep: usado para tirar espaços
sep = ''
#varre a entrada de "a" e encontra suas Keys para jogar n lista chave
for i in list(a):
    for k,v in alf.items():
        if v ==i:
            #print('chave: ',i,'key: ',k) #usado para testar
            chave.append(k)
#print(chave) #usado para testar
#pega o valor da key da lista chave e procura o correspondente na lista cif
for i in list(chave):
    for k,v in cif.items():
        if k == i:
            cripto.append(v)
print (sep.join(cripto))
