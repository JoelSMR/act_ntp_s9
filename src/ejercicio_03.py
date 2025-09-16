import pandas as pd

def ejercicio_03():
    empleados = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "nombre": ["Ana", "Luis", "Carla", "Pedro", "María", "Jorge"],
        "edad": [28, 35, 32, 42, 41, 39],
        "departamento": ["IT", "HR", "IT", "Ventas", "Marketing", "Ventas"],
        "salario": [60000, 48000, 75000, 30000, 55000, 62000]
    })

    print("Empleados de IT o Ventas")
    filtro1 = empleados["departamento"].isin(["IT", "Ventas"])
    print(empleados[filtro1])

    print("\nEmpleados con edad de 28, 35 o 42 años")
    filtro2 = empleados["edad"].isin([28, 35, 42])
    print(empleados[filtro2])