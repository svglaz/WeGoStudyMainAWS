import datetime
import subprocess
from faker import Faker
fake = Faker(locale=['en_CA','en_US'])


app = 'WeGoStudy'
wegostudy_url = 'https://www.wegostudy.ca/'
wegostudy_home_page_title = 'WeGoStudy'
user_name = 'Joshua Thomas Bailey'
user_email = 'svglaz@yahoo.ca'
user_password = 'testpassword2'
partner_home_page = 'https://www.wegostudy.ca/partner/home'
partner_student_details_page = 'https://www.wegostudy.ca/partners/student_details'
partner_new_student_page = 'https://www.wegostudy.ca/partners/student_details/new'
partner_details_page = 'https://www.wegostudy.ca/partners/partner_details/testpartner-a6d899cd-c8aa-4ed0-87c7-bafea8aca8ae'

first_name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()
preferred_name = f'{first_name} {last_name}'
full_name = f'{first_name} {middle_name} {last_name}'
date_of_birth = '20001112'
passport_number = fake.pyint(111111,999999)
phone_number = fake.phone_number()[:20]
aprt_number = fake.pyint(1,300)
building_number = fake.building_number()
street = fake.street_name()
mailing_address = f'{building_number} {street}'
postal_code = fake.postalcode()
email_address = fake.email()

job_description = fake.sentence(nb_words=50)

path = subprocess.check_output('pwd', shell=True, text=True)

image_1 = path.strip()+'/upload/StudentImage.png'
image_2 = path.strip()+'/upload/avatar.jpg'
document_1 = path.strip()+'/upload/TestDocument_1.pdf'
document_2 = path.strip()+'/upload/TestDocument_2.pdf'

organization = fake.company()
birth_date = fake.day_of_month()+ '-' + fake.month() + '-' + fake.year()


def get_random_passport_number():
    return fake.pyint(111111, 999999)


invalid_logins = [
    {
        'email': 'chris.velasco78gmail.com',
        'password': 'P@r0la000'
    },
    {
        'email': 'chris.velasco78@gmail.com',
        'password': 'P@r0la000'
    },
    {
        'email': ' ',
        'password': 'P@r0la000'
    },
    {
        'email': 'constantinrox.iasi@gmail.com',
        'password': '123password'
    },
    {
        'email': 'constantinrox.iasi@gmail.com',
        'password': ' '
    },
    {
        'email': ' ',
        'password': ' '
    },
    {
        'email': 'chris.velasco78gmail.com',
        'password': '123password'
    },
    {
        'email': ' ',
        'password': '123password'
    },
    {
        'email': 'chris.velasco78@gmail.com',
        'password': ' '
    },
    {
        'email': 'chris.velascigmail.com',
        'password': ' '
    }
]
