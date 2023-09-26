from flask import Flask

app = Flask (__name__)

@app.route("/students")
def students():
    return {"students":["Maria", "Kelly", "John", "Kevin"]}


if __name__ == "__main__":
    app.run(debug=True)