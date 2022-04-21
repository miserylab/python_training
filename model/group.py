__author__ = 'miserylab'

from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # стандартная функция определяет,как будет выглядеть объект при выводе на консоль,
    # каково его строковое представление - representation
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # стандартная функция equals
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
