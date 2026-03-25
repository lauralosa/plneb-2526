import spacy
from spacy.matcher import Matcher

nlp=spacy.load("pt_core_news_lg")
texto = open("TPC6\Harry Potter e A Pedra Filosofal.txt", encoding="utf-8")
texto = texto.read()
doc = nlp(texto)
amigos={}
for sent in doc.sents:
    amigo=[]
    for entity in sent.ents: 
        if entity.label_ == "PER":
            if entity.text not in amigo:
                amigo.append(entity.text)
    if len(amigo)>1:
        for w in amigo:
            for w2 in amigo:
                if w!=w2:
                    if w not in amigos:
                        amigos[w]={}    
                    if w2 not in amigos[w]:
                        amigos[w][w2]=1
                    else:
                            amigos[w][w2]+=1

print(amigos)