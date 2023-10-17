import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class TicTacToe():
    def __init__(self):
        self.root = ctk.CTk()
        self.size = 3
        self.char = ''
        self.res_char = ''
        self.width = self.size * 100 + (self.size + 1) * 10
        self.height = self.size * 100 + (self.size + 1) * 10
        self.matrix = []
        self.matrix_image = []
        self.frame = ctk.CTkFrame(self.root, self.width, self.height)
        self.frame.pack(pady=5)
        self.run()

    def run(self):
        self.counter = 0

        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        main_menu = tk.Menu(self.root)
        self.root.config(menu=main_menu)

        game_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=lambda: self.new_game())
        game_menu.add_command(label="Exit", command=lambda: self.root.destroy())

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)

        self.root.geometry(f"{self.width}x{self.height}+{int(x)}+{int(y)}")

        self.root.mainloop()

    def new_game(self):
        top_level = tk.Toplevel()
        top_level.title("New Game")
        top_level.width = 400
        top_level.height = 200
        top_level.resizable(False, False)

        screen_width = top_level.winfo_screenwidth()
        screen_height = top_level.winfo_screenheight()
        x = (screen_width / 2) - (top_level.width / 2)
        y = (screen_height / 2) - (top_level.height / 2)
        top_level.geometry(f"{top_level.width}x{top_level.height}+{int(x)}+{int(y)}")

        top_level.first_player = ctk.CTkEntry(top_level, width=200)
        top_level.first_player.place(x=170, y=30)
        ctk.CTkLabel(top_level, text="First Player :", font=("Bold", 16)).place(x=55, y=30),

        top_level.second_player = ctk.CTkEntry(top_level, width=200)
        top_level.second_player.place(x=170, y=70)

        ctk.CTkLabel(top_level, text="Second Player :", font=("Bold", 16)).place(x=30, y=70)

        top_level.info_label = ctk.CTkLabel(top_level, text="Choose one :", font=("Bold", 16)).place(x=50, y=120)

        top_level.char = tk.IntVar()

        tk.Radiobutton(top_level, text="X", variable=top_level.char, value=1, font=("Bold", 15)).place(x=170, y=120)
        tk.Radiobutton(top_level, text="O", variable=top_level.char, value=2, font=("Bold", 15)).place(x=230, y=120)
        top_level.start_game = ctk.CTkButton(top_level, text="Start", font=("Bold", 20),
                                        command=lambda: self.check_questionnaire(top_level)).place(x=130, y=160)

        top_level.mainloop()

    def check_questionnaire(self, top_level):
        try:
            self.fplayer_name = top_level.first_player.get().strip()
            self.splayer_name = top_level.second_player.get().strip()
            choose = top_level.char.get()

            if not (self.fplayer_name != '' and self.splayer_name != '' and choose != ''):
                raise Exception()
            top_level.destroy()

            self.char = {1: 'X', 2: 'O'}[choose]

            for i in range(self.size):
                arr = []
                for j in range(self.size):
                    arr += [self.create_button(i, j)]
                self.matrix_image += [arr]
            self.matrix = [["" for i in range(self.size)] for j in range(self.size)]


            self.run()

        except:
            messagebox.showinfo("Error", "The information was not completely filled out!")

    def create_button(self, row, col):
        btn = ctk.CTkButton(self.frame, (self.width - (self.size + 1) * 10) // self.size,
                            (self.height - (self.size + 1) * 10) // self.size, text="",
                            font=("Bold", 40), border_color="#bbada0",
                            command=lambda: self.validation(row, col))
        btn.grid(row=row, column=col, padx=5, pady=5)

        return btn

    def validation(self, r, c):
        self.matrix[r][c] = 'O' if self.counter & 1 else 'X'
        self.matrix_image[r][c].configure(image=tk.PhotoImage(file=("image/o.png" if self.counter & 1 else "image/cancel.png")), state=tk.DISABLED)

        res = {}
        pos_char = ''

        for i in range(self.size):
            cnt = 1
            pos_char = self.matrix[i][0]
            for j in range(1, self.size):
                if pos_char == self.matrix[i][j] and pos_char != "":
                    cnt += 1
            if cnt == self.size:
                res['row'] = i

        for i in range(self.size):
            cnt = 1
            pos_char = self.matrix[0][i]
            for j in range(1, self.size):
                if pos_char == self.matrix[j][i] and pos_char != "":
                    cnt += 1
            if cnt == self.size:
                res['col'] = i

        cnt = cnt1 = 1
        pos_char1 = self.matrix[0][self.size - 1]
        pos_char = self.matrix[0][0]
        for i in range(1, self.size):
            if pos_char == self.matrix[i][i] and pos_char != "":
                cnt += 1
            if pos_char1 == self.matrix[i][self.size - 1 - i] and pos_char1 != "":
                cnt1 += 1

        res['player'] = pos_char
        if cnt == self.size:
            res['ldig'] = 1
            res['player'] = pos_char
        elif cnt1 == self.size:
            res['rdig'] = 1
            res['player'] = pos_char1

        self.counter += 1
        self.res_char = pos_char

        check = True

        if 'col' in res:
            for i in range(self.size):
                self.matrix_image[i][res['col']].configure(fg_color="red")
        elif 'row' in res:
            for i in range(self.size):
                self.matrix_image[res['row']][i].configure(fg_color="red")
        elif 'ldig' in res:
            for i in range(self.size):
                self.matrix_image[i][i].configure(fg_color="red")
        elif 'rdig' in res:
            for i in range(self.size):
                self.matrix_image[i][self.size - 1 - i].configure(fg_color="red")
            self.res_char = pos_char1
        elif self.counter == 9:
            self.res_char = 'D'
        else:
            check = False

        if check:
            self.block_cells()

    def block_cells(self):
        messagebox.showinfo("Game over", f"{[self.fplayer_name, self.splayer_name][self.char != self.res_char].lower().title()} won the game" if self.res_char != 'D' else "Draw")
        for i in range(self.size):
            for j in range(self.size):
                self.matrix_image[i][j].configure(state=tk.DISABLED)



