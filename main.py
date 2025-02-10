#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Frame, Button
import importlib
from functools import partial
from resources.view.window import window_def



class index (window_def):

    __dict_menu = {}

    width = 200
    title = "pyScript"

    ''' Загружает настройки формы '''
    def load_cfg(self, cfg_file_name):
        data=self.load_cfg_json(cfg_file_name)

        key = "menu"
        if key in data:
            self.__dict_menu=data["menu"]


    ''' Формирует форму GUI '''
    def gui2(self, frame):

        self.load_cfg("cfg/main.json")
        self.load_cfg("cfg/___main.json")


        # Динамический фрайм
        frame_main = Frame(frame, width=1, relief=SOLID, borderwidth=0)
        frame_main.pack_propagate(0)
        frame_main.grid(column=1, row=0, sticky="n")

        # Месторасположения кнопок
        frame_menu = Frame(frame, width=150)
        frame_menu.grid(column=0, row=0, sticky="n")

        # Кнопки меню
        i = 1
        for key in self.__dict_menu:
            frame_text_btn = Frame(frame_menu, height=30, width=self.width)
            frame_text_btn.pack_propagate(0)
            frame_text_btn.grid(column=0, row=i, pady=3, padx=6)

            # partial - что бы помнить уникальные ключи для каждой кнопки
            btn = Button(frame_text_btn, text=self.__dict_menu[key]["title"], command=partial (self.click_btn_menu, key, frame_main))
            btn.pack(fill=BOTH, expand=1)
            i += 1

        return

    ''' Отработка нажатия кнопки (динамическая) '''
    def click_btn_menu(self, key, frame):
        print(self.__class__.__name__ + ": click_menu: " + key)
        # Очищаем динамичный фрайм
        for widget in frame.winfo_children():
            widget.destroy()
        # Получаем новый модуль
        module_name = self.__dict_menu[key]["module"] + "." + self.__dict_menu[key]["class"]
        # Подгружаем модуль
        obj_module = importlib.import_module(module_name)
        my_class = getattr(obj_module, self.__dict_menu[key]["class"])
        my_instance = my_class()
        # Обновляем вид
        my_instance.gui2(frame)
        print(self.__class__.__name__ + ": fin_click_menu")



if __name__ == "__main__":
    index = index()
    index.gui()
