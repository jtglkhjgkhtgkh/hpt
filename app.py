import openai
from flask import Flask, request, jsonify, render_template

# Установите значение переменной OPENAI_API_KEY в свой ключ API OpenAI
openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Получаем текст из POST-запроса
    text = request.form["text"]

    # Вызываем GPT-3 для генерации ответа
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Возвращаем ответ в формате JSON
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run()
