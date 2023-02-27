from flask import Flask, request, jsonify,render_template
import openai
import os

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ["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"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prompt", methods=["POST"])
def generate_response():
    # Get prompt from request body
    prompt = request.json["prompt"]

    # Set up OpenAI parameters
    model_engine = "text-davinci-002"
    temperature = 0.7
    max_tokens = 1024
    top_p = 1
    frequency_penalty = 0
    presence_penalty = 0

    # Generate response using OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    # Return response as JSON
    return jsonify(response.choices[0].text.strip())
