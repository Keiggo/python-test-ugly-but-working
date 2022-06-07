BROKER = 'broker'
SUPPLIER = 'supplier'
CUSTOMER = 'customer'

ROLE = [
    (BROKER, BROKER.title()),
    (SUPPLIER, SUPPLIER.title()),
    (CUSTOMER, CUSTOMER.title()),
]

PENDING = 'pending'
FULLFILLED = 'fullfilled'

ORDER_STATUS = [
    (PENDING, PENDING.title()),
    (FULLFILLED, FULLFILLED.title()),
]