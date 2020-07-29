import re
from bs4 import BeautifulSoup


def clean_text(text):
    """
    去除html标签和标点符号
    :param text:传入原始文本
    :return:处理后的文本
    """
    text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text
