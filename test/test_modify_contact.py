from model.contact_info import Contact



def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Tatiana", lastname="Togunova", nickname="Natsu", company_name="Test", address="City2, street2, house2", home_number="7654321", mobile_number="+79174224812", work_number="-",
                                email1="natsu@ya.ru", email2="natsu@gmail.com", bday="13", bmonth="October", byear="1996"))
    app.session.logout()