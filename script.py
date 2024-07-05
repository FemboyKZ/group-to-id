import requests
import xmltodict

def fetch_and_save_member_ids(group_url_name):
    url = f'https://steamcommunity.com/groups/{group_url_name}/memberslistxml/?xml=1'
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    data_dict = xmltodict.parse(response.content)
    
    member_ids = data_dict['memberList']['members']['steamID64']
    
    with open('{txt_name}.txt', 'w') as file:
        for steamid in member_ids:
            file.write(f"{steamid}\n")

txt_name = 'whitelist' # txt file name
group_url_name = 'FemWL' # group url

fetch_and_save_member_ids(group_url_name)

print("Member IDs have been saved to {txt_name}.txt")
