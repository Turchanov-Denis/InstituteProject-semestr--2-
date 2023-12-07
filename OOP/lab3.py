# Turchanov Denis 4PM
import re


class Draw_Console:
    def __init__(self):
        self.alphabets = {
            'standard': {
                'A': [
                    "  A  ",
                    " A A ",
                    "AAAAA",
                    "A   A",
                    "A   A",
                ],
                'B': [
                    "BBBB ",
                    "B   B",
                    "BBBB ",
                    "B   B",
                    "BBBB ",
                ],
                'C': [
                    " CCC ",
                    "C    ",
                    "C    ",
                    "C    ",
                    " CCC ",
                ],
                'D': [
                    "DDD  ",
                    "D   D",
                    "D   D",
                    "D   D",
                    "DDD  ",
                ],
                'E': [
                    "EEEEE",
                    "E    ",
                    "EEEE ",
                    "E    ",
                    "EEEEE",
                ],
                'F': [
                    "FFFFF",
                    "F    ",
                    "FFF  ",
                    "F    ",
                    "F    ",
                ],
                'G': [
                    " GGG ",
                    "G    ",
                    "G  GG",
                    "G   G",
                    " GGGG",
                ],
                'H': [
                    "H   H",
                    "H   H",
                    "HHHHH",
                    "H   H",
                    "H   H",
                ],
                'I': [
                    " III ",
                    "  I  ",
                    "  I  ",
                    "  I  ",
                    " III ",
                ],
                'J': [
                    "   JJ",
                    "   J ",
                    "   J ",
                    "J  J ",
                    " JJ  ",
                ],
                'K': [
                    "K   K",
                    "K  K ",
                    "KK   ",
                    "K  K ",
                    "K   K",
                ],
                'L': [
                    "L    ",
                    "L    ",
                    "L    ",
                    "L    ",
                    "LLLLL",
                ],

                'M': [
                    "M       M",
                    "MM     MM",
                    "M M   M M",
                    "M  M M  M",
                    "M   M   M",
                ],
                'N': [
                    "N       N",
                    "NN      N",
                    "N N     N",
                    "N  N    N",
                    "N    NNNN",
                ],
                'O': [
                    "  OOOO  ",
                    " O    O ",
                    "O      O",
                    " O    O ",
                    "  OOOO  ",
                ],
                'P': [
                    "PPPPP  ",
                    "P     P",
                    "PPPPP  ",
                    "P      ",
                    "P      ",
                ],
                'Q': [
                    "  QQQQ  ",
                    " Q    Q ",
                    "Q  Q  Q",
                    " Q   Q ",
                    "  QQQ  Q",
                ],
                'R': [
                    "RRRR ",
                    "R   R",
                    "RRRR ",
                    "R R  ",
                    "R  RR",
                ],
                'S': [
                    " SSS ",
                    "S    ",
                    " SSS ",
                    "    S",
                    " SSS ",
                ],
                'T': [
                    "TTTTT",
                    "  T  ",
                    "  T  ",
                    "  T  ",
                    "  T  ",
                ],
                'U': [
                    "U   U",
                    "U   U",
                    "U   U",
                    "U   U",
                    " UUU ",
                ],
                'V': [
                    "V   V",
                    "V   V",
                    "V   V",
                    " V V ",
                    "  V  ",
                ],
                'W': [
                    "W   W",
                    "W   W",
                    "W W W",
                    "WW WW",
                    "W   W",
                ],
                'X': [
                    "X   X",
                    " X X ",
                    "  X  ",
                    " X X ",
                    "X   X",
                ],
                'Y': [
                    "Y   Y",
                    " Y Y ",
                    "  Y  ",
                    "  Y  ",
                    "  Y  ",
                ],
                'Z': [
                    "ZZZZZ",
                    "   Z ",
                    "  Z  ",
                    " Z   ",
                    "ZZZZZ",
                ],
            },
            'big': {
                'A': [
                    "   AA   ",
                    "  A  A  ",
                    " AAAAA  ",
                    "A      A",
                    "A      A",
                ],
                'B': [
                    "BBBBB  ",
                    "B    B ",
                    "BBBBBB ",
                    "B    B ",
                    "BBBBB  ",
                ],
                'C': [
                    "  CCCC  ",
                    " C      ",
                    " C      ",
                    " C      ",
                    "  CCCC  ",
                ],
                'D': [
                    "DDDD   ",
                    "D    D ",
                    "D     D",
                    "D    D ",
                    "DDDD   ",
                ],
                'E': [
                    "EEEEEE ",
                    "E      ",
                    "EEEEE  ",
                    "E      ",
                    "EEEEEE ",
                ],
                'F': [
                    "FFFFFF ",
                    "F      ",
                    "FFFFF  ",
                    "F      ",
                    "F      ",
                ],
                'G': [
                    "  GGGG  ",
                    " G      ",
                    " G  GGGG",
                    " G     G",
                    "  GGGG G",
                ],
                'H': [
                    "H      H",
                    "H      H",
                    "HHHHHHHH",
                    "H      H",
                    "H      H",
                ],
                'I': [
                    " IIIII ",
                    "   I   ",
                    "   I   ",
                    "   I   ",
                    " IIIII ",
                ],
                'J': [
                    "      JJ",
                    "      J ",
                    "      J ",
                    "J     J ",
                    " JJJJJ  ",
                ],
                'K': [
                    "K     K",
                    "K   K  ",
                    "KKK    ",
                    "K   K  ",
                    "K     K",
                ],
                'L': [
                    "L      ",
                    "L      ",
                    "L      ",
                    "L      ",
                    "LLLLLLL",
                ],
                'M': [
                    "M       M",
                    "MM     MM",
                    "M M   M M",
                    "M  M M  M",
                    "M   M   M",
                ],
                'N': [
                    "N       N",
                    "NN      N",
                    "N N     N",
                    "N  N    N",
                    "N    NNNN",
                ],
                'O': [
                    "  OOOO  ",
                    " O    O ",
                    "O      O",
                    " O    O ",
                    "  OOOO  ",
                ],
                'P': [
                    "PPPPP  ",
                    "P     P",
                    "PPPPP  ",
                    "P      ",
                    "P      ",
                ],
                'Q': [
                    "  QQQQ  ",
                    " Q    Q ",
                    "Q  Q  Q",
                    " Q   Q ",
                    "  QQQ  Q",
                ], 'R': [
                    "RRRR  ",
                    "R    R",
                    "RRRR  ",
                    "R   R ",
                    "R    RR",
                ],
                'S': [
                    "  SSSS ",
                    " S     ",
                    "  SSSS ",
                    "     S ",
                    " SSSS  ",
                ],
                'T': [
                    "TTTTTTT",
                    "   T   ",
                    "   T   ",
                    "   T   ",
                    "   T   ",
                ],
                'U': [
                    "U     U",
                    "U     U",
                    "U     U",
                    "U     U",
                    " UUUUU ",
                ],
                'V': [
                    "V     V",
                    "V     V",
                    " V   V ",
                    "  V V  ",
                    "   V   ",
                ],
                'W': [
                    "W     W",
                    "W     W",
                    "W  W  W",
                    "WW   WW",
                    "W     W",
                ],
                'X': [
                    "X     X",
                    " X   X ",
                    "  X X  ",
                    " X   X ",
                    "X     X",
                ],
                'Y': [
                    "Y     Y",
                    " Y   Y ",
                    "  Y Y  ",
                    "   Y   ",
                    "   Y   ",
                ],
                'Z': [
                    "ZZZZZZZ",
                    "    Z  ",
                    "   Z   ",
                    "  Z    ",
                    "ZZZZZZZ",
                ],

            }
        }
        self.symbol = '*'  # Символ по умолчанию
        self.current_font = 'standard'
        self.color = '\033[0m'  # Default color

    def set_font(self, font_name):
        if font_name in self.alphabets:
            self.current_font = font_name
        else:
            print(f"Шрифт '{font_name}' не найден. Используется 'standard'.")

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_color(self, color_code):
        self.color = f'\033[{color_code}m'

    def print_art(self, text, x=0, y=0):
        lines = [""] * len(self.alphabets[self.current_font]['A'])

        for char in text:
            if char.upper() in self.alphabets[self.current_font]:
                char_data = self.alphabets[self.current_font][char.upper()]
                for i, line in enumerate(char_data):
                    if y + i < len(lines):
                        formatted_line = re.sub(r"[A-Z]", self.symbol, line)
                        lines[y + i] += " " * x + formatted_line
                    else:
                        break

        for line in lines:
            print(self.color + line + '\033[0m')


# Тестирование
if __name__ == "__main__":
    draw_console = Draw_Console()

    try:
        draw_console.set_font('big')  # Установите шрифт по вашему выбору
        draw_console.set_symbol('&')  # Установите символ по вашему выбору
        draw_console.set_color('32')  # Установите цвет по вашему выбору
        draw_console.print_art("Hello world", x=10, y=1)
    except KeyboardInterrupt:
        pass
