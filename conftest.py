__author__ = 'miserylab'

import pytest
from python_training.fixture.application import Application


fixture = None

# @pytest.fixture
# def app(request):
#     global fixture
#     if fixture is None:
#         fixture = Application()
#         fixture.session.login(username="admin", password="secret")
#     else:
#         if not fixture.is_valid():
#             fixture = Application()
#             fixture.session.login(username="admin", password="secret")
# #    fixture.session.login(username="admin", password="secret")
#     return fixture


#очень долго стартуют тесты=( из-за ensure_login. время ожидания 5 сек self.wd.implicitly_wait(5) вapplication
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture




@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
