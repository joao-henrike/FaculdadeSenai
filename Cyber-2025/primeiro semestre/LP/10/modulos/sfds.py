with open('teste.txt', "w", encoding="utf-8") as f:
    i = 0
    for linha in f:
        i = i + 1
        print(str(i) + ": "+ linha)