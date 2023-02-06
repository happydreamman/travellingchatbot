import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            max_tokens=200,
            temperature=0.1,
        )
        print("response: ",response, "\n")
        return redirect(url_for("index", result=animal + response.choices[0].text))

    result = request.args.get("result")
    # result ="a\nb\nc"
    print("result: ", result)
    r0=r1=r2=r3=""   
    if result and len(result.split("\n"))>=4:
        r0 = result.split("\n")[0]
        r1 = result.split("\n")[1]
        r2 = result.split("\n")[2]
        r3 = result.split("\n")[3]
    return render_template("index.html", result=result, r0=r0,r1=r1,r2=r2,r3=r3)


def generate_prompt(animal):
    return """Suggest the best 3 airline paths to travel to Dubai from my location? And how long will it take? 

Location: {}
Path:""".format(
        animal.strip()
    )
