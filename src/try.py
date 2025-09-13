from os import system

for i in range(1 ,int(input("CANTIDAD ARCHIVOS"))+1):
    string_name= f"ejercicio_0{i}.py" if i <10 else f"ejercicio_{i}.py" 
    print(string_name)
    system(f'type nul > "{string_name}"')