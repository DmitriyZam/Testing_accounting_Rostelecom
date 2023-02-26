import pytest

from pages.auth_page import AuthPage
from pages.registration_page import RegPage


# TC-LK.RT-1 pass
# проверка отображения страницы входа в приложение
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


# TC-LK.RT-2 fail BR001
# отображение меню входа согласно требований, симметричность 
@pytest.mark.xfail(reason="Расположение элементов на странице не соответсвует ожидаемым требованиям")
def test_location_of_page_blocks(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=1)
    assert page.lk_form.find(timeout=1)


# TC-LK.RT-3 fail BR002
# проверка работы, переключения кнопки Tab меню, смена аунтефикации
@pytest.mark.xfail(reason="Таб выбора 'Номер' не соответсвует ожидаемым требованиям")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# TC-LK.RT-4 fail BR003
# проверка наименования кнопки «Продолжить», согласно требованиям
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


# TC-LK.RT-5 pass
# регистрация пользователя с пустым полем «Имя», появления текста об ошибке
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-6 pass
# регистрация пользователя с полем «Имя» (менее 2-х символов), появление текста об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('P')
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-7 pass
# регистрация пользователя, поле «Фамилия» (более 30-ти символов), появление текста с ошибкой
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Нрвапдлжвоаждваопукпощукшепокщепокшерп")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# TC-LK.RT-8 pass
# Повторная регистрация с зарегистрированным номером, отображается pop-up "Учетная запись уже существует"
def test_registration_of_an_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("+79530696975")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# TC-LK.RT-9 fail BR004
# проверка наличия кнопки «х» - закрыть всплывающее окно оповещения
@pytest.mark.xfail(reason="Должна быть кнопка закрыть 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("+79530697386")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# TC-LK.RT-10 pass
# регистрация пользователя пароль (менее 8-ми символов), появления текста с подсказкой об ошибке
def test_incorrect_password_during_registration(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("man12")
    reg_page.password_confirmation_field.send_keys("man12")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"



# TC-LK.RT-11 pass
# вход по некорректному паролю в форме «Авторизация», при повторной регистраци, появления текста с подсказкой об ошибке
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79530697386')
    page.password.send_keys("Qwerty788")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# TC-LK.RT-12 pass
# форма «Регистрации» в поле ввода «Фамилия», недопустимые символы, вместо кириллицы
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys(";%:?*()"%;%")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



# ТC-LK.RT-13 pass
# форма «Регистрация», поле ввода «Пароль» и поле ввода «Подтверждение пароля», не совпадают.
def test_password_and_password_confirmation_do_not_match(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("leapoldkudasoffrus@gmail.com")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty788")
    reg_page.continue_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# ТC-LK.RT-14 pass
# не валидный email в поле ввода «Email или мобильный телефон»
def test_invalid_email_or_mobile_phone(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Леапольд")
    reg_page.last_name_field.send_keys("Кудасов")
    reg_page.email_or_mobile_phone_field.send_keys("777777")
    reg_page.password_field.send_keys("Qwerty789")
    reg_page.password_confirmation_field.send_keys("Qwerty789")
    reg_page.continue_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"


# TC-LK.RT-15 pass
# тестирование аутентификации зарегестрированного пользователя.
def test_authorisation_valid(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys('+79530697386')
    page.password.send_keys("Qwerty789")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()
                                       
                                       
                                       
# TC-LK.RT-16 pass
# проверка открытия пользовательского соглашения
def test_agreement(selenium):
    form = AuthForm(selenium)

    original_window = form.driver.current_window_handle
    # клик по надписи "Пользовательским соглашением" в подвале страницы
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement' 
                                       
                                       
                                       
# TC-LK.RT-17 pass 
# авторизации пользователя по ссылке через вконтакте
def test_auth_vk(selenium):
    form = AuthForm(selenium)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'
                                
