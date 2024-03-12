import tkinter as tk
from tkinter import scrolledtext, StringVar, Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class GraphPlotter:
    def __init__(self, master):
        self.master = master
        master.title("Graph Plotter")

        # Equation entry and plot button
        self.equation_var = StringVar()
        self.equation_entry = ttk.Entry(master, textvariable=self.equation_var, width=40)
        self.equation_entry.grid(row=0, column=0, padx=10, pady=10)

        self.plot_button = ttk.Button(master, text="Plot", command=self.plot_graph)
        self.plot_button.grid(row=0, column=1, padx=10, pady=10)

        # Display area for entered equations
        self.equation_display = scrolledtext.ScrolledText(master, width=50, height=10, wrap=tk.WORD)
        self.equation_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Matplotlib figure for plotting
        self.fig, self.ax = plt.subplots(figsize=(6, 4), tight_layout=True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Resize handling
        master.bind("<Configure>", self.on_resize)

    def plot_graph(self):
        equation = self.equation_var.get()
        if equation:
            self.ax.clear()

            x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

            try:
                y = eval(equation)
                self.ax.plot(x, y, label=equation)
                self.ax.legend()
                self.ax.set_title("Graph Plot")
                self.ax.grid(True)
            except Exception as e:
                self.equation_display.insert(tk.END, f"Error: {e}\n")

            self.equation_display.insert(tk.END, f"{equation}\n")
            self.canvas.draw()

    def on_resize(self, event):
        width = self.master.winfo_width() - 20
        height = self.master.winfo_height() - 250
        self.fig.set_size_inches(width / 100, height / 100)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphPlotter(root)
    root.geometry("800x600")
    root.mainloop()
