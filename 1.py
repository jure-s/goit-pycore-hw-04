def total_salary(path):
    try:

        with open(path, "r", encoding="utf-8") as fh:

            salaries = [int(el.strip().split(",")[1]) for el in fh.readlines()]

        total = sum(salaries)

        return (total, total // len(salaries))
    
    except FileNotFoundError:
        return "Файл не знайдено"
    except ZeroDivisionError:
        return "Файл порожній або не містить відомості про зарплату"
    except ValueError:
        return "Невірні дані у файлі"
    except Exception as err: 
        return str(err)


if __name__ == "__main__":

    total, average = total_salary("./data/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")