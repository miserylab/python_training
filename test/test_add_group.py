# -*- coding: utf-8 -*-
__author__ = 'miserylab'

from python_training.model.group import Group


def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="4324234", header="edfdgdfg", footer="ggdfgfdgdfg"))
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
