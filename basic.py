# BASIC GUI APP

import tkinter as tk

root = tk.Tk()
root.title("Basic GUI App")
root.geometry("400x600")
root.iconbitmap("python_18894.ico")
root.config(bg="lightblue")

label1 = tk.Label(root, text="Programming Languages")
label1.config (bg="pink", fg = "red", font=("Arial", 20),
            relief = "groove", borderwidth=10,
            pady = 20, padx = 5)
label1.pack()
             

label2 = tk.Label(root, text = "My fav laguange is: ")
label2.config(bg = "blue", fg = "white", font = ("Times-Roman", 15),
              relief = "ridge", borderwidth =2,
              pady = 10, padx = 10)
label2.place(y = 470)   

label3 = tk.Label(root, text= "Pick a language")
label3.config(bg= "grey", fg = "white", font = ("Courier", 15),
              borderwidth = 5, pady = 5, padx = 5, relief = "solid")
label3.place(y = 520)

root.mainloop()

