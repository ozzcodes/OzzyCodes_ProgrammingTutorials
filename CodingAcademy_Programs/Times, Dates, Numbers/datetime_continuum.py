from datetime import datetime
from datetime import timedelta

now = datetime.today()
print(now)
print(now + timedelta(days=1))

then = now + timedelta(days=1)
print(then - now)
