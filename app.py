from flask import Flask, render_template, request
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        function = request.form["function"]
        user_input = request.form["user_input"]

        if function == "question":
            prompt = f"Answer this factual question clearly: {user_input}"
        elif function == "summary":
            prompt = f"Summarize the following: {user_input}"
        elif function == "creative":
            prompt = f"Write a creative piece based on: {user_input}"
        else:
            prompt = user_input

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message["content"]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
