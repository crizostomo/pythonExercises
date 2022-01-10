import locale

locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8")

valor_em_dolar_formatado = locale.currency(15000.0, grouping=True, symbol=True, international=True)
print(valor_em_dolar_formatado)