def read_file(filename, mode="all"):
    mode = input("Выберите режим чтения (all - весь файл, line - построчно): ")

    with open(filename, "r") as file:
        if mode == "all":
            content = file.read()
            print(content)
        elif mode == "line":
            for line in file:
                print(line, end="")
        else:
            print("Неверный режим чтения.")

read_file("example.txt")
print("\n")
read_file("example.txt", mode="line")