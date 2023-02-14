import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        try:
            response = openai.Completion.create(
                model="curie:ft-blockx-2023-02-12-13-06-40",
                prompt=generate_prompt(animal),
                max_tokens=40,
                temperature=0.1,
            )
            print("response: ",response, "\n")
        except openai.error.RateLimitError as e:
            print(e.message)
            result = "The server is currently overloaded with other requests. Sorry about that! You can retry your request, or contact us through our help center at help.openai.com if the error persists."
            return redirect(url_for("index",result="" +result))

        return redirect(url_for("index",result="" + response.choices[0].text))

    result = request.args.get("result")
    # result ="a\nb\nc"
    print("result: ", result)
    # r0=r1=r2=r3=""   
    # if result and len(result.split("\n"))>=4:
    #     r0 = result.split("\n")[0]
    #     r1 = result.split("\n")[1]
    #     r2 = result.split("\n")[2]
    #     r3 = result.split("\n")[3]
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """{}""".format(
        animal.strip()
    )
