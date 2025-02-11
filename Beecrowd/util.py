import os
import curses
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def menu(stdscr, title, options):
    curses.curs_set(0)
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        for i, option in enumerate(options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(options) // 2 + i
            if i == current_row:
                stdscr.addstr(y, x, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"  {option}")
        
        stdscr.addstr(0, 0, title)
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN or key == ord('s'):  
            if current_row < len(options) - 1:
                current_row += 1
        elif key == curses.KEY_UP or key == ord('w'):  
            if current_row > 0:
                current_row -= 1
        elif key == 10:  
            return options[current_row]

def main(stdscr):
    languages = {"Python": ".py", "JavaScript": ".js", "Java": ".java", "C++": ".cpp", "TypeScript": ".ts", "C": ".c", "Aleatório": "Aleatório"}
    categories = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d != "__pycache__"]
    
    category_choice = menu(stdscr, "Escolha a categoria:", categories)

    stdscr.clear()
    stdscr.addstr(0, 0, "Digite o número do exercício: ")
    stdscr.refresh()
    curses.echo()
    exercise_number = stdscr.getstr().decode("utf-8").strip()
    curses.noecho()
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Digite o título do exercício: ")
    stdscr.refresh()
    curses.echo()
    exercise_title = stdscr.getstr().decode("utf-8").strip()
    curses.noecho()

    exercise_name = f"{exercise_number}_{exercise_title}"

    language_choice = menu(stdscr, "Escolha a linguagem:", list(languages.keys()))

    if language_choice == "Aleatório":
        language_choice = random.choice(["Python", "C++"])

    exercise_path = os.path.join(BASE_DIR, category_choice, exercise_name)
    os.makedirs(exercise_path, exist_ok=True)

    solution_path = os.path.join(exercise_path, f"main{languages[language_choice]}") 
    in_txt_path = os.path.join(exercise_path, "in.txt")
    out_txt_path = os.path.join(exercise_path, "out.txt")

    if not os.path.exists(solution_path):
        with open(solution_path, "w") as f:
             if language_choice == "C++":
                f.write("""#include <bits/stdc++.h>

using namespace std;

int main(){
    
    return 0;
}
""")
    
    if not os.path.exists(in_txt_path):
        with open(in_txt_path, "w") as f:
            f.write("")  
    
    if not os.path.exists(out_txt_path):
        with open(out_txt_path, "w") as f:
            f.write("")  

    stdscr.clear()
    stdscr.addstr(0, 0, f"\nExercício '{exercise_name}' criado com sucesso em '{category_choice}' na linguagem {language_choice}!")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    if not os.environ.get("RUNNING_IN_NEW_TERMINAL"):
        os.environ["RUNNING_IN_NEW_TERMINAL"] = "1"  
        os.system("start cmd /k python " + __file__)  
    else:
        curses.wrapper(main)
