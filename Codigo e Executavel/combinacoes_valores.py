import tkinter as tk
from itertools import combinations
import re

def closest_sum(numbers, target):
    closest_combination = None
    closest_difference = float('inf')
    for i in range(1, len(numbers) + 1):
        for combination in combinations(numbers, i):
            difference = abs(sum(combination) - target)
            if difference < closest_difference:
                closest_combination = combination
                closest_difference = difference
    return closest_combination

def currency_to_float(currency_str):
    currency_str = re.sub(r'[^\d,]', '', currency_str)
    currency_str = currency_str.replace(',', '.')
    return float(currency_str)

def calcular():
    target = float(target_entry.get())
    list_number = list(values_entry.get())
    string = ''.join(list_number)
    lista_de_strings = string.split()
    lista_de_strings = [x for x in lista_de_strings if x != 'R$']
    numbers = list(map(currency_to_float, lista_de_strings))
    result = closest_sum(numbers, target)
    soma = round(sum(result),2)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f'- A combinação mais próxima é: {result}\n- Valor desejado: {target}\n- Valor obtido: {soma}')

root = tk.Tk()
root.title("Código de Combinação de Valores")

target_label = tk.Label(root, text="Qual o valor desejado para a soma?")
target_label.pack()
target_entry = tk.Entry(root)
target_entry.pack()

values_label = tk.Label(root, text="Quais os valores para fazer a combinação? (Separados por espaço)")
values_label.pack()
values_entry = tk.Entry(root)
values_entry.pack()

calculate_button = tk.Button(root, text="Calcular", command=calcular)
calculate_button.pack()

result_text = tk.Text(root, height=5, width=48)
result_text.insert(tk.END, "Por favor, insira os dados acima para obter sua combinação")
result_text.pack(pady=30, padx=30)


root.mainloop()
