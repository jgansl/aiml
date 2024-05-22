import os
# import spotipy

from dotenv import load_dotenv
from json import dumps
from notion_client import Client
from pprint import pprint
# from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
jprint = lambda x,i=2: print(dumps(x, indent=i))


# Function to insert a Spotify track into a Notion database
def insert_track_to_notion(notion_token, database_id, spotify_client_id, spotify_client_secret, track_id): #!
   # # Initialize Spotify client
   # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))
   
   # # Get track information from Spotify
   # track = sp.track(track_id)
   
   # track_name = track['name']
   # track_uri = track['uri']
   
   # # Initialize Notion client
   # notion = Client(auth=notion_token)
   
   # Prepare data to insert into Notion
   new_page = {
      "parent": {
         "database_id": database_id
      },
      "properties": {
         "Name": {
            "title": [
               {
                  "text": {
                     "content": track_name
                  }
               }
            ]
         },
         "SID": {
            "rich_text": [
               {
                  "text": {
                     "content": track_id
                  }
               }
            ]
         },
         "URI": {
            "url": track_uri
         }
      }
   }
   
   # Insert data into Notion database
   notion.pages.create(**new_page)

# # Example usage
# notion_token = 'your_notion_integration_token'
# database_id = 'your_notion_database_id'
# spotify_client_id = 'your_spotify_client_id'
# spotify_client_secret = 'your_spotify_client_secret'
# track_id = 'spotify_track_id'

# insert_track_to_notion(notion_token, database_id, spotify_client_id, spotify_client_secret, track_id)


if __name__ == "__main__":
   #assert print(os.environ["NOTION_TOKEN"])
   notion = Client(auth=os.environ["NOTION_TOKEN"])
   # from notion_client import AsyncClient
   # notion = AsyncClient(auth=os.environ["NOTION_TOKEN"])
   
   #list_users_response = notion.users.list()
   #jprint(list_users_response)

   query = notion.databases.query(
      **{
         #   "database_id": "897e5a76-ae52-4b48-9fdf-e71f5945d1af",
         "database_id":   "1108aaad2d204c90b743292c74a622c6",
         #   "database_id":   "1108aaad-2d20-4c90b7432-92c74a622c6",
         #   "filter": {
         #       "property": "Landmark",
         #       "rich_text": {
         #           "contains": "Bridge",
         #       },
         #   },
      }
   )
   jprint([i['properties']['Name']['title'][0]['text']['content'] for i in query['results']])