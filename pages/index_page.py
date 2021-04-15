
from pages.base_page import BasePage

from utils.yaml_transfer import YamlTransfer
import os


FILE_PATH = os.path.join(os.getcwd(), r'yamls\index_page.yaml')


class IndexPage(BasePage):
    def search(self, keywords):
        """
        :param keywords: 输入关键字查询
        :return:
        """
        data = {"keywords": keywords}
        yaml_content = YamlTransfer.get_yaml_content(FILE_PATH, data)
        self.exec_steps(yaml_content, 'search')
        from pages.login_page import LoginPage
        return  LoginPage(self.driver)
