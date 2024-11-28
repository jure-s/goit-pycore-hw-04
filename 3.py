import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory(path: Path, indent=0):

    try:

        if not path.is_dir():
            print(Fore.RED + f"Помилка: {path} не є директорією!")
            return
        
        for item in path.iterdir():
            if item.is_dir():

                print(Fore.BLUE + " " * indent + f"📂 {item.name}")

                visualize_directory(item, indent + 3)
            else:

                print(Fore.GREEN + " " * indent + f"📜 {item.name}")
    except FileNotFoundError:
        print(Fore.RED + "Помилка: вказана директорія не знайдена!")
    except Exception as e:
        print(Fore.RED + f"Помилка: {str(e)}")


def main():

    try:
        args = sys.argv
        if len(args) != 2:
            raise Exception("Необхідно вказати шлях до директорії!")

        folder_path = Path(args[1])

        if not folder_path.exists():
            raise FileNotFoundError("Директорію не знайдено")

        print(Fore.CYAN + folder_path.resolve().name)
        visualize_directory(folder_path)
        
    except Exception as err:
        print(Fore.RED + str(err))


if __name__ == "__main__":
    main()
