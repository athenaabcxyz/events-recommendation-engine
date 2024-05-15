import pickle
import requests
import mimetypes, urllib3

events = pickle.load(open('artificats/event_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))
event_info = pickle.load(open('artificats/event_info.pkl', 'rb'))
events_list = events['name'].values

def is_url_image(url):    
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def check_url(url):
    """Returns True if the url returns a response code between 200-300,
       otherwise return False.
    """
    try:
        headers = {
            "Range": "bytes=0-10",
            "User-Agent": "MyTestAgent",
            "Accept": "*/*"
        }

        req = urllib3.Request(url, headers=headers)
        response = urllib3.urlopen(req)
        return response.code in range(200, 209)
    except Exception:
        return False

def is_image_and_ready(url):
    return is_url_image(url) and check_url(url)

def fetch_poster(event_id):
    for index in range(len(events)):
        if(event_info.iloc[index]['id']==event_id):           
            name = event_info.iloc[index]['name']
            image_url = event_info.iloc[index]['image']
            venues = event_info.iloc[index]['venues']
            startTime = event_info.iloc[index]['startDateTime']
            info = event_info.iloc[index]['info']
    return name, image_url, venues, startTime, info

def recommend(event):
    index = events[events['name'] == event].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x: x[1])
    recommend_events_id = []
    for i in distances[1:6]:
        event_id = events.iloc[i[0]]['id']
        recommend_events_id.append(events.iloc[i[0]]['id'])
    return recommend_events_id

def rewriteGroup(filterer_id):
    groups = []
    for i in range(0, len(filterer_id), 3):
        groups.append(filterer_id[i:i+3])
    return groups

def event_filter(input_text):
    return_list = []
    if(input_text==''):
        for index in range(len(events)):
            return_list.append(events.iloc[index]['id'])   
    else:
        for index in range(len(events)):
            if (events.iloc[index]['name'].lower().find(input_text)>0):               
                return_list.append(events.iloc[index]['id'])
    return return_list

    


