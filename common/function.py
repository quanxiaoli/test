import os,configparser


def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]


def config_url():
    config=configparser.ConfigParser()
    config.read(project_path()+'\config.ini')
    return config.get("url",'')
if __name__=='__main__':
    print("项目路径："+project_path())