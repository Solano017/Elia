def resolver_leyes_newton():
    print("=== RESOLUTOR DE SEGUNDA LEY DE NEWTON Y SISTEMAS DE BLOQUES ===")
    print("1. Sistema de 1 bloque")
    print("2. Sistema de 2 bloques en contacto (como el ejercicio de la pág. 32)")
    
    opcion = input("\nSelecciona el tipo de problema (1 o 2): ").strip()
    
    g = 9.81  # Aceleración de la gravedad en m/s^2

    if opcion == "1":
        print("\n--- SISTEMA DE 1 BLOQUE ---")
        m = float(input("Masa del bloque (m) en kg: "))
        F = float(input("Fuerza aplicada (F) en N: "))
        mu = float(input("Coeficiente de fricción (mu) [0 si no hay fricción]: "))
        
        # Cálculos
        F_friccion = mu * m * g
        F_neta = F - F_friccion
        a = F_neta / m
        W = F * float(input("Distancia recorrida (d) en metros [0 si no aplica]: ") or 0)
        
        print("\n--- RESULTADOS ---")
        print(f"• Fuerza de fricción (F_f = mu * m * g): {F_friccion:.2f} N")
        print(f"• Fuerza neta (F_neta = F - F_f): {F_neta:.2f} N")
        print(f"• Aceleración (a = F_neta / m): {a:.2f} m/s²")
        if W > 0:
            print(f"• Trabajo realizado (W = F * d): {W:.2f} J")

    elif opcion == "2":
        print("\n--- SISTEMA DE 2 BLOQUES EN CONTACTO ---")
        m1 = float(input("Masa del bloque 1 (m1) en kg: "))
        m2 = float(input("Masa del bloque 2 (m2) en kg: "))
        F = float(input("Fuerza aplicada al bloque 1 (F) en N: "))
        mu = float(input("Coeficiente de fricción (mu) [0 si no hay fricción]: "))
        
        # Masa total
        m_total = m1 + m2
        
        # Fricción total y aceleración
        F_friccion_total = mu * m_total * g
        F_neta = F - F_friccion_total
        a = F_neta / m_total
        
        # Fuerza de interacción entre bloques (F_1->2)
        F_friccion_m2 = mu * m2 * g
        F_contacto = (m2 * a) + F_friccion_m2
        
        print("\n--- RESULTADOS ---")
        print(f"• Masa total (m1 + m2): {m_total:.2f} kg")
        print(f"• Fuerza de fricción total (F_f = mu * m_total * g): {F_friccion_total:.2f} N")
        print(f"• Aceleración del sistema (a = (F - F_f) / m_total): {a:.2f} m/s²")
        print(f"• Fuerza que ejerce el bloque 1 sobre el bloque 2 (F_1->2): {F_contacto:.2f} N")

    else:
        print("Opción no válida. Reinicia el programa.")

# Ejecutar el programa
if __name__ == "__main__":
    resolver_leyes_newton()