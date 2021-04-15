
import chevron
import yaml


class YamlTransfer:
    @staticmethod
    def get_yaml_content(filepath, render_dict):
        """
        cheveron渲染yaml文件
        :param render_dict:根据yaml文件中的参数化内容传入的参数值
        mustache用 {{}}代表要进行替换的参数
        :return:
        """
        with open(filepath, encoding='UTF-8') as f:
            result = yaml.safe_load(chevron.render(f, render_dict))
            return result

    @staticmethod
    def get_yaml():
        """
        举例：使用mustache技术进行渲染
        :return:
        """
        result = chevron.render('Hello, {{ mustache }}!', {'mustache': '[\'1\',\'2\',\'3\']'})
        return result
