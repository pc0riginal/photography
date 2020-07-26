import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'_5#y2L"F4Q8z\n\xec]/'