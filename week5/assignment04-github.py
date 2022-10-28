import requests
from github import Github
from config import config as cfg # import token from the config file

token = cfg["github_token"]  
 # store the key as a variable 
g = Github(token)                                                         
repo = g.get_repo("Cormac88/aprivateone")
# get the repo our my file is stored in

file_info = repo.get_contents("string_replace.txt")
# gets the contents of my file in the private repo
file_url = file_info.download_url
# gets the url of my file in the private repo


response = requests.get(file_url)
# make http request to file url
file_on_repo = response.text
# output the contents of the file

new_file = file_on_repo.replace("Andrew", "Cormac" )
# Replaces words 'Andrew' with 'Cormac'


# Use the library function to update the contents of the file on github
github_resonse = repo.update_file(file_info.path,"Replaces words 'Andrew' with 'Cormac'", 
new_file, file_info.sha)
# Pass the path, commit message, the new file content and file 
# sha(unique ID for the commit) as parameters

print(github_resonse)