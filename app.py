from flask import Flask, render_template, request
# создаем объект фласка
app = Flask(__name__)
# наша бд
questions = [{"question": "Vopros", "main_text": "eto tekst", "answer":["1", "2"]}]
# # пишем маршрутизатор
# @app.route("/") # urls в джанго
# def home(): # views в джанго
#     test = "info from back"
#     return render_template("index.html", info=test)
# # создаем динамический маршрутизатор
# @app.route("/user/<int:name>/<string:age>")
# def hello(name,age):
#     return {"name":name, "age": age} # возвращать можно только стринг или словарь
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
@app.route("/add-question", methods=["POST", "GET"])
def add_question():
    if request.method == "POST":
        # получаем информацию из форм
        front_question = request.form.get("question")
        front_main_text = request.form.get("main_text")
        questions.append({"question": front_question, "main_text": front_main_text,
                          "answer":[]})
        return render_template("question.html", question=front_question,
                               main_text= front_main_text)
    # если человек перейдет по ссылке не заполнив форму
    elif request.method == "GET":
        return render_template("index.html")
@app.route("/all_questions")
def all_questions():
    return render_template("all_questions.html", all_questions=questions)

app.run(debug=True)