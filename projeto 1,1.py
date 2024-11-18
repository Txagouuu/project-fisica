import tkinter as tk
from tkinter.ttk import Combobox

# Função para calcular a distância
def calcular_distancia():
    try:
        h = float(entry1.get())  # Altura inicial
        mu_c = float(entry2.get())  # Coeficiente de atrito
        c = float(entry3.get())  # Razão entre massas m2/m1
        
        # Verificar tipo de colisão
        tipo_colisao = tipo_colisao_combobox.get()
        
        if tipo_colisao == "Elástica":
            # Fórmula para colisão elástica
            d = (4 * h) / (mu_c * (1 + c)**2)
        elif tipo_colisao == "Não-elástica":
            # Fórmula para colisão não-elástica
            d = (h) / (mu_c * (1 + c)**2)
        else:
            result_label.config(text="Erro: Selecione um tipo de colisão.")
            return
        
        # Exibir resultado
        result_label.config(text=f"Distância d: {d:.3f} m")
    except ValueError:
        result_label.config(text="Erro: Insira valores válidos.")

# Janela principal
root = tk.Tk()
root.title("Cálculo de Distância após Colisão")
root.configure(bg="gray")

# Rótulo e entrada para altura
label1 = tk.Label(root, text="Altura inicial (h):", font=("Helvetica", 18, "bold"), bg="gray", fg="black")
label1.pack(pady=5)
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

# Rótulo e entrada para coeficiente de atrito
label2 = tk.Label(root, text="Coeficiente de atrito (μc):", font=("Helvetica", 18, "bold"), bg="gray", fg="black")
label2.pack(pady=5)
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

# Rótulo e entrada para razão de massas
label3 = tk.Label(root, text="Razão entre massas (c = m2/m1):", font=("Helvetica", 18, "bold"), bg="gray", fg="black")
label3.pack(pady=5)
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

# Combobox para selecionar o tipo de colisão
label4 = tk.Label(root, text="Tipo de colisão:", font=("Helvetica", 18, "bold"), bg="gray", fg="black")
label4.pack(pady=5)
tipo_colisao_combobox = Combobox(root, values=["Elástica", "Não-elástica"], state="readonly", width=30)
tipo_colisao_combobox.pack(pady=5)
tipo_colisao_combobox.set("Elástica")  # Valor padrão

# Botão para calcular
button = tk.Button(root, text="Calcular Distância", command=calcular_distancia)
button.pack(pady=10)

# Rótulo para exibir o resultado
result_label = tk.Label(root, text="", font=("Arial", 20), bg="white")
result_label.pack(pady=20)

# Loop principal
root.mainloop()
