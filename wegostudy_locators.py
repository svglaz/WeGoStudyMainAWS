import datetime
from faker import Faker
fake = Faker(locale=['en_CA','en_US'])

app = 'WeGoStudy'
wegostudy_url = 'https://www.wegostudy.ca/'
wegostudy_home_page_title = 'WeGoStudy'
user_name = 'TestPartner'
user_email = 'svglaz@yahoo.ca'
user_password = 'testpassword2'
partner_home_page = 'https://www.wegostudy.ca/partner/home'
partner_student_details_page = 'https://www.wegostudy.ca/partners/student_details'
partner_new_student_page = 'https://www.wegostudy.ca/partners/student_details/new'

first_name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()
preferred_name = f'{first_name} {last_name}'
full_name = f'{first_name} {middle_name} {last_name}'
date_of_birth = '20001112'
passport_number = fake.pyint(111111,999999)
phone_number = fake.phone_number()
aprt_number = fake.pyint(1,300)
building_number = fake.building_number()
street = fake.street_name()
mailing_address = f'{building_number} {street}'
postal_code = fake.postalcode()
email_address = fake.email()

job_description = fake.sentence(nb_words=50)

image_1 = './upload/StudentImage.png'
document_1 = './upload/TestDocument_1.pdf'
document_2 = './upload/TestDocument_2.pdf'