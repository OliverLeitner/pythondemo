import json
import decimal
# from sqlalchemy.ext.serializer import loads, dumps
from libs.orm.orm import Session, Customer


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)


session = Session()

# Create objects
query = session.query(Customer).order_by(Customer.customerNumber)

# pickle the query
# serialized = dumps(query)

# unpickle.  Pass in metadata + scoped_session
# query2 = loads(serialized)

# print(query2.all())
customers = [r.as_dict() for r in query]
print(json.dumps(customers, cls=Encoder))
