import requests
import json
from datetime import datetime, timedelta, timezone, tzinfo



class Goals:
    def __init__(self) -> None:
        self.url = "https://g2.goalifyapp.com/api/1.0.1"
        self.head = {"Authorization": "Bearer hYbMa28MkvBc8lbGnIsoqfGXnJ_B1es1KdH-UcsS",
                     "Content-Type": "application/json"}

    def get_all(self):
        x = requests.get(url=self.url + "/goals", headers=self.head)
        j = x.json()
        for e in j['result']['goals']:
            print(e['name'], e['id'])
        return j['result']['goals']

    def post_activity(self, goal_id, activity_value, notes):
        timestamp = datetime.now() - timedelta(hours=7, minutes=55)
        log_time = datetime.now() - timedelta(hours=8, minutes=1)
        activity_time = log_time.strftime('%Y-%m-%dT%H:%M:%S')
        timestamp_formatted = timestamp.strftime('%Y-%m-%dT%H:%M:%S')
        body = {"id": timestamp_formatted, "logtime": activity_time,
                "value": activity_value, "comment": notes}
        print(self.url + "/goals/" + goal_id +
              "/activities/", body)
        x = requests.post(url=self.url + "/goals/" + goal_id +
                          "/activities/", headers=self.head, data=str(body))
        print(x.text)
        return x


a = Goals()
a.post_activity("434ff9d9-3f97-4594-be07-a8e45f47d62f", 1, "Good stuff")
# a.get_all()
# url = "https://g2.goalifyapp.com/api/1.0.1/goals"


# head = {"Authorization": "Bearer hYbMa28MkvBc8lbGnIsoqfGXnJ_B1es1KdH-UcsS"}

# d = {"pluginDescription":"Example Application","permissions":63,"type":"accesstoken","validuntil":"2029-12-31T23:59:59","note":"created by GoalifyDesktop","annotations":{"key":"value"}}

# x = requests.get(url=url, headers=head)
# j = x.json()

# for i in j['result']['goals']:
#     print(i['name'])


# # curl -X POST "https://goalify.example.com/api/1.0.1/tokens/tokenrequest" \
# #      -H "Content-Type: application/json" \
# #      -H "x-goalify-rest-plugin: 320b638f5e225cf483cc5cfdda41c2547eb745079abc9" \
# #      -d ''
# curl -X POST "https://g2.goalifyapp.com/api/1.0.1/tokens/tokenrequest" \
#      -H "Content-Type: application/json" \
#      -H "x-goalify-rest-plugin: 320b638f5e225cf483cc5cfdda41c2547eb745079abc9" \
#      -d '{"pluginDescription":"Example Application","permissions":63,"type":"accesstoken","validuntil":"2019-12-31T23:59:59","note":"created by GoalifyDesktop","annotations":{"key":"value"}}'
