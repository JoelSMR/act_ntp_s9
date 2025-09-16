import pandas as pd

def ejercicio_04():
    empleados = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "nombre": ["Ana", "Luis", "Carla", "Pedro", "María", "Jorge"],
        "edad": [28, 35, 32, 42, 41, 39],
        "departamento": ["IT", "HR", "IT", "Ventas", "Marketing", "Recursos Humanos"],
        "salario": [60000, 48000, 75000, 30000, 55000, 62000]
    })

    print("Empleados cuyos nombres empiezan con 'M'")
    filtro1 = empleados["nombre"].str.startswith("M")
    print(empleados[filtro1])

    print("\nEmpleados en departamentos que contienen 'R'")
    filtro2 = empleados["departamento"].str.contains("R", case=False)  
    print(empleados[filtro2])