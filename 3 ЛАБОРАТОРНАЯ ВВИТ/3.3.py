def read_file(filename):
    mode = input("Выберите режим чтения (all - весь файл, line - построчно): ")
    try:
        with open(filename, "r") as file:
            if mode == "all":
                content = file.read()
                print(content)
            elif mode == "line":
                for line in file:
                    print(line, end="")
            else:
                print("Неверный режим чтения.")

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

read_file("example.tt")