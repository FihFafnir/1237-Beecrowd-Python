import re

output = ""
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
        for i in range(len(string_1)):
            j = i
            while j < len(string_1) - i:
                # Pular substring menores ou de mesmo tamanho que a já registrada 
                if i + 1 <= max_length:
                    break
                
                substring = string_1[j:j+i+1]

                # Procura a substring dentro da segunda string
                if re.search(rf"({substring})", string_2) != None:
                    if max_length < len(substring):
                        max_length = len(substring)
                    
                j += 1

        # Adiciona a saída
        output += f"{max_length}\n"
    except EOFError:
        break

# Saída
print(output, end="")