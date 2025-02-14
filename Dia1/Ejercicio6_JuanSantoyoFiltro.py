# Descripción: Programa que calcula el salario neto de N empleados, teniendo en cuenta que el valor de la hora
N = int(input("Ingrese el número de empleados: "))
valor_hora = 20000
sueldos_brutos = []
sueldos_netos = []
eps_total = 0
pension_total = 0

for i in range(N):
  nombre = input("Ingrese el nombre del empleado: ")
  horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
  sueldo_bruto = horas_trabajadas * valor_hora
  eps = sueldo_bruto * 0.04
  pension = sueldo_bruto * 0.04
  sueldo_neto = sueldo_bruto - eps - pension
  sueldos_brutos.append(sueldo_bruto)
  sueldos_netos.append(sueldo_neto)
  eps_total += eps
  pension_total += pension
  print(f"Empleado: ", nombre)
  print(f"Sueldo bruto: $", sueldo_bruto)
  print(f"Descuento EPS: $", eps)
  print(f"Descuento pensión: $", pension)
  print(f"Sueldo neto: $", sueldo_neto)

# Cálculo de estadísticas
sueldo_bruto_total = sum(sueldos_brutos)
sueldo_neto_total = sum(sueldos_netos)
promedio_bruto = sueldo_bruto_total / N
promedio_neto = sueldo_neto_total / N

# Empleado con mayor y menor salario neto
indice_mayor = sueldos_netos.index(max(sueldos_netos))
indice_menor = sueldos_netos.index(min(sueldos_netos))

print("\nEstadísticas:")
print(f"Total sueldos brutos: $", sueldo_bruto_total)
print(f"Total descuentos EPS: $", eps_total)
print(f"Total descuentos pensión: $", pension_total)
print(f"Total sueldos netos: $", sueldo_neto_total)
print(f"Promedio sueldo bruto: $", promedio_bruto)
print(f"Promedio sueldo neto: $", promedio_neto)
print(f"Empleado que más gana: {nombre[indice_mayor]} (${sueldos_netos[indice_mayor]:.2f})")
print(f"Empleado que menos gana: {nombre[indice_menor]} (${sueldos_netos[indice_menor]:.2f})")
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117