from flask import Flask, render_template, request
from together import Together
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_input = request.form["prompt"]
        try:
            response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            response_text = response.choices[0].message.content
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
