dinero = 2000
hambre = 18
precio_helado = 100
heladosquemehecomido= 0
aumento=1.2

while(0<hambre<85 and dinero>0):
    hambre = hambre + hambre
    dinero_gastado= (heladosquemehecomido+1)*precio_helado*aumento
    precio_helado= precio_helado*aumento
    heladosquemehecomido = heladosquemehecomido + 1
dinero_restante = dinero-dinero_gastado

print("si me tomo", heladosquemehecomido + 1, "estoy llenito")
print("todavía tengo", (dinero_restante), "euros")