from django.db import models

daily_order_seq_creation_ddl = """create table if not exists daily_order_seq_{}
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
)
"""


class Order(models.Model):
    # YYYYMMDD-nnnnn
    id = models.CharField(max_length=14, primary_key=True)
