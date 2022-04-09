seg = int(input("Digite o número de segundos: "))
ano = seg // (365 * 24 * 3600)
dia = seg // 86400
hora = seg // 3600
min = seg // 60
seg = seg % 60
print(ano,'años', dia - 365*ano, "dias,", hora - 24*dia, "horas,", min - 60*hora , "minutos y", seg, "segundos.")
