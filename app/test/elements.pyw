from tkinter import *
from tkinter import Text, Listbox, Menu, Canvas
from tkinter import ttk
from tkinter.ttk import Button, Label, Entry, Checkbutton, Radiobutton, Frame, Combobox, Scrollbar, Treeview, Scale, Spinbox, Notebook, Style

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

    width = 200
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



    def print_action(self, r_header, text=''):
        r_header.config(text=f"Выбран {text}")
        print(text)


if __name__ == "__main__":
    index = elements()
    index.gui()
