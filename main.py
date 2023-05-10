output = []
while True:
    try:
        # Entrada
        string_1 = input()
        string_2 = input()
        max_length = 0

        # Atribui a menor string na variável "string_1"
        if len(string_2) < len(string_1):
            temp = string_1
            string_1 = string_2
            string_2 = temp
        
        # Verifica cada substring possível para encontrar a substring com maior comprimento
        for i in range(1, len(string_1)):
            for j in range(len(string_1) - i + 1):
                # Procura a substring dentro da segunda string
                substring = string_1[j:j+i]
                if substring in string_2:
                    max_length = len(substring)
                    break 
        # Adiciona a saída
        output.append(max_length)
    except EOFError:
        break

# Saída
for i in output:
    print(i)
