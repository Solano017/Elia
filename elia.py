def resolver_leyes_newton():
    print("=== RESOLUTOR DE SEGUNDA LEY DE NEWTON Y SISTEMAS DE BLOQUES ===")
    print("1. Sistema de 1 bloque")
    print("2. Sistema de 2 bloques en contacto")

    opcion = input("\nSelecciona el tipo de problema (1 o 2): ").strip()

    if opcion == "1":
        print("\n--- SISTEMA DE 1 BLOQUE ---")

        m = float(input("Masa del bloque (m) en kg: "))
        F = float(input("Fuerza aplicada (F) en N: "))
        F_friccion = float(input("Fuerza de fricción en N: "))

        # Cálculos
        F_neta = F - F_friccion
        a = F_neta / m

        print("\n--- RESULTADOS ---")
        print(f"• Fuerza de fricción: {F_friccion:.2f} N")
        print(f"• Fuerza neta: {F_neta:.2f} N")
        print(f"• Aceleración: {a:.2f} m/s²")

    elif opcion == "2":
        print("\n--- SISTEMA DE 2 BLOQUES EN CONTACTO ---")

        m1 = float(input("Masa del bloque 1 (m1) en kg: "))
        m2 = float(input("Masa del bloque 2 (m2) en kg: "))
        F = float(input("Fuerza aplicada al bloque 1 (F) en N: "))

        # Fricción de CADA bloque
        f1 = float(input("Fricción del bloque 1 en N: "))
        f2 = float(input("Fricción del bloque 2 en N: "))

        # Masa total
        m_total = m1 + m2

        # Fricción total
        F_friccion_total = f1 + f2

        # Fuerza neta
        F_neta = F - F_friccion_total

        # Aceleración del sistema
        a = F_neta / m_total

        # Fuerza que ejerce el bloque 1 sobre el bloque 2
        F_contacto = m2 * a + f2

        print("\n--- RESULTADOS ---")
        print(f"• Masa total: {m_total:.2f} kg")
        print(f"• Fuerza de fricción total: {F_friccion_total:.2f} N")
        print(f"• Fuerza neta: {F_neta:.2f} N")
        print(f"• Aceleración del sistema: {a:.2f} m/s²")
        print(f"• Fuerza del bloque 1 sobre el bloque 2: {F_contacto:.2f} N")

    else:
        print("Opción no válida. Reinicia el programa.")


# Ejecutar el programa
if __name__ == "__main__":
    resolver_leyes_newton()