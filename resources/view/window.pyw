#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Frame, Button
import json



class window_def:

    width = 200
    title = "Имя не указано"

    def load_cfg_json(self, cfg_file_name):
        print(self.__class__.__name__ + ": load json: " + cfg_file_name)
        try:
            with open(cfg_file_name, encoding="utf-8") as file:
                data = json.load(file)
        except:
            data = {}

        return data



    def get_window(self, element):
        return element.winfo_toplevel()



    def gui(self):
        print(self.__class__.__name__ + ': open window')
        # Главное окно
        window = Tk()
        window.title(self.title)
        window.resizable(width=False, height=False)

        # Главный фрайм
        frame_main = Frame(window, height=30, width=self.width)
        frame_main.pack_propagate(0)
        frame_main.grid(column=0, row=0, padx=2, pady=2)

        # Содержимое окна
        self.gui2(frame_main)

        # Местоположение кнопки выхода
        frame_exit_btn = Frame(window, height=30, width=self.width)
        frame_exit_btn.pack_propagate(0)
        frame_exit_btn.grid(column=0, row=1, padx=1, pady=10)

        # Кнопка выхода
        exit_btn = Button(frame_exit_btn, text="Выход", command=window.destroy)
        exit_btn.grid(column=0, row=0, padx=0, pady=0)
        exit_btn.pack(fill=BOTH, expand=True)

        window.mainloop()
        print(self.__class__.__name__ + ': close window') #  + type(self).__name__
        return

    def gui2(self, frame):
        return



if __name__ == "__main__":
    index = adm_script()
    index.gui()
