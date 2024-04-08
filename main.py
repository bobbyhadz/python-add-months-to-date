# Add months to a date in Python

from datetime import date, datetime
from dateutil.relativedelta import relativedelta


date_1 = date(2023, 6, 24)
print(date_1)  # 👉️ 2023-06-24

# ✅ Add 3 months to a date
result = date_1 + relativedelta(months=+3)
print(result)  # 👉️ 2023-09-24