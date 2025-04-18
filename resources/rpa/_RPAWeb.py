#!/usr/bin/python
# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


'''Настройки сценария'''
class script_start:

    ENV_DRIVER_FIREFOX='firefox'

    ENV_SIZE_SM='sm'
    ENV_SIZE_MID='mid'
    ENV_SIZE_MAX='max'

    driver = None
    driver_close = True
    host_url=None

    def __init__ (self, start_set={}, driver_close=False):

        print()
        print('script_start start_set:')
        self.driver_close = driver_close

        browser_set=start_set['browser']
        print(browser_set)
        # Запуск браузера
        if browser_set["type"] == self.ENV_DRIVER_FIREFOX:
            print('  Firefox')
            options = Options()
            firefox_profile = FirefoxProfile()
            # Геолокация
            if 'geo' in browser_set:
                print('  Add geo: "lat": ' + browser_set['geo']['lat'] + ', "lng": ' + browser_set['geo']['lng'])
                # set the geolocation preferences
                firefox_profile.set_preference('geo.prompt.testing', True)
                firefox_profile.set_preference('geo.prompt.testing.allow', True)
                firefox_profile.set_preference('geo.provider.network.url', 'data:application/json,{"location": {"lat": ' + browser_set['geo']['lat'] + ', "lng": ' + browser_set['geo']['lng'] + '}, "accuracy": 100.0}')

            options.profile = firefox_profile

            self.driver = webdriver.Firefox(options=options)
            print('  Firefox start')
        else:
            raise Exception("Неизвесный тип драйвера")

        driver=self.get_driver()

        # Устанавливаем размер окна
        if 'size' in browser_set:
            size=browser_set['size']
            key = "w"
            if key in size:
                key = "h"
                if key in size:
                    driver.set_window_size(size["w"], size["h"])

            # Позиция на экране
            driver.set_window_position(0,0)

            # Развернуть на всё окно
            key = "type"
            if key in size:
                driver.maximize_window()


        print("  selenium: " + selenium.__version__)
        print("  Браузер: " + driver.capabilities['browserName'] + " (" + driver.capabilities['browserVersion'] + ")")
        size = driver.get_window_size()
        print("  Размер окна: " + str(size.get("width")) + "x" + str(size.get("height")))

        # Установка url
        key="platform"
        if key in start_set:
            self.host_url = host_url(start_set['platform']['host'])

    def __del__(self):
        # Закрытие браузера
        if self.driver_close == True and self.driver != None:
            self.driver.quit()
        print("")
        print("OK")

    # Возвращает объект браузер
    def get_driver(self):
        return self.driver

    # Возвращает объект url
    def get_host_url(self):
        return self.host_url





''' Настройки ссылки подключения '''
class host_url:

    def_url_protocol = ""
    def_url_login = ""
    def_url_password = ""
    def_url_host = ""
    def_url_port = ""
    def_url_path = ""

    def __init__(self, set_start={}):

        print()
        print(self.__class__.__name__)
        print('  Project connect set_start:')
        print(set_start)

        key = 'protocol'
        if key in set_start:
            self.def_url_protocol=set_start['protocol']
        key = 'login'
        if key in set_start:
            self.def_url_login=set_start['login']
        key = 'password'
        if key in set_start:
            self.def_url_password=set_start['password']
        key = 'host'
        if key in set_start:
            self.def_url_host=set_start['host']
        key = 'port'
        if key in set_start:
            self.def_url_port=set_start['port']

    def set_def_url_path(self, path):
        self.ddef_url_path=path

    ''' Возвращает обрабатываемую ссылку '''
    def get_url(self, with_password=True):
        url = self.def_url_protocol + "://"
        if self.def_url_login and with_password:
            url = url + self.def_url_login + ":" + self.def_url_password + "@"
        url = url + self.def_url_host
        if self.def_url_port:
            url = url + ":" + self.def_url_port
        url = url + "/"
        if self.def_url_path:
            url = url + self.def_url_path
        return url





''' Элементами '''
class ElementScriptSection:

    ''' Возвращает элемент типу и селектору '''
    def get_elem(self, type, selector, parent = None):
        ''' Второй вариант
        if parent == None:
            return self.get_driver().find_element(type, selector)
        return parent.find_element(type, selector)
        '''
        if parent == None: parent = self.get_driver()
        return parent.find_element(type, selector)

    ''' Возвращает массив элементов типу и селектору '''
    def get_elems(self, type, selector, parent = None):
        if parent == None: parent = self.get_driver()
        return parent.find_elements(type, selector)

    ''' Возвращает элемент по атрибуту id '''
    def get_elem_by_id(self, selector, parent = None):
        return self.get_elem(By.ID, selector, parent)

    ''' Возвращает массив элементов по атрибуту id '''
    def get_elems_by_id(self, selector, parent = None):
        return self.get_elems(By.ID, selector, parent)

    ''' Возвращает элемент по атрибуту name '''
    def get_elem_by_name(self, selector, parent = None):
        return self.get_elem(By.NAME, selector, parent)

    ''' Возвращает массив элементов по атрибуту name '''
    def get_elems_by_name(self, selector, parent = None):
        return self.get_elems(By.NAME, selector, parent)

    ''' Возвращает элемент по тэгу '''
    def get_elem_by_tag(self, selector, parent = None):
        return self.get_elem(By.TAG_NAME, selector, parent)

    ''' Возвращает массив элементов по тэгу '''
    def get_elems_by_tag(self, selector, parent = None):
        return self.get_elems(By.TAG_NAME, selector, parent)

    ''' Возвращает элемент по классу '''
    def get_elem_by_class(self, selector, parent = None):
        return self.get_elem(By.CLASS_NAME, selector, parent)

    ''' Возвращает массив элементов по классу '''
    def get_elems_by_class(self, selector, parent = None):
        return self.get_elems(By.CLASS_NAME, selector, parent)

    ''' Возвращает элемент по css '''
    def get_elem_by_css(self, selector, parent = None):
        return self.get_elem(By.CSS_SELECTOR, selector, parent)

    ''' Возвращает массив элементов по css '''
    def get_elems_by_css(self, selector, parent = None):
        return self.get_elems(By.CSS_SELECTOR, selector, parent)

    ''' Возвращает элемент по тексту ссылки '''
    def get_elem_by_link_text(self, selector, parent = None):
        return self.get_elem(By.LINK_TEXT, selector, parent)

    ''' Возвращает массив элементов по тексту ссылки '''
    def get_elems_by_link_text(self, selector, parent = None):
        return self.get_elems(By.LINK_TEXT, selector, parent)

    ''' Возвращает элемент по части текста ссылки '''
    def get_elem_by_partial_link_text(self, selector, parent = None):
        return self.get_elem(By.PARTIAL_LINK_TEXT, selector, parent)

    ''' Возвращает массив элементов по части текста ссылки '''
    def get_elems_by_partial_link_text(self, selector, parent = None):
        return self.get_elems(By.PARTIAL_LINK_TEXT, selector, parent)

    ''' Возвращает элемент по xpath '''
    def get_elem_by_xpath(self, selector, parent = None):
        selector = self.check_xpath(selector, parent)
        return self.get_elem(By.XPATH, selector, parent)

    ''' Возвращает массив элементов по xpath '''
    def get_elems_by_xpath(self, selector, parent = None):
        selector = self.check_xpath(selector, parent)
        return self.get_elems(By.XPATH, selector, parent)


    ''' Возвращает элемент по xpath '''
    def check_xpath(self, selector, parent = None):
        # Если указан родитель
        if parent != None:
            # Поиск всегда от точки родителя
            if selector[0] != ".":
                selector = "." + selector
        return selector


    ''' Возвращает родитель элемента (по количеству уровней)'''
    def get_parent_by_lavel(self, elem, level = 1):
        for i in range(abs(int(level))):
            try:
                elem = elem.find_element(By.XPATH, '..')
            except selenium.common.exceptions.NoSuchElementException:
                return None
                break
        return elem

    ''' Возвращает родитель элемента по тегу '''
    def get_parent_by_tag(self, elem, selector):
        while True:
            elem = elem.find_element(By.XPATH, '..')
            if elem.tag_name == selector:
                return elem
                break
            if elem.tag_name == 'html':
                return None
                break

    ''' Возвращает родитель элемента по xpath '''
    def get_parent_by_xpath(self, elem, selector):
        while True:
            try:
                elem = elem.find_element(By.XPATH, selector)
                return elem
                break
            except selenium.common.exceptions.NoSuchElementException:
                elem = elem.find_element(By.XPATH, '..')
                if elem.tag_name == 'html':
                    return None
                    break


    ''' Возвращает активный элемент '''
    def get_elem_active(self):
        return self.get_driver().switch_to.active_element





''' Действия '''
class ActionScriptSection:

    def_action = None

    ''' Прокручивает страницу к объекту '''
    def scroll_shim(self, passed_in_driver, elem):
        # Высота окна
        w_h = passed_in_driver.execute_script("return document.documentElement.clientHeight")
        # Расположение элемента относительно верхнего угла окна
        top_y = passed_in_driver.execute_script("return arguments[0].getBoundingClientRect().top;", elem)
        # Прокручиваем, только если элемент не в зоне видимости окна
        if top_y >= w_h or top_y <= 0:
            passed_in_driver.execute_script('arguments[0].scrollIntoView(true);', elem)
            passed_in_driver.execute_script("window.scrollBy(0, -120);")
            self.pause(0.5)

    def get_action(self):
        if self.def_action == None:
            driver = self.get_driver()
            self.def_action = ActionChains(driver)
        return self.def_action

    ''' Активирует выполнение заданныой последовательности команд '''
    def action_run(self):
        self.get_action().perform()
        return self

    ''' Задаёт команду паузы '''
    def action_pause(self, msec = 1000):
        self.get_action().pause(msec)
        self.action_run()
        return self

    ''' Задаёт перемещение к элементу '''
    def action_move(self, elem):
        driver = self.get_driver()
        action = self.get_action()

        self.scroll_shim(driver, elem)
        action.move_to_element(elem)
        self.action_run()
        return self

    ''' Задаёт команду щелчка ЛКМ '''
    def action_click(self, elem):
        self.action_move(elem)
        self.get_action().click(elem)
        self.action_run()
        return self

    ''' Задаёт команду щелчка ПКМ '''
    def action_context_click(self, elem):
        self.action_move(elem)
        self.get_action().context_click(elem)
        self.action_run()
        return self

    ''' Задаёт команду ввод текста '''
    def action_text(self, elem, text):
        self.action_move(elem)
        self.get_action().send_keys_to_element(elem, str(text))
        self.action_run()
        return self

    ''' Задаёт команду выбора select '''
    def action_select_by_text(self, elem, text):
        self.action_move(elem)
        select = Select(elem)
        select.select_by_visible_text(text)
        return self





''' Проверка '''
class AssertScriptSection:

    def_errors = {}

    def _assert(self, value_1, value_2, msg = ""):
        try:
            assert value_1 in value_2
        except Exception:
            raise AssertException(msg)

    def _assert_msg(self, msg, def_msg = ""):
        if bool(msg) != True: msg = def_msg
        return msg

    def assert_equals(self, value_1, value_2, msg = ""):
        msg = self._assert_msg(msg, "Значение '" + str(value_1) + "', ожидалось '" + str(value_2) + "'")
        self._assert(value_1, value_2, msg)

    def assert_true(self, value, msg = ""):
        msg = self._assert_msg(msg, "Значение '" + str(value) + "', ожидалось True")
        self._assert(bool(value), True, msg)

    def assert_false(self, value, msg = ""):
        msg = self._assert_msg(msg, "Значение '" + str(value) + "', ожидалось False")
        self._assert(bool(value), False, msg)

    def assert_none(self, value, msg = ""):
        msg = self._assert_msg(msg, "Значение '" + str(value) + "', ожидалось None")
        self._assert(value, None, msg)



''' Проверка '''
class AssertException(Exception):

    def_errors = {}

    def _assert(self, value_1, value_2, msg = ""):
         assert value_1 in value_2

    def assert_equals(self, value_1, value_2, msg = ""):
        self._assert(value_1, value_2, msg)

    def assert_true(self, value_1, msg = ""):
        self._assert(bool(value_1), True, msg)

    def assert_false(self, value_1, msg = ""):
        self._assert(bool(value_1), False, msg)




''' Общие настройки скрипта '''
class DefaultScript (script_start, ElementScriptSection, ActionScriptSection, AssertScriptSection):

    def_env = None

    def __init__(self, set_start={}):
        print()
        print(self.__class__.__name__)

        script_start.__init__(self, start_set=set_start)

        print()
        print("  Тест: " + type(self).__name__)

    def __del__(self):
        self.log("OK")

    ''' Выводит лог '''
    def log(self, text):
        print("    " + str(text))

    ''' Возвращает драйвер '''
    def get_env(self):
        return self.def_env

    ''' Возвращает драйвер '''
    def get_driver(self):
        return self.driver

    ''' Возвращает/загружает страницу '''
    def get_page(self):
        driver = self.get_driver()
        print(self.host_url.get_url())
        driver.get(self.host_url.get_url())
        return

    ''' Выполняет тест (подгрузка обрабатываемой страницы) '''
    def run(self):
        self.get_page()
        return

    ''' Выполняет паузу '''
    def pause(self, sec = 1):
        time.sleep(sec)
        return self





''' Настройки тестов проекта '''
class DefaultSubscript (DefaultScript):

    parent = None

    def __init__(self, parent):
        self.parent = parent
        self.def_env = parent.get_env()
        return

    def __del__(self):
        return
