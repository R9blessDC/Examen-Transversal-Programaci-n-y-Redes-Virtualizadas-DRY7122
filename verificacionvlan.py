def veri_vlan(numero_vlan):
        if 1 <= numero_vlan <= 1005:
            print(f"VLAN {numero_vlan} pertenece al rango normal.")
        elif 1006 <= numero_vlan <= 4094:
            print(f"VLAN {numero_vlan} pertenece al rango extendido.")
        else:
            print("Número de VLAN inválido.")

if __name__ == "__main__":
    vlan = int(input("Ingrese el número de VLAN: "))
    veri_vlan(vlan)
