#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import Text, Listbox, Menu, Canvas
from tkinter import ttk
from tkinter.ttk import Button, Label, Entry, Checkbutton, Radiobutton, Frame, Combobox, Scrollbar, Treeview, Scale, Spinbox, Notebook, Style
from tkinter import messagebox

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..\\..\\")

from resources.view.window import window_def


'''
    Button — кнопка; 12
    Label — текстовая метка; 1
    Entry — однострочное текстовое поле; 1
    Text — многострочное текстовое поле; 1
    Checkbutton — флажок; 1
    Radiobutton — переключатель или радиокнопка; 1
    Frame — фрейм, который организует виджеты в группы; 1
    Listbox — список; 1
    Combobox — выпадающий список; 1
    Menu — элемент меню; 1
    Scrollbar — полоса прокрутки; 1
    Treeview — позволяет создавать древовидные и табличные элементы; 1
    Scale — текстовая метка; 1
    Spinbox — список значений со стрелками для перемещения по элементам; 1
    ProgressBar — текстовая метка; 1
    Canvas — «холст», на котором рисуют графические фигуры; 2
    Notebook — панель вкладок. 1
'''


class elements (window_def):

    width = 350
    title = "GUI"

    __radio = {
        "radio_1": "radio-1",
        "radio_2": "radio-2"
    }


    __combobox = [
        "combobox-1",
        "combobox-2"
    ]

    i = 0


    def get_frame(self, parent_frame, height=20):
        frame = Frame(parent_frame, height=height, width=self.width)
        frame.pack_propagate(0) # don't shrink
        frame.grid(column=0, row=self.i, padx=5, pady=5)
        self.i = self.i + 1
        return frame



    @window_def._decorator_gui2
    def gui2(self, frame):

        frame_el = self.get_frame(frame)

        l_result = Label(frame_el, text="")
        l_result.grid(column=0, row=0, padx=2, pady=2)
        l_result.pack(fill=BOTH, expand=1, padx=0)



        frame_el = self.get_frame(frame, height=30)

        btn = Button(frame_el, text="Запустить", command=lambda: self.button_action())
        btn.grid(column=0, row=0, padx=2, pady=2)
        btn.pack(fill=BOTH, expand=1, padx=0)



        frame_el = self.get_frame(frame)

        w = Label(frame_el, text="Label")
        w.grid(column=0, row=0, padx=2, pady=2)
        w.pack(fill=BOTH, expand=1, padx=0)



        frame_el = self.get_frame(frame)

        w = Entry(frame_el)
        w.grid(column=0, row=0, padx=2, pady=2)
        w.pack(fill=BOTH, expand=1, padx=0)



        cb_var = IntVar()

        frame_el = self.get_frame(frame)

        w = Checkbutton(frame_el, text="Checkbutton", state=ACTIVE, variable=cb_var, offvalue=0, onvalue=1)
        w.grid(column=0, row=0, padx=2, pady=2)
        w.pack(fill=BOTH, expand=1, padx=0)



        radio_var = StringVar(value="radio_2")

        frame_el = self.get_frame(frame)

        r_header = Label(frame_el, text="Выберите radio")
        r_header.grid(column=0, row=0, padx=2, pady=2)
        r_header.pack(fill=BOTH, expand=1, padx=0)

        for key in self.__radio:
            frame_el = self.get_frame(frame)

            w = Radiobutton(frame_el, text=self.__radio[key], value=key, variable=radio_var, command=lambda: self.print_action(l_result, radio_var.get()))
            w.grid(column=0, row=0, padx=2, pady=2)
            w.pack(fill=BOTH, expand=1, padx=0)



        frame_el = self.get_frame(frame)

        cb_header = Label(frame_el, text="Выберите combobox")
        cb_header.grid(column=0, row=0, padx=2, pady=2)
        cb_header.pack(fill=BOTH, expand=1, padx=0)

        frame_el = self.get_frame(frame)

        combobox = Combobox(frame_el, values=self.__combobox)
        combobox.set(self.__combobox[1])
        combobox.grid(column=0, row=0, padx=2, pady=2)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        combobox.bind("<<ComboboxSelected>>", lambda event: self.print_action(l_result, combobox.get()))


        frame_el = self.get_frame(frame)

        tr_header = Label(frame_el, text="Дерево")
        tr_header.grid(column=0, row=0, padx=2, pady=2)
        tr_header.pack(fill=BOTH, expand=1, padx=0)

        frame_el = self.get_frame(frame, height=100)

        tree = Treeview(frame_el, show="tree headings", selectmode="browse")
        tree.pack(fill=BOTH, expand=1, padx=0)
        tree.bind("<<TreeviewSelect>>", lambda event: self.print_action(l_result, tree.item(tree.selection()[0])))

        tree.heading("#0", text="Отделы", anchor=NW)

        tree.insert("", END, iid=1, text="Административный отдел", open=True)
        tree.insert("", END, iid=2, text="IT-отдел", open=True)
        tree.insert("", END, iid=3, text="Отдел продаж")

        tree.insert(1, index=END, text="Tom")
        tree.insert(2, index=END, text="Bob")
        ind = tree.insert(2, index=END, text="Sam")
        tree.insert(ind, index=END, text="Sam 1")
        tree.insert(ind, index=END, text="Sam 2")

        scrollbar = Scrollbar(tree, orient="vertical", command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree["yscrollcommand"]=scrollbar.set


        frame_el = self.get_frame(frame)

        tab_header = Label(frame_el, text="Таблица")
        tab_header.grid(column=0, row=0, padx=2, pady=2)
        tab_header.pack(fill=BOTH, expand=1, padx=0)

        frame_el = self.get_frame(frame, height=150)

        # определяем данные для отображения
        people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]

        # определяем столбцы
        columns = ("name", "age", "email")

        table = Treeview(frame_el, columns=columns, show="headings", selectmode="browse")
        table.pack(fill=BOTH, expand=1, padx=0)
        table.bind("<<TreeviewSelect>>", lambda event: self.print_action(l_result, table.item(table.selection()[0])))

        # определяем заголовки
        table.heading("name", text="Имя", anchor=W, command=lambda: self.sort(0, False, table))
        table.heading("age", text="Возраст", anchor=W, command=lambda: self.sort(1, False, table))
        table.heading("email", text="Email", anchor=W, command=lambda: self.sort(2, False, table))

        table.column("#1", stretch=True, width=100)
        table.column("#2", stretch=True, width=100)
        table.column("#3", stretch=True, width=200)

        scrollbar = Scrollbar(table, orient="horizontal", command=table.xview)
        scrollbar.pack(side=BOTTOM, fill=X)
        table["xscrollcommand"]=scrollbar.set

        # добавляем данные
        for person in people:
            table.insert("", END, values=person)


        window = self.get_window(frame)
        window.option_add("*tearOff", FALSE) # Отключаем пунктирную линию в меню

        settings_menu = Menu()
        settings_menu.add_command(label="Save", command=lambda: self.menu_click("Save"))
        settings_menu.add_command(label="Open", command=lambda: self.menu_click("Open"))

        file_menu = Menu()
        file_menu.add_cascade(label="Settings", menu=settings_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=lambda: self.menu_click("Exit"))

        main_menu = Menu()

        main_menu.add_cascade(label="File", menu=file_menu)
        main_menu.add_cascade(label="Settings", menu=settings_menu)
        main_menu.add_cascade(label="Edit", command=lambda: self.menu_click("Edit"))
        main_menu.add_cascade(label="View", command=lambda: self.menu_click("View"))

        window.config(menu=main_menu)

    def sort(self, col, reverse, tree):
        # получаем все значения столбцов в виде отдельного списка
        l = [(tree.set(k, col), k) for k in tree.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index,  (_, k) in enumerate(l):
            tree.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        tree.heading(col, command=lambda: self.sort(col, not reverse, tree))

    def print_action(self, r_header, text=''):
        r_header.config(text=f"Выбран {text}")
        print(text)

    def menu_click(self, text):
        messagebox.showinfo("GUI Python", f"Нажат пункт меню {text}")

if __name__ == "__main__":
    index = elements()
    index.gui()
