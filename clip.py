
import os
import json
import pyperclip
import pysimplegui as sg

ROOT_DIR = os.path.diename(os.path.abspath)
SAVE_FILE = os.path.join(ROOT_DIR,"clipboard-history.json")

MAX_HISTORY = 20

history = []
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE,"r",encoding="utf-8") as f:
        history = json.load(f)

def save_history():
    with open(SAVE_FILE,"w",encoding="utf-8") as f:
        json.dump(history,f,ensure_ascii=False,indent=2)

def list_format(history):
    crlf = lambda v: v.strip().replace("\r","").replace("\n","")