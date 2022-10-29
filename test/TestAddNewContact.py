# -*- coding: utf-8 -*-
import pytest
from model.contact_info import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="Ella", lastname="Sova", nickname="Somnium", company_name="Lenvendo", address="City, street, house", home_number="1234567", mobile_number="+79818486206", work_number="-",
                                email1="ella.mukh@ya.ru", email2="ella.somnium@gmail.com", bday="19", bmonth="May", byear="1992"))
    app.session.logout()
