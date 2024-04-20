import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = config.driver


# Загрузка тестовой страницы
def load_page():
    driver.get('https://koshelek.ru/authorization/signup')
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "k-text")))

# Локатор. Возвращает css класс для проверки наличия ошибки в поле "Имя пользователя"
def username_field_message_class(shadowroot):
    namehost = shadowroot.find_element(By.CSS_SELECTOR, '[class="v-text-field__slot"]')
    messageclass = namehost.find_element(By.TAG_NAME, 'label').get_attribute("class")
    return messageclass

# Тэг label содержит информацию об ошибке ввода. Функция возвращает нужный label для поля ввода с названием name
def find_label(labels, name):
    for label in labels:
        if label.text == name:
            return label

# Локатор. Возвращает css класс для проверки наличия ошибки в поле "email"
def email_field_message_class(shadowroot):
    labels = shadowroot.find_elements(By.CSS_SELECTOR, 'label')
    messageclass = find_label(labels, 'Электронная почта').get_attribute("class")
    return messageclass

# Локатор. Возвращает css класс для проверки наличия ошибки в поле "Имя пользователя"
def password_field_message_class(shadowroot):
    labels = shadowroot.find_elements(By.CSS_SELECTOR, 'label')
    messageclass = find_label(labels, 'Пароль').get_attribute("class")
    return messageclass

# Вводит name в поле "Имя пользоветеля", находящегося в shadowroot
def set_username(name, shadowroot):
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-text-field-primary"]').send_keys(name)

# Тесты поля "Имя пользователя". Описание теста в его названии
def test_username_pustoi_vvod():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_5_simvolov():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('olego', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_zaglavnih_bykv():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('OLEGOL', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_33_simvola():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('olegoolegoolegoolegoolegoolegoole', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_cifra_v_na4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('1olegol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_specsimvol_v_na4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('@olegol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_defis_v_na4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('-olegol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_simvoli_drygogo_jazika():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('올레고고글고엘드', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_rysskih_bykv():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('олегол', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_pod4erkivanie_v_na4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('_olegol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_so_specsimvolami():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('oleg@!$%^&*ol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_s_defisom():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('oleg-ol', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_s_probelom_vnytri():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('oleg oleg', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_s_probelom_vna4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username(' olegoleg', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_drygogo_polzovatela():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('ovpltest', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)


def test_username_stroka_s_simvolami_ekranirovania():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    set_username('ole{gol}', shadowroot)
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in username_field_message_class(shadowroot)

# Тесты поля "Email". Описание теста в его названии
def test_email_pustoi_vvod():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_rysskih_bykv():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('олег@маил.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_s_dvoinoi_maskoi():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('oleg@mail.ruoleg@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_probel_v_nazvanii_jashika():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('oleg@m ail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_probel_v_nazvanii_polzovatela():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('ole g@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_nazvanie_zanjato():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('ov-pl@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_so_specsimvolami_v_nazvanii_polzovatela():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('oleg!#$%^&*@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_so_specsimvolami_v_nazvanii_jashika():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('oleg@ma!#$%^&*il.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_s_probelom_v_na4ale():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys(' oleg@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_s_simvolami_ekranirovanija():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('{oleg@mail.ru}')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_s_zaglavnimi_bykvami():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('OLEG@MAIL.RU')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)


def test_email_stroka_s_simvolami_drygogo_jazika():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "username").send_keys('올레고@mail.ru')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in email_field_message_class(shadowroot)

# Тесты поля "Пароль". Описание теста в его названии
def test_password_pustoi_vvod():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in password_field_message_class(shadowroot)


def test_password_7_simvolov():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "new-password").send_keys('1Olegol')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in password_field_message_class(shadowroot)


def test_password_65_simvolov():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "new-password").send_keys(
        '1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg1Oleg')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in password_field_message_class(shadowroot)


def test_password_stroka_bez_zaglavnih_bykv():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "new-password").send_keys('1olegoleg')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in password_field_message_class(shadowroot)


def test_password_stroka_bez_cifr():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    shadowroot.find_element(By.ID, "new-password").send_keys('olegoleg')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in password_field_message_class(shadowroot)

# Тест чек-бокса
def test_checkbox_ne_aktiven():
    load_page()
    shadowroot = driver.find_element(By.CSS_SELECTOR, '.remoteComponent').shadow_root
    checkbox = shadowroot.find_element(By.CSS_SELECTOR,
                                       '[class="v-input v-input--hide-details v-input--dense theme--light v-input--selection-controls v-input--checkbox"]')
    shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
    assert 'error--text' in checkbox.get_attribute("class")
    driver.quit()

# username
# shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-text-field-primary"]').send_keys('12345')

# email
# shadowroot.find_element(By.ID, "username").send_keys('12345')

# password
# shadowroot.find_element(By.ID, "new-password").send_keys('12345')

# checkbox
# shadowroot.find_element(By.CLASS_NAME, "v-input--selection-controls__input").click()

# далее
# shadowroot.find_element(By.CSS_SELECTOR, '[specialtoken="k-btn-long-button"]').click()
