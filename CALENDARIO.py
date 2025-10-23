def calendario(dia, mes, ano):
    meses = [" ", "Janeirao", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
"Augosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    print(f"{dia} de {meses[mes]} de {ano}")

dianum = int(input("Digite qual o dia: "))
mesnum = int(input("Digite qual o número do mês: "))
anonum = int(input("digite qual o numero do ano: "))

calendario(dianum, mesnum, anonum)
    