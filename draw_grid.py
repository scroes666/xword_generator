# import tkinter as tk
#
#
# class GridApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Grid Display")
#
#         # Create a 15x15 grid of Entry widgets
#         self.entries = [[None] * 15 for _ in range(15)]
#         for i in range(15):
#             for j in range(15):
#                 self.entries[i][j] = tk.Entry(master, width=3)
#                 self.entries[i][j].grid(row=i, column=j)
#
#         # Add a button to print the filled-in grid
#         self.print_button = tk.Button(master, text="Print Grid", command=self.print_grid)
#         self.print_button.grid(row=15, columnspan=15)
#
#     def print_grid(self):
#         grid_values = [[entry.get() for entry in row] for row in self.entries]
#         for row in grid_values:
#             print(" ".join(row))
#
#
# def main():
#     root = tk.Tk()
#     app = GridApp(root)
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()
