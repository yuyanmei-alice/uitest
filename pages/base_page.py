
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import os

from selenium.webdriver.common.keys import Keys

from utils.read_config import ReadConfig


class BasePage:

    def __init__(self, driver: WebDriver = None):
        """
        基类：初始化浏览器启动对象
        :param driver: 从其他页面传过来的driver
        """
        # 控制是否采用无界面形式运行自动化测试
        if driver is None:
            try:
                using_headless = os.environ["using_headless"]
            except KeyError:
                using_headless = None
                print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
            chrome_options = Options()
            if using_headless is not None and using_headless.lower() == 'true':
                print('使用无界面方式运行')
                chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(executable_path=ReadConfig.get_properties('driver', 'chrome_driver'),
                                           options=chrome_options)
            self.driver .maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def _find(self, by, locator):
        """
        封装查找元素的方法
        :param by:
        :param locator:
        :return:
        """
        return self.driver.find_element(by, locator)

    def start(self):
        """
        提供进入index页面的方法
        :return:
        """
        self.driver.get(ReadConfig.get_exec_env())
        from pages.index_page import IndexPage
        return IndexPage(self.driver)

    def exec_steps(self, yaml_content, func):
        """
        步骤驱动
        :param yaml_content: 传入记录操作步骤的yaml文件内容
        :param func: 具体功能方法名
        :return:
        """
        steps = yaml_content[func]
        for step in steps:
            if step['action'] == 'click':
                self._find(step['by'], step['locator']).click()
            elif step['action'] == 'sendKeys':
                self._find(step['by'], step['locator']).send_keys(step['value'])
            elif step['action'] == 'upload':
                self.upload(step['value'])
            elif step['action'] == 'sleep':
                sleep(step['value'])
            elif step['action'] == 'send_keyboard_key':
                self._send_keyboard_key(step['by'], step['locator'], step['value'])
            elif step['action'] == 'mouse_click':
                self._mouse_click()
            elif step['action'] == 'execute_script':
                self._excute_js(step['value'])
            elif step['action'] == 'interrupt_click':
                self._interrupt_click(step['by'], step['locator'])
            elif step['action'] == 'clear':
                self._find(step['by'], step['locator']).clear()
            elif step['action'] == 'switch_to_iframe':
                self._switch_to_iframe(step['by'], step['locator'])

    def close(self):
        """
        封装driver的关闭浏览器方法
        :return: 无
        """
        self.driver.quit()

    def get(self, url):
        """
        封装driver的get方法
        :param url: 跳转url
        :return:
        """
        self.driver.get(url)

    def ielement_is_exsit(self, by, locator):
        """
        判断用例是否存在，用于断言
        :param by: 元素定位方式
        :param locator: 元素具体定位路径
        :return:
        """
        ele = self.driver.find_elements(by, locator)
        if ele.__len__() > 0:
            return True
        else:
            return False

    def element_not_exsit(self, by, locator):
        """
        判断元素是否不存在，用于断言
        :param by: 元素定位方式
        :param locator: 元素具体定位路径
        :return:
        """
        ele = self.driver.find_elements(by, locator)
        if ele.__len__() == 0:
            return True
        else:
            return False

    def _upload(self, file_type):
        """
        封装上传文件方法，用autoit实现（父类私有）
        :param file_type: 上传文件类型（包括xls,pdf,word）
        :return:
        """
        if "xlsx" == file_type:
            os.system('d:\\upload.exe')
        elif "pdf" == file_type:
            os.system('d:\\upload_pdf.exe')
        elif "doc" == file_type:
            os.system('d:\\upload_word.exe')

    def _send_keyboard_key(self, by, locator, value):
        """
        封装模拟键盘操作 （父类私有）
        :param by: 元素定位方式
        :param locator: 元素具体定位路径
        :param value:  需要模拟的键盘操作
        :return:
        """
        if value == 'ENTER':
            self._find(by, locator).send_keys(Keys.ENTER)

    # 封装模拟鼠标操作 （父类私有）
    def _mouse_click(self):
        """
        封装模拟鼠标点击页面的空白处 （父类私有）
        :return:
        """
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()

    def _excute_js(self, js):
        """
        封装执行js方法（父类私有）
        :param js: 需要执行的js语句
        :return: 无
        """
        self.driver.execute_script(js)

    def _interrupt_click(self, by, locator):
        """
        UI自动化时，解决selenium中无法点击Element：ElementClickInterceptedException（父类私有）
        :param by: 元素定位方式
        :param locator:  元素具体定位路径
        :return: 无
        """
        self.driver.execute_script("arguments[0].click();", self._find(by, locator))

    def _switch_to_iframe(self, by, locator):
        """
        封装切换到iframe （父类私有）
        :param by: 元素定位方式
        :param locator: 元素具体定位路径
        :return: 无
        """
        self.driver.switch_to.frame(self._find(by, locator))

    def get_text_of_element(self, by, locator):
        return self._find(by, locator).text



