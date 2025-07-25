import tkinter as tk
from tkinter import ttk,messagebox

saldo = 0

def creacuenta():
    #nombre=entrada_nombre.get()
    global saldo
    global sld
    tk.Label(root, text="Primer nombre: ").pack()
    tk.Label(root, text=entrada_nombre.get()).pack()
    tk.Label(root, text="Apellido: ").pack()
    tk.Label(root, text=entrada_apellido.get()).pack()
    tk.Label(root, text="Numero de cuenta: ").pack()
    tk.Label(root, text=entrada_numcuenta.get()).pack()
    tk.Label(root, text="Tipo de cuenta: ").pack()
    tk.Label(root, text=entrada_tipocuenta.get()).pack()
    tk.Label(root, text="Pin: ").pack()
    tk.Label(root, text=entrada_pin.get()).pack()
    tk.Label(root, text="Saldo: ").pack()
    sld = tk.Label(root, text=entrada_saldo.get())
    sld.pack()
    saldo = sld.cget("text")
    print(saldo)

def depositar():
    global saldo
    cantidad = entrada_cantidad.get()
    saldoactual=int(saldo)
    saldoactual += int(cantidad)
    print(saldoactual)
    sld.config(text=saldoactual)
    saldo=saldoactual


def retirar():
    cantidad=entrada_cantidad.get()

root=tk.Tk()
root.title("Banco")
root.geometry("300x200")
tk.Label(root, text="Ejercicio Banco").pack()

tk.Label(root, text="Datos para crear una cuenta: ").pack()

tk.Label(root, text="Primer nombre: ").pack()
entrada_nombre = tk.Entry(root)
entrada_nombre.pack()

tk.Label(root, text="Apellido: ").pack()
entrada_apellido = tk.Entry(root)
entrada_apellido.pack()

tk.Label(root, text="Numero de cuenta: ").pack()
entrada_numcuenta = tk.Entry(root)
entrada_numcuenta.pack()

tk.Label(root, text="Tipo de cuenta: ").pack()
entrada_tipocuenta = tk.Entry(root)
entrada_tipocuenta.pack()

tk.Label(root, text="Pin: ").pack()
entrada_pin = tk.Entry(root)
entrada_pin.pack()

tk.Label(root, text="Saldo: ").pack()
entrada_saldo = tk.Entry(root)
entrada_saldo.pack()

tk.Button(root, text="Crear cuenta", command=creacuenta).pack()

tk.Label(root, text="Cantidad: ").pack()
entrada_cantidad = tk.Entry(root)
entrada_cantidad.pack()

tk.Button(root, text="Depositar", command=depositar).pack()
tk.Button(root, text="Retirar", command=retirar).pack()

root.mainloop()