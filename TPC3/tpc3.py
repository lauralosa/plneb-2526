import re

f=open('dicionario_medico.txt','r',encoding='utf8')
texto = f.read()

texto = re.sub(r'\f','',texto)
texto = re.sub(r'\n\n','\n\n@',texto) 
texto = re.sub(r'\n@(?=[A-ZÁÀÂÃÄÉÈÊÍÌÎÓÒÔÕÚÙÛÇ])','\n#',texto) 
texto = re.sub(r'\n\n#','\n', texto)
texto = texto.replace('@', '')

print(texto)

conceitos = re.split(r'\n\n', texto)
print(len(conceitos))



