# Setting up example database
from database import companies
import dataset

password = None
db = dataset.connect(f'mysql://root:{password}@localhost/ali')

companies.insert(
    {'company_id':'1234' ,
    'company_name': 'Avita',
    'company_key': '123thjmv79cdfj3ki5tye'}
)
    