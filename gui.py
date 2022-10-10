from tkinter import *
from tkinter import ttk
import main

window = Tk()
window.title("Конвертер валют")
window.geometry("250x350")

def calcvalue():
  if var.get() == "AMD":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyAMD(main.a)
      title["text"] = main.currencyAMDT()

  elif var.get() == "AUD":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyAUD(main.a)
      title["text"] = main.currencyAUDT()

  elif var.get() == "BYN":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyBYN(main.a)
      title["text"] = main.currencyBYNT()

  elif var.get() == "DKK":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyDKK(main.a)
      title["text"] = main.currencyDKKT()

  elif var.get() == "USD":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyUSD(main.a)
      title["text"] = main.currencyUSDT()

  elif var.get() == "EUR":
      a = entry.get()
      main.a = float(a)
      label["text"] = main.currencyEUR(a)
      title["text"] = main.currencyEURT()


currency= ('AMD','AUD','BYN','DKK','USD','EUR')

var = StringVar()
combobox = ttk.Combobox(window, textvariable = var)
combobox['values'] = currency
combobox['state'] = 'readonly'
combobox.pack(fill='x',padx= 5, pady=5)

entry = ttk.Entry()
entry.pack(fill='x',padx= 6, pady=6)
label = ttk.Label()
label.pack(fill='x',padx= 5, pady=5)

text = ttk.Label()
text.pack(fill='x',padx= 5, pady=5)
text['text'] = 'Курс на завтра:'


title = ttk.Label()
title.pack(fill='x',padx= 5, pady=5)

button = Button(window, text = 'Расчет', command = calcvalue)
button.pack()



window.mainloop()