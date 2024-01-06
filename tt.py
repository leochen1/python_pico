from datetime import datetime, timedelta

# 獲取現在的時間 commit test
now = datetime.now()
print("現在的時間是：", now)

# 獲取下一秒的時間
next_second = now + timedelta(seconds=1)
print("下一秒的時間是：", next_second)
