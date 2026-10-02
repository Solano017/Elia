def resolver_leyes_newton_corregido():
    print("=" * 60)
    print(" RESOLUTOR AVANZADO: SEGUNDA LEY DE NEWTON Y FRICCIÓN")
    print("=" * 60)
    print("1. Sistema de 1 bloque")
    print("2. Sistema de 2 bloques en contacto")
    
    opcion = input("\nSelecciona el tipo de problema (1 o 2): ").strip()
    
    # Gravedad utilizada en las lecturas
    g = 9.81  

    if opcion == "1":
        print("\n--- SISTEMA DE 1 BLOQUE ---")
        m = float(input("Masa del bloque (m) en kg: "))
        F_aplicada = float(input("Fuerza horizontal aplicada (F) en N: "))
        mu = float(input("Coeficiente de fricción (mu) [0 si no hay]: "))
        
        # 1. Fuerza Normal y Fricción Máxima
        Normal = m * g
        F_friccion_max = mu * Normal
        
        # 2. Análisis del movimiento
        if F_aplicada > F_friccion_max:
            F_friccion_real = F_friccion_max
            F_neta = F_aplicada - F_friccion_real
            a = F_neta / m
            se_mueve = True
        else:
            # Si F_aplicada <= F_friccion_max, el objeto se queda estático
            F_friccion_real = F_aplicada  # La fricción estática iguala la fuerza
            F_neta = 0.0
            a = 0.0
            se_mueve = False
            
        print("\n" + "=" * 30 + " RESULTADOS " + "=" * 30)
        print(f"• Fuerza Normal (N = m * g): {Normal:.2f} N")
        print(f"• Fuerza de fricción máxima (F_f_max = mu * N): {F_friccion_max:.2f} N")
        print(f"• Fuerza de fricción REAL actuando: {F_friccion_real:.2f} N")
        print(f"• Fuerza neta (F_neta = F - F_f_real): {F_neta:.2f} N")
        print(f"• Aceleración (a = F_neta / m): {a:.2f} m/s²")
        
        if not se_mueve and mu > 0:
            print("\n  [NOTA]: La fuerza aplicada no es suficiente para vencer la fricción.")
            print("          El objeto permanece en reposo (a = 0 m/s²).")

    elif opcion == "2":
        print("\n--- SISTEMA DE 2 BLOQUES EN CONTACTO ---")
        m1 = float(input("Masa del bloque 1 (m1) en kg: "))
        m2 = float(input("Masa del bloque 2 (m2) en kg: "))
        F_aplicada = float(input("Fuerza aplicada sobre el bloque 1 (F) en N: "))
        mu = float(input("Coeficiente de fricción (mu) [0 si no hay]: "))
        
        m_total = m1 + m2
        Normal_total = m_total * g
        F_friccion_total_max = mu * Normal_total
        
        if F_aplicada > F_friccion_total_max:
            F_friccion_total_real = F_friccion_total_max
            F_neta = F_aplicada - F_friccion_total_real
            a = F_neta / m_total
            
            # Fricción individual en el bloque 2 y fuerza de contacto
            F_friccion_m2 = mu * (m2 * g)
            F_contacto = (m2 * a) + F_friccion_m2
            se_mueve = True
        else:
            F_friccion_total_real = F_aplicada
            F_neta = 0.0
            a = 0.0
            F_contacto = 0.0
            se_mueve = False

        print("\n" + "=" * 30 + " RESULTADOS " + "=" * 30)
        print(f"• Masa total (m1 + m2): {m_total:.2f} kg")
        print(f"• Fuerza Normal total (N_total = m_total * g): {Normal_total:.2f} N")
        print(f"• Fuerza de fricción total REAL: {F_friccion_total_real:.2f} N")
        print(f"• Fuerza neta del sistema: {F_neta:.2f} N")
        print(f"• Aceleración del sistema: {a:.2f} m/s²")
        print(f"• Fuerza de interacción (F_1->2): {F_contacto:.2f} N")
        
        if not se_mueve and mu > 0:
            print("\n  [NOTA]: El sistema no se mueve porque la fuerza es menor que la fricción estática.")

# Ejecutar el script
if __name__ == "__main__":
    resolver_leyes_newton_corregido()