from datetime import datetime
from dateutil import tz

UTCtime = datetime.utcnow()
print(type(UTCtime))
print(UTCtime)

HERE = tz.tzlocal()
print(HERE)

UTC = tz.gettz('UTC')
gmt = UTCtime.replace(tzinfo=UTC)
gmt.astimezone(HERE)
print(gmt.astimezone(HERE))

