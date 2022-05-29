import datetime
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# s = Service(executable_path='../chromedriver')
# driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'--------------------~*~------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegostudy_url)
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f'{locators.app} App website launched successfully.')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {locators.wegostudy_home_page_title}')
        sleep(0.25)
    else:
        print(f'f{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-----------------------~*~-------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.25)
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == locators.wegostudy_url:
        driver.find_element(By.LINK_TEXT, 'LOGIN').click()
        sleep(0.25)

        if driver.find_element(By.XPATH, '//div[contains(@class, "authentication_form")]').is_displayed():
            print(f'Pop up window is displayed.')
            sleep(0.25)
            driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
            sleep(0.25)
            driver.find_element(By.ID, 'user_password').send_keys(locators.user_password)
            sleep(0.25)
            driver.find_element(By.XPATH, '//input[contains(@value, "SIGN IN")]').click()
            sleep(1.5)

            if driver.current_url == locators.partner_home_page:
                assert driver.find_element(By.XPATH, '//div[contains(text(), "Signed in successfully.")]').is_displayed()
                assert driver.find_element(By.LINK_TEXT, locators.user_name).is_displayed()
                print(f'Signed in successfully at {datetime.datetime.now()}. Username: {locators.user_name}')
            else:
                print(f'Login is not successful. Check your code or website and try again.')


def log_out():
    driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
    sleep(0.5)
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    sleep(0.5)
    assert driver.current_url == locators.wegostudy_url
    assert driver.find_element(By.XPATH, '//div[contains(text(), "Signed out successfully.")]').is_displayed()
    print(f'Signed out successfully at {datetime.datetime.now()}')


def negative_login_test():
    for i in range(10):
        driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
        sleep(0.25)
        driver.find_element(By.ID, 'user_email').send_keys(locators.invalid_logins[i]['email'])
        sleep(0.25)
        driver.find_element(By.ID, 'user_password').send_keys(locators.invalid_logins[i]['password'])
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
        sleep(0.5)
        if driver.find_element(By.XPATH, '//small[@class="error-msg signin-msg"]').is_displayed():
            sleep(1)
            message = driver.find_element(By.XPATH, '//small[@class="error-msg signin-msg"]')
            print(f'{i}: Error message:', message.text)
        else:
            print('Something is wrong, check the code.')
        driver.find_element(By.XPATH, '//button[@class = "close-btn"]').click()
        sleep(1)


def create_new_student():
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    assert driver.current_url == locators.partner_student_details_page
    assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(1)

    if driver.current_url == locators.partner_new_student_page:
        assert driver.current_url == locators.partner_new_student_page
        print(f'We are on new student page.')

        # _______________________________User Picture________________________________

        driver.find_element(By.ID, 'imageUpload').send_keys(locators.image_1)
        sleep(0.5)

        # ____________________________Personal Information___________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').send_keys(locators.middle_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.preferred_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.get_random_passport_number())
        sleep(0.3)
        driver.find_element(By.XPATH, '//span[text()="Country of citizenship"]').click()
        sleep(0.3)
        c = random.randint(254, 500)
        driver.find_element(By.XPATH, f"//option[@data-select2-id='{c}']").click()
        sleep(0.3)
        driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
        sleep(0.3)
        driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
        sleep(0.3)

    # __________________________Contact Information_________________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_apartment_number').send_keys(locators.aprt_number)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.mailing_address)
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'Country').click()
        sleep(0.3)
        driver.find_element(By.XPATH, '//li[@data-option-array-index="21"]').click()
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'Province/State').click()
        sleep(0.3)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[2]').click()
        sleep(0.3)
        driver.find_element(By.LINK_TEXT, 'City').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[3]').click()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postal_code)
        sleep(0.3)
        driver.find_element(By.ID, 'user_email').send_keys(locators.email_address)
        sleep(0.3)

        # ____________________________Education Information_______________________

        driver.find_element(By.LINK_TEXT, 'Credentials').click()
        sleep(0.5)
        driver.find_element(By.XPATH,
                           '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/ul/li[2]').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').send_keys('CCTB')
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').send_keys('ISAQM')
        sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'GPA Scale').click()
        sleep(3)
        driver.find_element(By.XPATH,
                            '//div[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div[1]/ul[1]/li[5]').click()
        sleep(3)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').send_keys('75')
        sleep(0.5)
        driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-green-br ml-auto btn-xs form-group add_fields")]').click()
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='custom-select chosen-select']")).select_by_value('Certificate')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='School Name'])[1]").send_keys('CCTB')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Program'])[1]").send_keys('ISAQM')
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='form-control chosen-select']")).select_by_value('100')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='GPA'])[1]").send_keys('90')
        sleep(0.75)
        driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-red-br")]').click()
        sleep(0.5)

        # ________________________________Documents____________________________________

        driver.find_element(By.XPATH, '//i[@class="fa fa-question-circle"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//a[@data-toggle="tooltip"]').is_displayed()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_documents_attributes_0_file').send_keys(locators.document_1)
        sleep(0.5)
        driver.find_element(By.XPATH,
                            '//a[contains(@class,"btn btn-green-br ml-auto btn-xs mb-3 add_fields")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, '(//input[contains(@class, "form-control-file")])[2]').send_keys(locators.document_2)
        sleep(2)
        driver.find_element(By.XPATH, '(//i[@class="fa fa-times"])[2]').click()
        sleep(0.5)

        # ___________________________Work Experience____________________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_type_of_industry').send_keys('Business')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_position_rank').send_keys('2')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_employer').send_keys('ABC')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_title').send_keys('Account Manager')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_job_description').send_keys(locators.job_description)
        sleep(0.3)
        driver.find_element(By.XPATH, '//a[contains(@class, "btn btn-green-br ml-auto btn-xs add_fields")]').click()
        sleep(0.3)
        driver.find_element(By.XPATH, "(//input[@placeholder='Industry'])[1]").send_keys('Commerce')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Rank'])[1]").send_keys('5')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Employer'])[1]").send_keys('Perl')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Title'])[1]").send_keys('Accountant')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//textarea[@placeholder='Job Description'])[1]").send_keys(locators.job_description)
        sleep(0.5)
        driver.find_element(By.XPATH, '(//a[contains(@class,"btn btn-red-br")])[2]').click()
        sleep(0.3)
        print(f'All fields are populated.')
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//div[contains(text(), "Student is created successfully.")]').is_displayed()
        sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Students').click()
        sleep(1)
        assert driver.current_url == locators.partner_student_details_page
        assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()
        if driver.find_element(By.XPATH, f'//h4[contains(., "{locators.full_name}")]').is_displayed():
            print(f'New student is created successfully.')
            sleep(0.5)
            driver.find_element(By.XPATH, '//img[@alt="Image"]').click()
            sleep(1)


def view_details_of_student():
    sleep(0.5)
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    assert driver.current_url == locators.partner_student_details_page
    assert driver.find_element(By.XPATH, '//h4[contains(text(), "My Students")]').is_displayed()

    elements = driver.find_elements(By.LINK_TEXT, 'View Details')
    size = len(elements)
    print('size:', size)
    random_index = random.randrange(size)
    print('random index:', random_index)

    view_details_link = elements[random_index].get_attribute("href")
    print('view_details_link:', view_details_link)
    elements[random_index].click()
    sleep(1)
    current_url = driver.current_url
    print('current url:', current_url)

    if current_url == view_details_link:
        print('We are on View details of student page.')

        # _______________________________User Picture________________________________

        driver.find_element(By.ID, 'imageUpload').send_keys(locators.image_1)
        sleep(0.5)
        driver.find_element(By.XPATH, '//input[contains(@class, "btn btn-green btn-save")]').click()
        sleep(0.3)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        sleep(0.3)

        # ____________________________Personal Information___________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_middle_name').send_keys(locators.middle_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.preferred_name)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').click()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.date_of_birth)
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.get_random_passport_number())
        sleep(0.3)
        driver.find_element(By.ID, "select2-user_student_detail_attributes_country_of_citizenship-container").click()
        sleep(0.3)
        c = random.randint(254, 500)
        driver.find_element(By.XPATH, f"//option[@data-select2-id='{c}']").click()
        sleep(0.3)
        driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
        sleep(0.3)
        driver.find_element(By.ID, 'phone_number').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
        sleep(1)
        driver.find_element(By.XPATH, '//input[@value="Save"]').click()
        sleep(0.3)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        sleep(0.3)
        print('Personal Information was successfully updated.')

        # __________________________Contact Information_________________________________

        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_apartment_number').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_apartment_number').send_keys(locators.aprt_number)
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.mailing_address)
        sleep(0.3)
        driver.find_element(By.XPATH, "//a[@class='chosen-single']//span").click()
        sleep(1)
        driver.find_element(By.XPATH, '//li[@data-option-array-index="206"]').click()
        sleep(1)
        driver.find_element(By.XPATH, "(//a[@class='chosen-single']//span)[2]").click()
        sleep(1)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[2]').click()
        sleep(1)
        driver.find_element(By.XPATH, "(//a[@class='chosen-single']//span)[3]").click()
        sleep(1.25)
        driver.find_element(By.XPATH, '(//li[@data-option-array-index="1"])[3]').click()
        sleep(1.25)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postal_code)
        sleep(1)
        # driver.find_element(By.ID, 'user_email').clear()
        # sleep(0.3)
        # driver.find_element(By.ID, 'user_email').send_keys(locators.email_address)
        # sleep(1)
        driver.find_element(By.XPATH, "(//input[@name='commit'])[3]").click()
        sleep(0.3)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        sleep(0.3)
        print('Contact Information was successfully updated.')

        # ____________________________Education Information_______________________

        driver.find_element(By.XPATH,
                            "//div[@id='user_student_detail_attributes_user_educations_attributes_0_credentials_chosen']/a[1]/span[1]").click()
        sleep(0.5)
        driver.find_element(By.XPATH, "(//a[@class='chosen-single']//span)[2]").click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').send_keys(
            'UBC')
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').send_keys(
            'IT')
        sleep(0.5)
        driver.find_element(By.XPATH,
                            "//div[@id='user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen']/a[1]/span[1]").click()
        sleep(0.5)
        driver.find_element(By.XPATH,
                            '//div[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div[1]/ul[1]/li[1]').click()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').clear()
        sleep(0.5)
        driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').send_keys('2')
        sleep(0.5)
        driver.find_element(By.XPATH,
                            '//a[contains(@class,"btn btn-green-br ml-auto btn-xs form-group add_fields")]').click()
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='custom-select chosen-select']")).select_by_value(
            'Certificate')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='School Name'])[1]").send_keys('CCTB')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Program'])[1]").send_keys('ISAQM')
        sleep(0.5)
        Select(driver.find_element(By.XPATH, "//select[@class='form-control chosen-select']")).select_by_value('100')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='GPA'])[1]").send_keys('90')
        sleep(0.75)
        driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-red-br")]').click()
        sleep(1)
        driver.find_element(By.XPATH, "(//input[@value='Save'])[3]").click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        sleep(0.3)
        print('Education information was successfully updated.')

        # ________________________________Documents____________________________________

        driver.find_element(By.XPATH, '//i[@class="fa fa-question-circle"]').click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, '//a[@data-toggle="tooltip"]').is_displayed()
        sleep(0.5)
        driver.find_element(By.XPATH,
                            '//a[contains(@class,"btn btn-green-br ml-auto btn-xs mb-3 add_fields")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@type='file'])[2]").send_keys(locators.document_2)
        sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='fa fa-times'])[1]").click()
        sleep(1)
        driver.find_element(By.XPATH, "(//input[@value='Save'])[3]").click()
        sleep(0.5)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        sleep(0.3)
        print('Documents were successfully updated.')

        # ___________________________Work Experience____________________________________

        driver.find_element(By.ID,
                            'user_student_detail_attributes_work_experiences_attributes_0_type_of_industry').clear()
        sleep(0.3)
        driver.find_element(By.ID,
                            'user_student_detail_attributes_work_experiences_attributes_0_type_of_industry').send_keys(
            'IT')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_position_rank').clear()
        sleep(0.3)
        driver.find_element(By.ID,
                            'user_student_detail_attributes_work_experiences_attributes_0_position_rank').send_keys('5')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_employer').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_employer').send_keys(
            'JupiterSoftware')
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_title').clear()
        sleep(0.3)
        driver.find_element(By.ID, 'user_student_detail_attributes_work_experiences_attributes_0_title').send_keys(
            'Developer')
        sleep(0.3)
        driver.find_element(By.ID,
                            'user_student_detail_attributes_work_experiences_attributes_0_job_description').clear()
        sleep(0.3)
        driver.find_element(By.ID,
                            'user_student_detail_attributes_work_experiences_attributes_0_job_description').send_keys(
            locators.job_description)
        sleep(0.3)
        driver.find_element(By.XPATH, '//a[contains(@class, "btn btn-green-br ml-auto btn-xs add_fields")]').click()
        sleep(0.3)
        driver.find_element(By.XPATH, "(//input[@placeholder='Industry'])[1]").send_keys('Commerce')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Rank'])[1]").send_keys('5')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Employer'])[1]").send_keys('Perl')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//input[@placeholder='Title'])[1]").send_keys('Accountant')
        sleep(0.5)
        driver.find_element(By.XPATH, "(//textarea[@placeholder='Job Description'])[1]").send_keys(
            locators.job_description)
        sleep(0.5)
        driver.find_element(By.XPATH, '(//a[contains(@class,"btn btn-red-br")])[2]').click()
        sleep(1)
        header_work_experience_optional = driver.find_element(By.XPATH,
                                                              '//h5[contains(text(), "Work Experience (optional)")]')
        section_work_experience = header_work_experience_optional.find_element(By.XPATH, './..')
        save_button = section_work_experience.find_element(By.XPATH, '//input[contains(@value, "Save")]')
        # save_button.click()
        driver.execute_script("arguments[0].click();", save_button)
        sleep(0.25)
        assert driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").is_displayed()
        print('Work Experience was successfully updated.')
        driver.find_element(By.XPATH, "//div[text()='Student detail was successfully updated.']").click()
        sleep(0.25)


# setUp()
# log_in()
# create_new_student()
# tearDown()

