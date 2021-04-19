import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# from config import POSTGRES_URI
# TODO: connection string via unixODBC
engine = sqlalchemy.create_engine(
    "mysql+pymysql://demo:123@127.0.0.1:3306/classicmodels?charset=utf8mb4",
    pool_pre_ping=True
)
Session = sessionmaker(bind=engine)

# these two lines perform the "database reflection" to analyze tables and
# relationships
Base = automap_base()
Base.prepare(engine, reflect=True)

# there are many tables in the database but I want `products` and `categories`
# only so I can leave others out
# TODO: move the mapping into new subdir in root, something like 'core'
Product = Base.classes.products
Customer = Base.classes.customers


# for debugging and passing the query results around
# I usually add as_dict method on the classes
def as_dict(obj):
    data = obj.__dict__
    data.pop('_sa_instance_state')
    return data


# add the `as_dict` function to the classes
for c in [Product, Customer]:
    c.as_dict = as_dict

# above goes into its own module #

# session = Session()

# Create objects
# for customer in session.query(Customer).order_by(Customer.customerNumber):
#    print(customer.customerName)
