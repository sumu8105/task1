from flask import Flask, render_template_string, request

app = Flask(__name__)

# === CONFLICT START ===
# Developer A might write:
# greeting_prefix = "Hello"

# Developer B might write:
# greeting_prefix = "Hi there"
greeting_prefix = "Hey , Hello Welcome "  # This is the line to change during conflict demo
# === CONFLICT END ===

with open("index.html") as f:
    html_template = f.read()

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ""
    if request.method == 'POST':
        name = request.form['name']
    return render_template_string(html_template, name=name, prefix=greeting_prefix)

if __name__ == '__main__':
    app.run(debug=True)
