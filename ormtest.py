from libs.orm.orm import Session, Customer

session = Session()

# Create objects
for customer in session.query(Customer).order_by(Customer.customerNumber):
    print(customer.customerName)
