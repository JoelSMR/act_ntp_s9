import pandas as pd

def ejercicio_05():
    # Simulamos una tabla de empleados
    empleados = pd.DataFrame({
        "id": [1, 2, 3, 4, 5, 6],
        "nombre": ["Ana", "Luis", "Carla", "Pedro", "María", "Laura"],
        "edad": [28, 35, 32, 42, 41, 30],
        "departamento": ["IT", "HR", "IT", "Ventas", "Marketing", "RRHH"],
        "salario": [60000, 48000, 75000, 30000, 55000, 65000]
    })

    print("Empleados de IT con más de 30 años Y salario mayor a 60,000")
    filtro1 = (empleados["departamento"] == "IT") & (empleados["edad"] > 30) & (empleados["salario"] > 60000)
    print(empleados[filtro1])

    print("\nEmpleados cuyo nombre empieza con 'L' O son de RRHH")
    filtro2 = empleados["nombre"].str.startswith("L") | (empleados["departamento"] == "RRHH")
    print(empleados[filtro2])