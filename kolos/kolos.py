import tkinter as tk
import pandas as pd

class InterfejsGUI(tk.Tk):

  def __init__(self,*args,**kwargs):
    try:
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("Titanic")
        self.geometry("1000x800")
        self.klasa = tk.IntVar(self)
        self.ch_first = tk.Radiobutton(self, text="Klasa 1", value=1, variable=self.klasa)
        self.ch_second = tk.Radiobutton(self, text="Klasa 2", value=2, variable=self.klasa)
        self.ch_third = tk.Radiobutton(self, text="Klasa 3", value=3, variable=self.klasa)
        self.ok_btn = tk.Button(self, text="Ok", command=self.process)

        self.ch_first.pack()
        self.ch_second.pack()
        self.ch_third.pack()
        self.ok_btn.pack()

        self.table = pd.read_excel("titanic_train.xlsx")
    except FileNotFoundError:
      print("Błąd: plik nie został znaleziony")
    except Exception as e:
      print(f"Nieoczekiwany błąd: {e}")

  def process(self):
    df:pd.DataFrame = self.table[self.table["Pclass"] == self.klasa & self.table["Age"] > 20]
    print(df)

tit = InterfejsGUI()
tit.mainloop()