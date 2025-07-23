import requests
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'


def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

def get_pages(response):
    return response['info']['pages']


#1 - Get the Character id of Rick Sanchez
#pages = data['info'][0]['pages']
#id = data['Rick Sanchez']['id']
#Get the current status and location of Rick Sanchez and Morty Smith
#name = data['results'][1]['name']
#status= data['results'][1]['status']
#location= data['results'][1]['location']
#name_0 = data['results'][0]['name']
#character_id = data['results'][0]['id']
#status_0 = data['results'][0]['status']
#location_0 = data['results'][0]['location']
#print(name,id, status, location, name_0, status_0, location_0, character_id)

#Get all the episodes where "Gene" has appeared, and the location for him.
#def cate_episoade (response):
    #charlist=[]
    #for item in response['results']:
        #char = { 'name': 'Gene',
                 #'no_ep': len(item['episode']),
                 #'location':item['location']}
        #charlist.append(char)
        # return charlist
#data = main_request(baseurl, endpoint)
#print(cate_episoade(data))

#- List all the characters who are alive and appeared in the "Narnia Dimension", regardless of episode or season.
#def all_characters(response):
    #charlist=[]
    #for character in response['results']:
     #if character['status']=='Alive' and character['location']['name']=='Narnia Dimension':
        #charlist.append(character)
        #return charlist
#data = main_request(baseurl, endpoint)
#print(all_characters(data))

#5 - From episode 28, list all the characters who have "Rick" in their name.
#def episode_28(response):
    #charlist = []

    #for character in response['results']:
        #name = character.get('name', '')
        #episodes = character['episode']

        #if 'Rick' in name:
            #for episode in episodes:
                #if '/28' in episode:
                    #charlist +=[character]
                    #charlist.extend([character])
                    #continue

    #return charlist

#data = main_request(baseurl, endpoint)
#for character in episode_28(data):
    #print(character['name'])

#List all the characters who are not Alive from episode 29.
#def are_alive (response):
    #charlist = []
    #for character in response['results']:
        #episodes = character['episode']

        #if character['status'] != 'Alive':
            #for episode in episodes:
                #if '/29' in episode:
                    #charlist +=[character]
                    #break
    #return charlist
#data = main_request(baseurl, endpoint)
#print(are_alive(data))

#List all the Species and filter them by types that appear in Season3, and if the species is different from Human,list their name based on the Species/Types.
def species_listing(response):
    species_list=[]
    name_added_once = []
    episodes = main_request(baseurl, "/episode/22,31")
    for character in response['results']:
        species = character.get('species','')
        types = character.get('type', '')
        name = character.get('name', '')
        if species != 'Human':
            for episode in episodes:
                if 22 <= episode['id'] <= 31:
                     species_list += [character]
                     name_added_once +=[name_added_once]
                #print(f"Species name : {name} and species type:{types}")
                break
        #else:
             #print(f"Species :{species} and type: {types}")
    return species_list
data = main_request(baseurl, endpoint)
print(species_listing(data))




