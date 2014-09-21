from flask import Flask, request, render_template

app = Flask("wtf")

@app.route("/")
def home():
	title = "Home page"
	return render_template("index.html", title=title), 200

@app.route('/about')
def about():
	return render_template("about.html", title="About us"), 200

@app.route('/search')
def search(question=None):
	if request.args.get('question') != None:
		q = request.args.get('question')
	return render_template("search.html", title="Search page", question = q), 200

@app.route('/contacts')
def contacts():
	if request.method == "POST":
		dados = request.form.to_dict()

	return render_template('contacts.html', title="Contacts"), 200


app.run(debug=True, use_reloader=True)

