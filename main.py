#!/usr/bin/env python3
from urllib import parse
from tkinter import *
import pyclip
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("intent")
args = parser.parse_args()
intent = args.intent

liste = intent.split(";")

res = {}
i = 0
for item in liste:
     i = i + 1
     if "=" in item:
          key, value = item.split("=")
          res[key] = value
     else:
          res[i] = item


query = parse.parse_qs(parse.urlsplit(parse.unquote(res["S.link"])).query)

main = Tk()
main.title("Firebase reCAPTCHA token")
T = Text(main)
m = Menu(main, tearoff=0)
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

T.bind("<Button-3>", do_popup)
T.pack()
T.insert(END, query["recaptchaToken"][0])

def copy_selection():
    pyclip.copy(T.selection_get())

m.add_command(label="Copy", command=copy_selection)

mainloop()
