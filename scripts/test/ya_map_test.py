if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..\\..\\")
# Общий драйвер подключения к БД
from scripts._set._project import ProjectTest, ProjectSet
#from selenium.webdriver.common.keys import Keys

import time





''' Настройки тестов страницы '''
class ya_map (ProjectTest):

    # Путь страницы тестирования
    def_url_path = "maps/"


    def run(self):
        self.host_url.def_url_path=self.def_url_path
        # Страница
        super().run()





if __name__ == '__main__':
    set={"platform": {
             "host": {
                 "protocol": "https",
                 "host": "yandex.ru"
             }
         },
         "browser": {
            "type": "firefox"
            }
        }
    ts = ya_map(set)

    ts.run()
    del ts
