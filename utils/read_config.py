import configparser
import os


class ReadConfig:

    @staticmethod
    def get_config_parser():
        config = configparser.ConfigParser()
        return config

    @staticmethod
    def get_properties(section, option):
        config = ReadConfig.get_config_parser()
        config.read(os.path.join(os.environ['HOMEPATH'], 'iselenium.ini'))
        return config.get(section, option)

    @staticmethod
    def get_config_path():
        return  os.path.join(os.environ['HOMEPATH'], 'iselenium.ini')

    @staticmethod
    def get_exec_env():
        """
        通过在jenkins中设置env参数，切换用例执行环境
        :return:
        """
        try:
            env = os.environ["env"]
        except KeyError:
            env = None
            host = ReadConfig.get_properties('host', 'beta')
        if env is not None and env.lower() == 'beta':
            host = ReadConfig.get_properties('host', 'beta')
        elif env is not None and env.lower() == 'uat':
            host = ReadConfig.get_properties('host', 'uat')
        return host


if __name__ == '__main__':
    print(f"请将工程下config/iselenium.ini文件拷贝到{os.path.abspath(ReadConfig.get_config_path())}，"
          f"并配置浏览器驱动地址以及访问起始地址")
