import pandas as pd

def ejercicio_02():
    empleados = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "nombre": ["Ana", "Luis", "Carla", "Pedro", "María", "Jorge"],
        "edad": [28, 45, 32, 22, 41, 39],
        "departamento": ["IT", "HR", "IT", "Ventas", "Marketing", "Ventas"],
        "salario": [60000, 48000, 75000, 30000, 55000, 62000]
    })

    print("=== Empleados de IT Y salario mayor a 60,000 ===")
    filtro1 = (empleados["departamento"] == "IT") & (empleados["salario"] > 60000)
    print(empleados[filtro1])

    print("\nEmpleados de Ventas O mayores de 40 años")
    filtro2 = (empleados["departamento"] == "Ventas") | (empleados["edad"] > 40)
    print(empleados[filtro2])

    print("\nEmpleados que NO son de Marketing")
    filtro3 = ~(empleados["departamento"] == "Marketing")
    print(empleados[filtro3])