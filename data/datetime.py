from datetime import datetime
import pytz

local = pytz.timezone("Asia/Ho_Chi_Minh")

def local_now():
    now = datetime.now(local)
    return now.strftime('%H:%M')