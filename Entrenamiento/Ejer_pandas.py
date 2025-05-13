import pandas as pd

print("**********COTIZACION COSTO DE OBRA**********\n")
Value_Activi = ["Escavación","Cimentación","Columnas","vigas","Muros","Repello","Estuco","Pintura","Enchape","Cielo Falso"]
Value_und = ["m3","ml","ml","ml","m2","m2","m2","m2","m2","m2"]
Value_cost_u = [20000,50000,30000,30000,7500,8000,8500,5000,32000,125000]
Value_cant = [12,52,30,39,78,82,85,50,31,125]

dataset1 = {"Actividad":Value_Activi,"Unidad":Value_und,"Costo Unitario":Value_cost_u,"Cantidad":Value_cant}
df = pd.DataFrame(dataset1)
df["Costo Total"] = (df["Costo Unitario"]*df["Cantidad"])
print(df)
print("*****************************************************************\n")
print(f"Costo total de la obra: ${df["Costo Total"].sum()}  de pesos colombianos")
