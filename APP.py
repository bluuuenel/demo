import tkinter as tk
import os
import windnd
from docx import Document
import csv
from nltk import word_tokenize  # 以空格形式实现分词


def read_files(file_path):
    """读取，返回所有文字"""
    doc = Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text


def extract_words(text):
    words = word_tokenize(text)
    interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']  # 定义标点符号列表
    cutwords = [word for word in words if word not in interpunctuations]
    res = []
    for i in cutwords:
        if i.isdigit() or i.lower() in res:
            pass
        else:
            res.append(i.lower())
    print(len(res))
    return res


def write_it(world_list):
    with open(r'eng.txt', 'w') as f:
        for i in world_list:
            f.write(i + '\n')


def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    judge_dir_files = os.path.isdir(msg)
    if judge_dir_files:
        pass
    else:
        pass
    return msg


def apps_():
    root = tk.Tk()
    root.geometry('400x200')
    root.title('提词器')
    file_pss = windnd.hook_dropfiles(root, func=dragged_files)
    root.mainloop()


write_it(extract_words(read_files('初中英语200句.docx')))
