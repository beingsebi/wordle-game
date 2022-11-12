import constants
import tkinter as tk
from tkinter import messagebox
import tools
import db_tools
from random import choice as rand_word
from os import system as fsys


all_words = db_tools.get_all_words(db_tools.disk_db())
root = tools.init_root()
title = tools.draw_title(root)
letters = tools.draw_letters(root)
tbox = tools.draw_tbox(root)
submit_btn = tools.draw_submit_btn(root)
play_again_btn = tools.draw_play_again_btn(root)
help_btn = tools.draw_help_btn(root)
easy_btn = tools.draw_easy_btn(root)
normal_btn = tools.draw_normal_btn(root)
hard_btn = tools.draw_hard_btn(root)
inf_btn = tools.draw_inf_btn(root)


line = answer = 0
dif_limit = 6


def init_game():
    pipe = open('pipe.txt', 'w')
    pipe.write('')
    easy_btn.config(state=tk.NORMAL)
    normal_btn.config(state=tk.NORMAL)
    hard_btn.config(state=tk.NORMAL)
    inf_btn.config(state=tk.NORMAL)
    global line, answer
    line = 0
    answer = rand_word(all_words)

    ###################################################
    # answer = 'CAIET'
    ##########  your desired existing answer ##########
    ###################################################

    # print(answer)

    for i in range(6):
        for j in range(5):
            letters[i][j].config(text='', background=constants.basic)
    if dif_limit == 3:
        for i in range(3, 6):
            for j in range(5):
                letters[i][j].config(background=constants.gri)


def handler_submit():
    global line, letters
    st = tbox.get("1.0", "end-1c").upper()

    if not st.isalpha():
        messagebox.showwarning(
            'Caractere invalide', 'Ati introdus caractere invalide')
        return None
    if len(st) != 5:
        messagebox.showwarning(
            'Lungime invalida', 'Cuvantul introdus trebuie sa aiba 5 litere')
        return None
    if (st not in all_words):
        messagebox.showwarning(
            'Cuvant invalid', 'Acesta nu este un cuvant valid')
        return None
    easy_btn.config(state=tk.DISABLED)
    normal_btn.config(state=tk.DISABLED)
    hard_btn.config(state=tk.DISABLED)
    inf_btn.config(state=tk.DISABLED)
    pipe = open('pipe.txt', 'a')
    pipe.write(st+'\n')
    if line < 6:
        for i in range(5):
            letters[line][i].config(text=f'{st[i]}')
        letters = tools.color_boxes(letters, line, st, answer)
    else:
        for i in range(5):
            for j in range(5):
                letters[i][j].config(
                    background=letters[i+1][j]['background'], text=letters[i+1][j]['text'])
        for i in range(5):
            letters[5][i].config(text=f'{st[i]}')
        letters = tools.color_boxes(letters, 5, st, answer)
    tbox.delete('1.0', tk.END)
    pipe = open('pipe.txt', 'a')
    if st == answer:
        messagebox.showinfo(
            'Victorie!', f'{answer}! CORECT! Ati castigat din {line+1} incercari!')
        init_game()
        return None
    line += 1

    if line == dif_limit:
        messagebox.showerror(
            'Poate data viitoare', f'Cuvantul corect era {answer}...')
        init_game()
        return None


def press_enter(_):
    st = tbox.get("1.0", "end-1c")[:-1]
    tbox.delete("1.0", "end")
    tbox.insert(tk.END, st)
    handler_submit()


def press_easy():
    global dif_limit
    dif_limit = 12
    easy_btn.config(relief='flat')
    normal_btn.config(relief='solid')
    hard_btn.config(relief='solid')
    inf_btn.config(relief='solid')
    for i in range(6):
        for j in range(5):
            letters[i][j].config(background=constants.basic)


def press_normal():
    global dif_limit
    dif_limit = 6
    easy_btn.config(relief='solid')
    normal_btn.config(relief='flat')
    hard_btn.config(relief='solid')
    inf_btn.config(relief='solid')
    for i in range(6):
        for j in range(5):
            letters[i][j].config(background=constants.basic)


def press_hard():
    global dif_limit
    dif_limit = 3
    easy_btn.config(relief='solid')
    normal_btn.config(relief='solid')
    hard_btn.config(relief='flat')
    inf_btn.config(relief='solid')
    for i in range(3, 6):
        for j in range(5):
            letters[i][j].config(background=constants.gri)


def press_inf():
    global dif_limit
    dif_limit = 2**49
    easy_btn.config(relief='solid')
    normal_btn.config(relief='solid')
    hard_btn.config(relief='solid')
    inf_btn.config(relief='flat')
    for i in range(6):
        for j in range(5):
            letters[i][j].config(background=constants.basic)


def press_help_btn():
    fsys('main1.exe')
    rd = open('write.txt', 'r')
    st = rd.readline()
    tbox.delete('1.0', tk.END)
    tbox.insert(tk.END, st)
    handler_submit()


submit_btn.config(command=handler_submit)
easy_btn.config(command=press_easy)
normal_btn.config(command=press_normal)
hard_btn.config(command=press_hard)
inf_btn.config(command=press_inf)
play_again_btn.config(command=init_game)
help_btn.config(command=press_help_btn)
root.bind('<Return>', press_enter)

init_game()
press_normal()
root.mainloop()
