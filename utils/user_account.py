
import yaml


class UserAccount:
    @staticmethod
    def get_user_info_by_role(roleName):
        """
        :param roleName: 角色名
        :return: 根据传入的角色名返回角色信息：用户名和密码
        """
        with open("../data/user_acount.yaml", encoding='UTF-8') as f:
            result = yaml.safe_load(f)[roleName][0]
            return result
