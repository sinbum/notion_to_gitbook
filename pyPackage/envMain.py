import configparser


# 토큰
def config_read(path):
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    return config


def get_notion_token(config):
    return config['NOTION_API_OAUTH']['NOTION_TOKEN']


def get_notion_db_id(config):
    return config['NOTION_API_OAUTH']['DB_ID']
