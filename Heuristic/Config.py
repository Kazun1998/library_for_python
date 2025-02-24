from os import getenv
from sys import stderr

class Config:
    @staticmethod
    def is_product(key = 'environment', development = 'development'):
        return getenv(key) == development

    @staticmethod
    def debug(*messages):
        stderr.write(f"[debug] {' '.join(map(str, messages))}\n")
