__author__ = 'maanas'

import agms

agms.Configuration.init('init.ini')

trans = agms.Transaction()

params = {
    'transaction_type': {'value': 'sale'},
    'amount': {'value': '100.00'},
    'cc_number': {'value': '4111111111111111'},
    'cc_exp_date': {'value': '0520'},
    'cc_cvv': {'value': '123'}
}

result = trans.process(params)

print result

