# Setting up example database
from database import companies
import dataset

db = dataset.connect('mysql://root:jarrwoo98@localhost/ali')

companies.insert(
    {'company_id':'1234' ,
    'company_name': 'Avita',
    'company_key': '123thjmv79cdfj3ki5tye'}
)
