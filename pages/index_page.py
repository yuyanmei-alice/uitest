from pages.base_page import BasePage

from utils.yaml_transfer import YamlTransfer
import os


class IndexPage(BasePage):
    FILE_PATH = os.path.join(os.getcwd(), r'yamls\index_page.yaml')

    def search(self, keywords):
        """
        :param keywords: 输入关键字查询
        :return:
        """
        data = {"keywords": keywords}
        yaml_content = YamlTransfer.get_yaml_content(self.FILE_PATH, data)
        self.exec_steps(yaml_content, 'search')

