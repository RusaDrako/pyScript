if __name__ == "__main__":
    import sys
    sys.path.insert(0, "..\\..\\")
# Общий драйвер подключения к БД
from scenarios._set._project import ProjectTest
# from selenium.webdriver.common.keys import Keys
import time



''' Конкретный тест '''
class scenario_test (ProjectTest):

    url_path = ""

    def run(self):
        super().run()

        return
