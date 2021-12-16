from datetime import datetime
from pytz import timezone

from flask import Flask

app = Flask(__name__)


@app.route("/sptime", methods = ["POST", "GET"])
def home():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone("America/Sao_Paulo")
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    return data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")


if __name__ == "__main__":
    app.run()