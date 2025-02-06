from tkinter import *
from tkinter.ttk import Frame, Button, Style, Combobox
import importlib

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..\\..\\")

from scenarios._set._project import ProjectTest, ProjectSet, FirefoxEnv
from resources.view.window import window_def



class scenario (window_def):

    width = 200
    title = "Запуск сценариев"

    __listbox_scenario_set = {
        "Тестовый сценарий": {"module": "app.mealty._test_m", "class": "index_Test"},
    }

    __combobox_geo = {
        "Москва": {"lat": "55.753767", "lng": "37.620556"},
    }

    __combobox_size = {
        "Средний": {"size": "mid"},
        "Мобильный": {"size": "sm"},
        "Максимальный": {"size": "max"}
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

    form_feald={}


    def start_driver(self):
        self.gui()
        return

    def tttt(self):
        self.form_feald["start_report"].config(text=json.dumps(self.create_set_start(), indent = 4))
        self.form_feald["start_report"].pack(fill="both")

    def listbox_scenario_set(self):
        listbox_scenario_set=self.form_feald["scenario_set"]
        ind = listbox_scenario_set.curselection()
        key = listbox_scenario_set.get(ind)
        self.form_feald["scenario_set_var"].config(text=key)


    def create_set_start(self):
        set_start={
            "platform": {},
            "browser": {},
        }
        combobox=self.form_feald["host"]
        key=combobox.get()
        set_start["platform"]["host"]=self.__combobox_host[key]

        combobox=self.form_feald["size"]
        key=combobox.get()
        if key in self.__combobox_size:
            set_start["browser"]["size"]=self.__combobox_size[key]

        combobox=self.form_feald["geo"]
        key=combobox.get()
        if key in self.__combobox_geo:
            set_start["browser"]["geo"]=self.__combobox_geo[key]
        print(set_start)
        return set_start


    def start_action(self):
        listbox_scenario_set=self.form_feald["scenario_set"]
        ind = listbox_scenario_set.curselection()
        key = listbox_scenario_set.get(ind)
        factory_env = FirefoxEnv()
        set_start = self.create_set_start()
        factory_env.set = set_start["browser"]
        env = factory_env.get()
#        my_instance = getattr(self.__listbox_scenario_set[key]["module"], self.__listbox_scenario_set[key]["class"])(test_env=env, set_start=set_start["platform"])
#        my_instance.run()
        module_name = self.__listbox_scenario_set[key]["module"] # + "." + self.__listbox_scenario_set[key]["class"]
        # Подгружаем модуль
        obj_module = importlib.import_module(module_name)
        my_class = getattr(obj_module, self.__listbox_scenario_set[key]["class"])
        my_instance = my_class(test_env=env, set_start=set_start["platform"])
        # Обновляем вид
        my_instance.run()


    def load_cfg(self):
        data=self.load_cfg_json("cfg/scenario.json")

        key = "host"
        if key in data:
            self.__combobox_host=data["hosts"]
        key = "geo"
        if key in data:
            self.__combobox_geo=data["geo"]
        key = "scenario_set"
        if key in data:
            self.__listbox_scenario_set=data["scenario_set"]


    def gui2(self, frame_main):

        self.load_cfg()



        frame_el_left = self.get_frame(frame_main, col=0, row=0, height=300, width=self.width)
        frame_el_right = self.get_frame(frame_main, col=1, row=0, height=300, width=self.width)
        frame_el_bottom = self.get_frame(frame_main, col=0, row=1, height=300, width=self.width, spancol=2)



        frame_el = self.get_frame(frame_el_right, col=0, row=0, height=20, width=self.width)

        cb_header = Label(frame_el, text="Сценарий")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_right, col=0, row=2, height=300, width=self.width)

        upload_set_keys = list(self.__listbox_scenario_set.keys())
        upload_set_var = Variable(value=upload_set_keys)
        listbox_scenario_set = Listbox(frame_el, listvariable=upload_set_var)
        listbox_scenario_set.configure(exportselection=False) # Чтобы фокус не слетал
        listbox_scenario_set.select_set(0, 0)
        listbox_scenario_set.grid(column=0, row=0, padx=5, pady=5)
        listbox_scenario_set.pack(fill=BOTH, expand=1)
        listbox_scenario_set.bind("<<ListboxSelect>>", lambda event: self.tttt())

        self.form_feald["scenario_set"]=listbox_scenario_set



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
        self.form_feald["host"]=combobox



        frame_el = self.get_frame(frame_el_left, col=0, row=2, height=20, width=self.width)

        cb_header = Label(frame_el, text="Размер окна Браузера")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_left, col=0, row=3, height=20, width=self.width)

        combobox_key_list=list(self.__combobox_size.keys())
        combobox_var = StringVar(value=combobox_key_list[0])

        combobox = Combobox(frame_el, values=combobox_key_list)
        combobox.set(combobox_key_list[0]) # = Combobox(frame_el_el, textvariable=combobox_var, values=combobox_key_list)
        combobox.grid(column=0, row=0, padx=2, pady=2)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        self.form_feald["size"]=combobox



        frame_el = self.get_frame(frame_el_left, col=0, row=4, height=20, width=self.width)

        cb_header = Label(frame_el, text="Геолокация")
        cb_header.place(x=0, y=0)

        frame_el = self.get_frame(frame_el_left, col=0, row=5, height=20, width=self.width)

#        combobox_var = StringVar(value=self.__combobox_geo[1])
        combobox_key_list=list(self.__combobox_geo.keys())
        combobox = Combobox(frame_el, values=combobox_key_list)
        combobox.pack(fill=BOTH, expand=1, padx=0)
        self.form_feald["geo"]=combobox
 #       combobox.bind("<<ComboboxSelected>>", lambda event: self.combobox_select(cb_header, combobox_var))



        frame_el_empty = self.get_frame(frame_el_left, 0, 10, width=self.width, height=170)
        cb_header = Label(frame_el_empty, text="Параметры запуска:", anchor="w", justify="left")
        cb_header.place(x=5, y=5)
        self.form_feald["start_report"]=cb_header


        frame_el = self.get_frame(frame_el_bottom, col=0, row=1, height=30, width=self.width * 2)

        btn = Button(frame_el, text="Запустить", command=lambda: self.start_action())
        btn.grid(column=0, row=0, padx=2, pady=2)
        btn.pack(fill=BOTH, expand=1, padx=0)

        return


    def get_frame(self, parent_frame, col, row, width=100, height=20, spanrow=1, spancol=1):
#        frame = Frame(parent_frame, height=height, width=width, relief=SOLID, borderwidth=0)
        frame = Frame(parent_frame, height=height, width=width)
        frame.pack_propagate(0) # don't shrink
        frame.grid(column=col, row=row, padx=3, pady=3, rowspan=spanrow, columnspan=spancol)
        return frame


if __name__ == "__main__":
    index = adm_script()
    index.gui()
