import os  # Brings in a helper to work with files and folders on the computer.
import configparser  # Brings in a helper to read and understand rule files.

# This class is like a special notebook for rules and settings.
class Config(object):
    # This is the first page of the notebook where you write down which rule file to use.
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file  # Remember the name of the rule file.
        self._path = os.path.join(os.getcwd(), config_file)
        # Find the rule file’s full location on the computer.

        if not os.path.exists(self._path):
            # Check if the file is missing.
            raise FileNotFoundError("No such file: " + config_file)
            # If the file isn’t there, stop everything and say it’s missing.

        self._config = configparser.ConfigParser()
        # Prepare a helper to read normal rule files.
        self._config.read(self._path, encoding='utf-8-sig')
        # Open the rule file and read its contents.

        self._configRaw = configparser.RawConfigParser()
        # Prepare another helper to read raw (unchanged) rule files.
        self._configRaw.read(self._path, encoding='utf-8-sig')
        # Open the same rule file but keep the data as it is without changes.

    # This function looks up a specific rule from the rule file.
    def get(self, section, name):
        return self._config.get(section, name)
        # Find the rule by its category (section) and name.

    # This function looks up a raw (unchanged) rule from the rule file.
    def getRaw(self, section, name):
        return self._configRaw.get(section, name)
        # Find the raw rule by its category (section) and name.

# These are like opening two notebooks for different sets of rules:
# One for general rules (config.ini) and one for special requirements (require.ini).
global_config = Config('./config.ini')
require_config = Config('./require.ini')

# # 初始化Config对象并加载配置文件
# config = Config(config_file='config.ini')
#
# # 从指定的章节和键中获取值
# use_cookie_pool = config.get('config', 'use_cookie_pool')  # 获取use_cookie_pool的值
# user_agent = config.get('config', 'user-agent')           # 获取user-agent的值
#
# # 获取原始值（未解析处理的内容）
# keyword_raw = config.getRaw('detail', 'keyword')          # 获取搜索关键字的原始值
#
# # 打印这些变量值
# print("Use Cookie Pool:", use_cookie_pool)
# print("User-Agent:", user_agent)
# print("Raw Keyword:", keyword_raw)
#
# # Prints the value of global_config
# print(global_config)
# # Prints the value of global_config
# print(require_config)