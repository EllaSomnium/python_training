# -*- coding: utf-8 -*-
import pytest
from contact_info import Contact
from application1 import ApplicationC


@pytest.fixture
def appl(request):
    fixture = ApplicationC()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(appl):
    appl.login(user="admin", password="secret")
    appl.add_new_contact(Contact(firstname="Ella", lastname="Sova", nickname="Somnium", company_name="Lenvendo", address="City, street, house", home_number="1234567", mobile_number="+79818486206", work_number="-",
    email1="ella.mukh@ya.ru", email2="ella.somnium@gmail.com", bday="19", bmonth="May", byear="1992"))
    appl.logout()
