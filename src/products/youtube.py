from googleapiclient.discovery import build

api_key = 'AIzaSyB575URcoNGOVhLw4aQ26-hjn2VvHlanl0'

# create youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername = 'schafer5' 
)

request = youtube.channels().list(
    part='contentDetails',
    forUsername = 'schafer5' 
)

request = youtube.playlistItems().list(
    part='status',
    playlistId = 'UUCezIgC97PvUuR4_gbFUs5g'
)

response = request.execute()

# print(response)