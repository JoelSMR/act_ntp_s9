import pandas as pd

def ejercicio_01():
    empleados = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
        "edad": [28, 40, 32, 22, 36],
        "departamento": ["IT", "HR", "IT", "Ventas", "IT"],
        "salario": [60000, 48000, 52000, 30000, 75000]
    })

    print("Empleados con salario mayor a 50,000")
    print(empleados[empleados["salario"] > 50000])

    print("\nEmpleados menores de 35 años")
    print(empleados[empleados["edad"] < 35])

    print("\nEmpleados del departamento 'IT'")
    print(empleados[empleados["departamento"] == "IT"])