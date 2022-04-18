# -*- coding: utf-8 -*-
__author__ = 'miserylab'

import pytest
from python_training.model.group import Group
from python_training.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="4324234", header="edfdgdfg", footer="ggdfgfdgdfg"))
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
