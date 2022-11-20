import ctypes
import tkinter.ttk as ttk
import tkinter as tk


class constants:

    @staticmethod
    def get_verde():
        return '#00e673'

    @staticmethod
    def get_galben():
        return '#ffff00'

    @staticmethod
    def get_gri():
        return '#8e8e8e'

    @staticmethod
    def get_basic():
        return '#f5efe6'

    @staticmethod
    def get_white():
        return 'white'

    @staticmethod
    def get_dict_size():
        return 11454


def init_root():
    root = tk.Tk()
    # icon in taskbar
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('wordle.1.0')
    root.title('Wordle')
    window_width = 600
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # root.geometry('600x400+250+200')
    root.resizable(False, False)
    root.iconbitmap('ico.ico')
    return root


def draw_title(root):
    label = ttk.Label(root, text='WORDLE',  font="Century 18 bold")
    label.place(relx=.5, y=30, anchor='center')
    return label


def draw_letters(root):
    letters = [[0 for _ in range(5)] for _ in range(6)]
    delta = [[(135+(j+1)*48, 30+(i+1)*48)for j in range(5)] for i in range(6)]
    for i in range(6):
        for j in range(5):
            letters[i][j] = ttk.Label(
                root, text=' ',  font="Century 22 bold", borderwidth=1, relief="solid", width=2, background=constants.get_basic())
            letters[i][j].place(
                x=delta[i][j][0], y=delta[i][j][1])
            letters[i][j].config(anchor='center')
    return letters


def draw_tbox(root):
    tbox = tk.Text(root, height=1, width=8, font="Century 22 bold",
                   borderwidth=1, relief="solid")
    tbox.place(x=180, y=385)
    tbox.focus_set()
    return tbox


def draw_submit_btn(root):
    button = tk.Button(root, text="Submit",  height=1, width=6, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=330, y=385)
    return button


def draw_play_again_btn(root):
    button = tk.Button(root, text="Play again",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=35, y=180)
    return button


def draw_help_btn(root):
    button = tk.Button(root, text="Help",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=35, y=230)
    return button


def draw_easy_btn(root):
    button = tk.Button(root, text="Usor↭12",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=450, y=130)
    return button


def draw_normal_btn(root):
    button = tk.Button(root, text="Normal↭6",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=450, y=180)
    return button


def draw_hard_btn(root):
    button = tk.Button(root, text="Greu↭3",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=450, y=230)
    return button


def draw_inf_btn(root):
    button = tk.Button(root, text="∞",  height=1, width=8, font="Century 14 bold",
                       borderwidth=1, relief="solid", bg=constants.get_white())
    button.place(x=450, y=280)
    return button


def color_boxes(letters, line, st, ans):
    bif = []
    afis = [0 for _ in range(5)]
    for i in range(5):
        if ans[i] == st[i]:
            bif.append(i)
            letters[line][i].config(background=constants.get_verde())
            afis[i] = 2
    for i in bif:
        st = st[:i]+'`'+st[i+1:]
        ans = ans[:i]+'~'+ans[i+1:]
    for i in range(5):
        for j in range(5):
            if st[i] == ans[j]:
                ans = ans[:j]+'~'+ans[j+1:]
                st = st[:i]+'`'+st[i+1:]
                letters[line][i].config(background=constants.get_galben())
                afis[i] = 1
                break

    for i in range(5):
        if st[i].isalpha():
            letters[line][i].config(background=constants.get_gri())

    pipe = open('pipe.txt', 'a')
    for i in afis:
        pipe.write(str(i))
    pipe.write('\n')

    return letters
