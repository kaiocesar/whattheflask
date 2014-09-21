#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request, url_for, render_template

from db import noticias

app = Flask('wtf')

@app.route("/noticias/cadastro", methods=["GET","POST"])
def cadastro():
	flash = False
	if request.method == "POST":
		dados_do_formulario = request.form.to_dict()
		nova_noticia = noticias.insert(dados_do_formulario)
		flash = True
		return render_template("news/add.html", flash=flash)

@app.route("/")
def index():
	noticias_template = u"""
		<a href="/noticia/{noticia[id]}">{noticia[title]}</a>
	"""
	todas_noticias = [
		noticias_template.format(noticia=noticia)
		for noticia in noticias.all()
	]

	return render_template("news/index.html", title="All news", noticias=todas_noticias)



if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)