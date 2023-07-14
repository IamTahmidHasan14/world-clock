import datetime
from dateutil import tz


def get_time_in_country(country, timezone):
  try:
    current_time = datetime.datetime.now(timezone)
    time_string = current_time.strftime("%I:%M %p")
    print(f"{country}: {time_string}")
  except Exception:
    print(f"Timezone information not available for {country}.")


countries = {
  'USA': 'America/New_York',
  'UK': 'Europe/London',
  'Finland': 'Europe/Helsinki',
  'Bangladesh': 'Asia/Dhaka',
  'Malaysia': 'Asia/Kuala_Lumpur',
  'Japan': 'Asia/Tokyo',
  'Australia': 'Australia/Sydney'
}

for country, timezone in countries.items():
  timezone = tz.gettz(timezone)
  get_time_in_country(country, timezone)
  print()
