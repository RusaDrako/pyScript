from tkinter import *
from tkinter.ttk import Frame, Button



class window_def:

    width = 200
    title = "Имя не указано"

    def gui(self):
        print('open window: ' + type(self).__name__)
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
        print('close window: ' + type(self).__name__)
        return

    def gui2(self, frame):
        return



if __name__ == "__main__":
    index = adm_script()
    index.gui()
