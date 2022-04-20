# -*- coding: utf-8 -*-
__author__ = 'miserylab'

from python_training.model.group import Group


def test_add_group(app):
        app.group.create(Group(name="4324234", header="edfdgdfg", footer="ggdfgfdgdfg"))


def test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))
