from flask import Flask, render_template, request 
import json

app = Flask(__name__)


f_db = open("dicionario_medico.json", "r")
db = json.load(f_db)

@app.get("/")
def home_page():
    return render_template("home.html")

@app.get("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos = db.keys())

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao = designacao, descricao=descricao)
    else:
        return render_template("erro.html", erro ="O conceito introduzido não existe" )

@app.get("/api/conceitos")
def conceitos_api():
    return db


@app.route("/pesquisar")
def pesquisar():
    query = request.args.get("query", "")
    case_sensitive = request.args.get("case_sensitive") == "on"
    word_boundary = request.args.get("word_boundary") == "on"
    
    resultados = []

    if query:
        for designacao, descricao in db.items():
            
            target_desig = designacao if case_sensitive else designacao.lower()
            target_desc = descricao if case_sensitive else descricao.lower()
            search_query = query if case_sensitive else query.lower()

            encontrou = False

            if word_boundary:
                
                palavras = (target_desig + " " + target_desc).replace(',', ' ').replace('.', ' ').split()
                if search_query in palavras:
                    encontrou = True
            else:
                
                if search_query in target_desig or search_query in target_desc:
                    encontrou = True

            if encontrou:
                
                desig_bold = designacao.replace(query, f"<b>{query}</b>")
                desc_bold = descricao.replace(query, f"<b>{query}</b>")

                resultados.append({
                    "designacao": designacao,
                    "desig_label": desig_bold,
                    "descricao": desc_bold
                })

    return render_template("pesquisar.html", resultados=resultados, query=query, 
                           case_sensitive=case_sensitive, word_boundary=word_boundary)

if __name__ == "__main__":
    app.run(host="localhost", port=4002, debug=True)