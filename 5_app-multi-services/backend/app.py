from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Bienvenue sur Flask via Nginx</h1><p>Contenu généré par Flask et servi par Nginx.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')