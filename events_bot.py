from tele_psybot import telegram_bot_sendtext
import pandas as pd
from datetime import datetime, timedelta

table_events= "https://docs.google.com/spreadsheets/d/e/2PACX-1vTttnzgDsRC0DK_p37AjXfVDJnJqoV6iDH5aqp9l454pxulRIhTjnJJwEFQ7tPbzpILq4zlVsrpKQaE/pub?gid=0&single=true&output=tsv"
events_df = pd.read_csv(table_events, sep ="\t")

#process times
events_df["Date"] = pd.to_datetime(events_df["Date"])
events_df["Time_start"] = pd.to_timedelta(events_df["Time_start"] + ":00")
events_df["Time_start"] = events_df.Date + events_df.Time_start
events_df = events_df.sort_values(by="Date")

# add one week
in_a_week = datetime.today() + timedelta(days=7)

events_today, events_this_w = "", ""


message_to_send = {"Events_this_w":[], "Events_today": []}
for x,y in events_df.iterrows():

    str_ms =f"""

    {y.Event}

        When:
        {y.Time_start.strftime('%d-%b-%Y %H:%M')}

        Event link: {y.Link}"""

    if y["Time_start"].date() == datetime.today().date():
        events_today += "*Events today: * "
        events_today += str_ms

    elif y["Time_start"].date() < in_a_week.date():
        events_this_w += "*Events this week:* "
        events_this_w += str_ms

final_msg = events_today + "\n\n\n" + events_this_w if events_today else events_this_w

if __name__ == "__main__":
    telegram_bot_sendtext(final_msg)
