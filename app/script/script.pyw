#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import Frame, Button, Style, Combobox, Scrollbar
import importlib
import json

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..\\..\\")

from resources.view.window import window_def



class script (window_def):

    width = 200
    title = "Запуск сценариев"

    __listbox_script_set = {
        "Тестовый сценарий": {"module": "scripts.test.script_test", "class": "script_test"},
    }

    __combobox_geo = {
        "Москва": {"lat": "55.753767", "lng": "37.620556"},
    }

    __combobox_size = {
        "Базовый": {"w": "1024", "h": "800"},
        "Мобильный": {"w": "360", "h": "760"},
        "Bootstrap xs": {"w": "368", "h": "800"},
        "Bootstrap sm": {"w": "580", "h": "800"},
        "Bootstrap md": {"w": "770", "h": "800"},
        "Bootstrap lg": {"w": "1000", "h": "800"},
        "Bootstrap xl": {"w": "1210", "h": "800"},
        "Bootstrap xxl": {"w": "1410", "h": "800"},
        "Максимальный": {"type": "max"}
    }

    __combobox_host = {
        "ya.ru": {
          "protocol": "https",
          "login": "",
          "password": "",
          "host": "ya.ru",
          "port": ""
        },
        "google.com": {
          "protocol": "https",
          "login": "",
          "password": "",
          "host": "google.com",
          "port": ""
        }
    }

    form_field={}


    ''' Отображает json настроек для старта сценария '''
    def view_start_set(self):
#        self.form_field["start_report"].config(text=json.dumps(self.create_set_start(), indent = 4))
        self.form_field["start_report"]["state"] = NORMAL
        self.form_field["start_report"].delete("1.0", END)
        self.form_field["start_report"].insert(END, json.dumps(self.create_set_start(), indent = 4))
        self.form_field["start_report"]["state"] = DISABLED


    ''' Фомирует json настроек для старта сценария '''
    def create_set_start(self):
        set_start={
            "platform": {},
            "browser": {},
        }

        set_start["browser"]["type"]="firefox"

        combobox=self.form_field["host"]
        key=combobox.get()
        set_start["platform"]["host"]=self.__combobox_host[key]

        combobox=self.form_field["size"]
        key=combobox.get()
        if key in self.__combobox_size:
            set_start["browser"]["size"]=self.__combobox_size[key]

        combobox=self.form_field["geo"]
        key=combobox.get()
        if key in self.__combobox_geo:
            set_start["browser"]["geo"]=self.__combobox_geo[key]

        return set_start


    ''' Запускает выполнение сценария '''
    def start_action(self):
        listbox_script_set=self.form_field["script_set"]
        ind = listbox_script_set.curselection()
        key = listbox_script_set.get(ind)

        set_start = self.create_set_start()
        print()
        print('set_start create:')
        print(set_start)

        module_name = self.__listbox_script_set[key]["module"]
        # Подгружаем модуль
        obj_module = importlib.import_module(module_name)
        my_class = getattr(obj_module, self.__listbox_script_set[key]["class"])
        my_instance = my_class(set_start=set_start)
        # Обновляем вид
        my_instance.run()


    ''' Загружает настройки формы '''
    def load_cfg(self, cfg_file_name):

        data=self.load_cfg_json(cfg_file_name)

        key = "hosts"
        if key in data:
            self.__combobox_host=data["hosts"]

        key = "geo"
        if key in data:
            self.__combobox_geo=data["geo"]

        key = "script_set"
        if key in data:
            self.__listbox_script_set=data["script_set"]


    ''' Обновление настроек формы (перезагрузка формы) '''
    def update_set_form(self):

        self.gui2(self.form_field["frame_main"])


    ''' Формирует форму GUI '''
    def gui2(self, frame_main):

        self.form_field["frame_main"]=frame_main

        self.load_cfg("cfg/script.json")
        self.load_cfg("cfg/___script.json")



        frame_el_left = self.get_frame(frame_main, col=0, row=0, height=300, width=self.width)
        frame_el_right = self.get_frame(frame_main, col=1, row=0, height=300, width=self.width)
        frame_el_right_2 = self.get_frame(frame_main, col=2, row=0, height=300, width=self.width)
        frame_el_bottom = self.get_frame(frame_main, col=0, row=1, height=300, width=self.width, spancol=3)



        frame_el = self.get_frame(frame_el_right, col=0, row=0, height=20, width=self.width)

        cb_header = Label(frame_el, text="Сценарий")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_right, col=0, row=2, height=340, width=self.width)

        upload_set_keys = list(self.__listbox_script_set.keys())
        upload_set_var = Variable(value=upload_set_keys)
        listbox_script_set = Listbox(frame_el, listvariable=upload_set_var)
        listbox_script_set.configure(exportselection=False) # Чтобы фокус не слетал
        listbox_script_set.select_set(0, 0)
        listbox_script_set.grid(column=0, row=0, padx=5, pady=5)
        listbox_script_set.pack(fill=BOTH, expand=1)
        listbox_script_set.bind("<<ListboxSelect>>", lambda event: self.view_start_set())

        self.form_field["script_set"]=listbox_script_set



        frame_el = self.get_frame(frame_el_left, col=0, row=0, height=20, width=self.width)

        cb_header = Label(frame_el, text="Площадка")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_left, col=0, row=1, height=20, width=self.width)

        combobox_key_list=list(self.__combobox_host.keys())
        combobox_var = StringVar(value=combobox_key_list[0])

        combobox = Combobox(frame_el, values=combobox_key_list)
        combobox.set(combobox_key_list[0])
        combobox.grid(column=0, row=0, padx=2, pady=2)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        combobox.bind("<<ComboboxSelected>>", lambda event: self.view_start_set())

        self.form_field["host"]=combobox



        frame_el = self.get_frame(frame_el_left, col=0, row=2, height=20, width=self.width)

        cb_header = Label(frame_el, text="Размер окна браузера")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_left, col=0, row=3, height=20, width=self.width)

        combobox_key_list=list(self.__combobox_size.keys())
        combobox_var = StringVar(value=combobox_key_list[0])

        combobox = Combobox(frame_el, values=combobox_key_list)
        combobox.set(combobox_key_list[0]) # = Combobox(frame_el_el, textvariable=combobox_var, values=combobox_key_list)
        combobox.grid(column=0, row=0, padx=2, pady=2)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        combobox.bind("<<ComboboxSelected>>", lambda event: self.view_start_set())

        self.form_field["size"]=combobox



        frame_el = self.get_frame(frame_el_left, col=0, row=4, height=20, width=self.width)

        cb_header = Label(frame_el, text="Геолокация")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_left, col=0, row=5, height=20, width=self.width)

#        combobox_var = StringVar(value=self.__combobox_geo[1])
        combobox_key_list=list(self.__combobox_geo.keys())
        combobox = Combobox(frame_el, values=combobox_key_list)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        combobox.bind("<<ComboboxSelected>>", lambda event: self.view_start_set())

        self.form_field["geo"]=combobox
#        combobox.bind("<<ComboboxSelected>>", lambda event: self.combobox_select(cb_header, combobox_var))



        frame_el_empty = self.get_frame(frame_el_left, col=0, row=6, height=170, width=self.width)



        frame_el = self.get_frame(frame_el_right_2, col=0, row=0, height=20, width=self.width*2)

        cb_header = Label(frame_el, text="Параметры запуска")
        cb_header.place(x=0, y=0)

        frame_el_text = self.get_frame(frame_el_right_2, col=0, row=1, height=340, width=self.width*2)

        editor = Text(frame_el_text, height=20, width=47, wrap="none", state=DISABLED)
        editor.grid(column = 0, row = 0, sticky = NSEW) #.pack(fill=BOTH, expand=1)

        scrollbar_y = Scrollbar(frame_el_text, orient="vertical", command=editor.yview)
        scrollbar_y.grid(column = 1, row = 0, sticky = NS)
        editor["yscrollcommand"] = scrollbar_y.set

        scrollbar_x = Scrollbar(frame_el_text, orient="horizontal", command=editor.xview)
        scrollbar_x.grid(column = 0, row = 1, sticky = EW)
        editor["xscrollcommand"] = scrollbar_x.set

        self.form_field["start_report"] = editor


        frame_el = self.get_frame(frame_el_left, col=0, row=11, height=30, width=self.width)

        btn = Button(frame_el, text="Обновить настройки", command=lambda: self.update_set_form())
        btn.grid(column=0, row=0, padx=2, pady=2)
        btn.pack(fill=BOTH, expand=1, padx=0)


        frame_el = self.get_frame(frame_el_bottom, col=0, row=1, height=30, width=self.width * 2)

        btn = Button(frame_el, text="Запустить", command=lambda: self.start_action())
        btn.grid(column=0, row=0, padx=2, pady=2)
        btn.pack(fill=BOTH, expand=1, padx=0)

        return


    ''' Типовой метод создания frame для элементов '''
    def get_frame(self, parent_frame, col, row, width=100, height=20, spanrow=1, spancol=1):
#        frame = Frame(parent_frame, height=height, width=width, relief=SOLID, borderwidth=0)
        frame = Frame(parent_frame, height=height, width=width)
        frame.pack_propagate(0) # don't shrink
        frame.grid(column=col, row=row, padx=3, pady=3, rowspan=spanrow, columnspan=spancol)
        return frame


if __name__ == "__main__":
    index = adm_script()
    index.gui()
