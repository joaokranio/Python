'''
    função
'''
#######################################
#      Dicionário original            #
#######################################
alf={'0': ' ', '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j',
       '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't',
       '21': 'u', '22': 'v', '23': 'x', '24': 'w', '25': 'y', '26': 'z','27':'1','28':'2','29':'3','30':'4','31':'5',
       '32':'6','33':'7','34':'8','35':'9','36':'0'}
#######################################
#      Dicionário + 3 Posições        #
#######################################
cif ={'0': ' ', '1': 'y', '2': 'z', '3': 'a', '4': 'b', '5': 'c', '6': 'd', '7': 'e', '8': 'f', '9': 'g', '10': 'h',
       '11': 'i', '12': 'j', '13': 'k', '14': 'l', '15': 'm', '16': 'n', '17': 'o', '18': 'p', '19': 'q', '20': 'r',
       '21': 's', '22': 't', '23': 'u', '24': 'v', '25': 'x', '26': 'w','27':'9','28':'0','29':'1','30':'2','31':'3',
       '32':'4','33':'5','34':'6','35':'7','36':'9'}
#######################################
#        Recebendo o input            #
#######################################
a = input(f'Digite seu texto: ').lower()
#######################################
#      seleção cript ou decripto      #
#######################################
perg = input('Selicione a opção desejada: 1: para ciptografar ou 2: para descriptografar: ')
chave = []
chave2 = []
cripto = []
cripto2 = []
sep = ''
########################################
#        fazer a criptografia          #
########################################
def funcao_criptografar():
    for i in list(a):
        for k, v in alf.items():
            if v == i:
                chave.append(k)
    #print(chave)
    for i in list(chave):
        for k, v in cif.items():
            if k == i:
                cripto.append(v)
   # print(chave)
    print(sep.join(cripto).upper())
########################################
#        fazer a decripto.             #
########################################
def funcao_decriptografar():
    for i in list(a):
        for k, v in cif.items():
            if v == i:
                # print('chave: ',i,'key: ',k) #usado para testar
                chave2.append(k)
    #print(chave)  # usado para testar
    for i in list(chave2):
        for k, v in alf.items():
            if k == i:
                cripto2.append(v)
    print(sep.join(cripto2).upper())

if perg =='1':
    funcao_criptografar()
else:
   funcao_decriptografar()
