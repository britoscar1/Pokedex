# Codigos de color ANSI
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


def color(texto, c):
    return f"{c}{texto}{RESET}"


def banner_bienvenida():
    print(CYAN + NEGRITA)
    print("  ____   ___  _  _________ ____  _______  __")
    print(" |  _ \\ / _ \\| |/ / ____|  _ \\| ____\\ \\/ /")
    print(" | |_) | | | | ' /|  _| | | | |  _|  \\  / ")
    print(" |  __/| |_| | . \\| |___| |_| | |___ /  \\ ")
    print(" |_|    \\___/|_|\\_\\_____|____/|_____/_/\\_\\")
    print(RESET)


def titulo_menu(texto):
    linea = "=" * 42
    print(color(linea, CYAN))
    print(color(f"  {texto}", CYAN + NEGRITA))
    print(color(linea, CYAN))


def barra_vida(nombre, vida_actual, vida_max=200, largo=20):
    if vida_max <= 0:
        vida_max = 1
    porcentaje = max(0, min(1, vida_actual / vida_max))
    llenas = int(porcentaje * largo)
    vacias = largo - llenas

    if porcentaje > 0.6:
        c = VERDE
    elif porcentaje > 0.3:
        c = AMARILLO
    else:
        c = ROJO

    barra = color("█" * llenas, c) + color("░" * vacias, BLANCO)
    return f"{nombre:<14} HP: [{barra}] {vida_actual}/{vida_max}"


def mensaje_victoria():
    print(VERDE + NEGRITA)
    print("  __     ___      _             _       _ ")
    print("  \\ \\   / (_) ___| |_ ___  _ __(_) __ _| |")
    print("   \\ \\ / /| |/ __| __/ _ \\| '__| |/ _` | |")
    print("    \\ V / | | (__| || (_) | |  | | (_| |_|")
    print("     \\_/  |_|\\___|\\__\\___/|_|  |_|\\__,_(_)")
    print(RESET)


def mensaje_derrota():
    print(ROJO + NEGRITA)
    print("   ____                    _        ")
    print("  |  _ \\  ___ _ __ _ __ ___ | |_ __ _ ")
    print("  | | | |/ _ \\ '__| '__/ _ \\| __/ _` |")
    print("  | |_| |  __/ |  | | | (_) | || (_| |")
    print("  |____/ \\___|_|  |_|  \\___/ \\__\\__,_|")
    print(RESET)
