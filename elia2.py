def pedir_float(mensaje, *, min_value=0.0):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debes introducir un número.")
            continue

        if min_value is not None and valor < min_value:
            print(f"El valor debe ser >= {min_value}.")
            continue

        return valor


def resolver_sistema_1_bloque():
    print("\n--- SISTEMA DE 1 BLOQUE ---")
    m = pedir_float("Masa del bloque (m) en kg: ", min_value=0.0)
    F_aplicada = pedir_float("Fuerza horizontal aplicada (F) en N: ", min_value=0.0)
    mu = pedir_float("Coeficiente de fricción (mu) [0 si no hay]: ", min_value=0.0)

    g = 9.81
    N = m * g
    f_max = mu * N

    if F_aplicada > f_max:
        f_real = f_max
        F_neta = F_aplicada - f_real
        a = F_neta / m
        se_mueve = True
    else:
        f_real = F_aplicada
        F_neta = 0.0
        a = 0.0
        se_mueve = False
#aaa
    resultado = {
        "N": N,
        "f_max": f_max,
        "f_real": f_real,
        "F_neta": F_neta,
        "a": a,
        "se_mueve": se_mueve,
    }

    print("\n" + "=" * 30 + " RESULTADOS " + "=" * 30)
    print(f"• Fuerza Normal (N = m * g): {resultado['N']:.2f} N")
    print(f"• Fuerza de fricción máxima: {resultado['f_max']:.2f} N")
    print(f"• Fuerza de fricción real: {resultado['f_real']:.2f} N")
    print(f"• Fuerza neta: {resultado['F_neta']:.2f} N")
    print(f"• Aceleración: {resultado['a']:.2f} m/s²")

    if not resultado["se_mueve"] and mu > 0:
        print("\n[NOTA]: La fuerza aplicada no es suficiente para vencer la fricción.")
        print("El objeto permanece en reposo.")

    return resultado


def resolver_sistema_2_bloques():
    print("\n--- SISTEMA DE 2 BLOQUES EN CONTACTO ---")
    m1 = pedir_float("Masa del bloque 1 (m1) en kg: ", min_value=0.0)
    m2 = pedir_float("Masa del bloque 2 (m2) en kg: ", min_value=0.0)
    F_aplicada = pedir_float("Fuerza aplicada sobre el bloque 1 (F) en N: ", min_value=0.0)
    mu = pedir_float("Coeficiente de fricción (mu) [0 si no hay]: ", min_value=0.0)

    g = 9.81
    m_total = m1 + m2
    N_total = m_total * g
    f_total_max = mu * N_total

    if F_aplicada > f_total_max:
        f_total_real = f_total_max
        F_neta = F_aplicada - f_total_real
        a = F_neta / m_total

        f_m2 = mu * (m2 * g)
        F_contacto = (m2 * a) + f_m2
        se_mueve = True
    else:
        f_total_real = F_aplicada
        F_neta = 0.0
        a = 0.0
        F_contacto = 0.0
        se_mueve = False

    resultado = {
        "m_total": m_total,
        "N_total": N_total,
        "f_total_real": f_total_real,
        "F_neta": F_neta,
        "a": a,
        "F_contacto": F_contacto,
        "se_mueve": se_mueve,
    }

    print("\n" + "=" * 30 + " RESULTADOS " + "=" * 30)
    print(f"• Masa total (m1 + m2): {resultado['m_total']:.2f} kg")
    print(f"• Fuerza Normal total: {resultado['N_total']:.2f} N")
    print(f"• Fuerza de fricción total real: {resultado['f_total_real']:.2f} N")
    print(f"• Fuerza neta del sistema: {resultado['F_neta']:.2f} N")
    print(f"• Aceleración del sistema: {resultado['a']:.2f} m/s²")
    print(f"• Fuerza de interacción (F_1->2): {resultado['F_contacto']:.2f} N")

    if not resultado["se_mueve"] and mu > 0:
        print("\n[NOTA]: El sistema no se mueve porque la fuerza es menor que la fricción estática.")

    return resultado


def main():
    print("=" * 60)
    print(" RESOLUTOR AVANZADO: SEGUNDA LEY DE NEWTON Y FRICCIÓN")
    print("=" * 60)

    while True:
        print("\n1. Sistema de 1 bloque")
        print("2. Sistema de 2 bloques en contacto")
        print("3. Salir")

        opcion = input("\nSelecciona el tipo de problema (1, 2 o 3): ").strip()

        if opcion == "1":
            resolver_sistema_1_bloque()
        elif opcion == "2":
            resolver_sistema_2_bloques()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
