import re


def strip_ssn(text: str, two_way=False, sub="*ssn*"):
    # matches the form 111-11-1111 and allows for digits replaced by asterisks
    return re.sub(r"[\d*]{3}[-]\d{2}[-]\d{4}", sub, text)