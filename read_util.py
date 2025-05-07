import yaml
import os
class YamlUtil:
    #读取环境文件
    # def read_enivrment_yml(self):
    #     with open(os.getcwd()+"/testcases.yml", 'r') as ymlfile:
    #         value = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    #         return value
     #读取用例文件
    def read_cases_yml(self,yaml_name):
        # path = os.path.join(yaml_name)

        with open(target_path, 'r', encoding='utf-8') as ymlfile:
            value = yaml.load(ymlfile, Loader=yaml.FullLoader)
            return value