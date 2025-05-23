# Módulo de Cores ANSI para Python3

# Reset
reset = "\033[0m"

# Estilos
bold = "\033[1m"
dim = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
invert = "\033[7m"
hidden = "\033[8m"

# Cores do Texto
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# Cores de Fundo
bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"

# Funções para cores RGB (256 cores)
def text_color_256(n):
    return f"\033[38;5;{n}m"

def bg_color_256(n):
    return f"\033[48;5;{n}m"

# Funções para cores TrueColor (16 milhões de cores)
def text_color_rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def bg_color_rgb(r, g, b):
    return f"\033[48;2;{r};{g};{b}m"

# Exemplo de uso se rodado diretamente
if __name__ == "__main__":
    print(f"{bold}{red}Texto Vermelho Negrito{reset}")
    print(f"{underline}{blue}Texto Azul Sublinhado{reset}")
    print(f"{text_color_256(196)}Texto Vermelho Intenso (256 cores){reset}")
    print(f"{bg_color_rgb(0, 128, 255)}Fundo Azul Claro (TrueColor){reset}")
