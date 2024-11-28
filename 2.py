from pprint import pprint

def get_cats_info(path):
    try: 
        with open(path, "r", encoding="utf-8") as fh:
            cats = []
            for line in fh:
                
                try:
                    id, name, age = line.strip().split(",")
                    age = int(age)  
                    cats.append({"id": id, "name": name, "age": age})
                except ValueError:
                    print(f"Невірний формат рядка: {line.strip()}")
                    continue
        return cats
    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as err:
        return f"Помилка: {err}"

if __name__ == "__main__":
    pprint(get_cats_info("./data/file_info_cats.txt"), indent=4)
