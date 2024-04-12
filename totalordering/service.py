from django.db import connection
from .models import daily_order_seq_creation_ddl, Order


def create_order(dt):
    date_str = dt.strftime('%Y%m%d')
    with connection.cursor() as cur:
        cur.execute(daily_order_seq_creation_ddl.format(date_str))
        cur.execute("insert into daily_order_seq_{} () values ()".format(date_str))
        cur.execute("select last_insert_id()")
        last_insert_id = cur.fetchone()[0]

    order = Order(pk="{}-{:05d}".format(date_str, last_insert_id))
    order.save()
    return order
