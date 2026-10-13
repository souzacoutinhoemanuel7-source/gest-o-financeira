from flask import Flask

# Inicializa a aplicação Flask (corrigido para __name__)
app = Flask(__name__)

# Rota principal (a página inicial do site: htt´//127.0.0.1:5000/)
@app.route("/")
def home():
    return "<h1>Meu Web App de Gestão Financeira está no ar! 🚀</h1><p>Servidor Flask rodando com sucesso.</p>"

# Rota do Dashboard
@app.route("/dashboard")
def dashboard():
    return "<h2>Bem-vindo ao seu Dashboard Financeiro!</h2>"

# Executa o servidor localmente quando rodamrmos este arquivo 
if __name__ == "__main__":
    app.run(debug=True)