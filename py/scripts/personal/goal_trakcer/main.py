'''
export workout data in json

save files to folder

parse each file to find the workouts you want to track

mark the activity to goalify
'''




for i in q['data']['workouts']:
    print(i['name'])
    print(i['activeEnergy']['qty'])
    print("\n")