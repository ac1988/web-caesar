from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method='POST'>
            <label>Rotate by: </label>
            <input type="text" name="rot" value='0' />
            <br/>
            <br/>
            <textarea name="text">{0}</textarea>
            <br/>
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_message = rotate_string(text, rot)
    return form.format(encrypted_message)

app.run()