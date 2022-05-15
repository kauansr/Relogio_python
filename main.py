from datetime import datetime
import tkinter as tk


class Telainicial:
    def __init__(self, master):
        self.nossatela = master
        self.lblrelogio = tk.Label(
            self.nossatela, font=('Arial',26), fg='Purple')
        self.lblrelogio.pack(pady=30,padx=30)
        self.alteracao()


    def alteracao(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.lblrelogio['text'] = now        
        self.nossatela.after(1000,self.alteracao)


janela = tk.Tk()
janela.title('Relógio')
Telainicial(janela)
janela.mainloop()