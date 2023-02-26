import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage


# TC-LK.RT-1.
# Загрузка формы разрешения входа.
def test_start_page_is_correct(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert phone_tab_class == "rt-tab rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.auth_title.get_text() == "Авторизация"
    assert page.logo_lk.get_text() == "Личный кабинет"


# TC-LK.RT-2. Ошибка.
# Проверка элементов в левом и правом блоке страницы.
@pytest.mark.xfail(reason="Расположение элементов на странице не соответсвует ожидаемым требованиям")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# TC-LK.RT-3. Ошибка.
# Проверка выбора «Номер».
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответсвует ожидаемым требованиям")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# TC-LK.RT-4. Ошибка.
# Проверка название кнопки «Продолжить» в форме «Регестрация».
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить'")
def test_registration_page_and_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# TC-LK.RT-5.
# Регистрация пользователя с пустым полем «Имя», появления текста с подсказкой об ошибке.
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Семенов")
    reg_page.email_or_mobile_phone_field.send_keys("Semenov1210874@mail.ru")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-6
# Регистрация пользователя с некорректным значением в поле «Имя»(менее 2-х символов), появление текста об ошибке.
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('А')
    reg_page.last_name_field.send_keys("Семенов")
    reg_page.email_or_mobile_phone_field.send_keys("Semenov1210874@mail.ru")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-7
# Регистрация пользователя с некорректным значением в поле «Фамилия» (более 30-ти символов), появление текста с ошибкой.
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алексей")
    reg_page.last_name_field.send_keys("Квлпвплдваполдатггущцымжюмьсдшбфувжмит")
    reg_page.email_or_mobile_phone_field.send_keys("Semenov1210874@mail.ru")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-8
# Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма.
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алексей")
    reg_page.last_name_field.send_keys("Семенов")
    reg_page.email_or_mobile_phone_field.send_keys("+79879746660")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# TC-LK.RT-9. Ошибка.
# Проверка кнопки «х» - закрыть всплывающее окно оповещения.
@pytest.mark.xfail(reason="Должна быть кнопка закрыть 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алексей")
    reg_page.last_name_field.send_keys("Семенов")
    reg_page.email_or_mobile_phone_field.send_keys("+79879746660")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# TC-LK.RT-10
# Некорректный пароль при регистрации пользователя(менее 8-ми символов), появления текста с подсказкой об ошибке.
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алексей")
    reg_page.last_name_field.send_keys("Константинов")
    reg_page.email_or_mobile_phone_field.send_keys("qwerty@mail.ru")
    reg_page.password_field.send_keys("omg87")
    reg_page.password_confirmation_field.send_keys("omg87")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"



# TC-LK.RT-11
# Вход по неправильному паролю в форме «Авторизация» уже зарегистрированного пользователя, надпись «Забыл пароль» перекрашивается в оранжевый цвет.
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79879746660')
    page.password.send_keys("123qwerty")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# TC-LK.RT-12
# Регистрация пользователя в форме «Регистрации» в поле ввода «Фамилия» вместо кириллицы, недопустимые символы.
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Анатолий")
    reg_page.last_name_field.send_keys(",:;;(;%")
    reg_page.email_or_mobile_phone_field.send_keys("123@mail.ru")
    reg_page.password_field.send_keys("12345qwerty")
    reg_page.password_confirmation_field.send_keys("12345qwerty")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



# ТC-LK.RT-13
# Поле ввода «Пароль» и поле ввода «Подтверждение пароля»  в форме «Регистрация» не совпадают.
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Анатолий")
    reg_page.last_name_field.send_keys("Полотно")
    reg_page.email_or_mobile_phone_field.send_keys("123@mail.ru")
    reg_page.password_field.send_keys("qwerty123")
    reg_page.password_confirmation_field.send_keys("qwerty12")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# ТC-LK.RT-14
# Не валидный email в поле ввода «Email или мобильный телефон».
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Анатолий")
    reg_page.last_name_field.send_keys("Полотно")
    reg_page.email_or_mobile_phone_field.send_keys("112233")
    reg_page.password_field.send_keys("qwerty")
    reg_page.password_confirmation_field.send_keys("qwerty")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"


# TC-LK.RT-15
# Тестирование аутентификации зарегестрированного пользователя.
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79879746660')
    page.password.send_keys("KuL7GPYFMQMCwZd")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()
