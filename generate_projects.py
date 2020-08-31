import json
import requests
import os
from requests.auth import HTTPBasicAuth
user, pwd = 'everyhopa', 'allibody'
r = requests.get('http://cb.uu.se/internt/annual_report/exportprojects.php?format=json&where=funding LIKE \'%BioImage Informatics Facility%\'', auth=HTTPBasicAuth(user, pwd))
jsonText = "["+r.text.replace("}{","},{")+"]"
jsonVal = json.loads(' '.join(jsonText.split()))
from unidecode import unidecode

try:
    from html.parser import HTMLParser  # Python 3
except ModuleNotFoundError:
    from HTMLParser import HTMLParser  # Python 2
parser = HTMLParser()
#jsonVal = parser.unescape(jsonVal)

template = """---
# Fill out as many of these as you can, and delete the rest.
# Text on a line after a "#" is a comment and is ignored for the published page.

title: "{title}"
author: {cbastaff}
external: "{external}"
excerpt: "{description_short}"
image: "{image}" # Image should be pushed to /images/projects/YYYY-MM-DD-projectid/ before
keywords: "{keywords}"
funding: "{funding}"
initdate: "{initdate}"
lastdate: "{lastdate}"
tags_: "{tags}"
# project_homepage_url: "http://example.com/external-project-page" # Optional external homepage for this project
---

## Project Description
{description}
"""
ids = {
    '190': 'EmmaAndersson2019-1',
    '193': 'AndersIsaksson2019-1',
    '194': None,
    '170': 'OscarFernandezCapetillo2018-1',
    '50': '',
    '52': '',
    '53': '',
    '54': '',
    '59': '',
    '67': '',
    '68': '',
    '69': '',
    '71': '',
    '144': '',
    '145': '',
    '146': '',
    '151': '',
    '169': '',
    '173': '',
    '180': '',
    '182': '',
    '183': '',
    '51': '',
    '55': '',
    '56': '',
    '57': '',
    '58': '',
    '61': '',
    '66': '',
    '162': 'BjörnBrunström2018-1',
    '163': 'ErikaComasco2018-1',
    '164': 'NilsHailer2019-1',
    '165': '',
    '171': 'PerOlaCarlsson2018-1',
    '172': '',
    '181': 'MarcelDenHoed2018-1'
}

for project in jsonVal:
    project["description_short"] = project["description"].replace("\r\n"," ")[:200] + "..."
    project["description"] = project["description"].replace("\r\n","<br/><br/>")
    
    print (project.keys())
    project["initdate"] = project["initdate"].replace("--","01").replace("-","")
    project["initdate"] = "{0}-{1}-{2}".format(project["initdate"][:4],project["initdate"][4:6],project["initdate"][6:8])
    project["lastdate"] = project["lastdate"].replace("--","01").replace("-","")
    if project["lastdate"] != "Current":
        project["lastdate"] = "{0}-{1}-{2}".format(project["lastdate"][:4],project["lastdate"][4:6],project["lastdate"][6:8])
    
    project["cbastaff"] = "[\"" + "\", \"".join(project["cbastaff"].split(",")) + "\"]"

    
    filename = ids[project["id_project"]]
    if filename is None:
        continue
    if filename == "":
        filename = project["external"].split(",")[0].split("-")[0].strip().replace(" ","")
    filename = project["initdate"] + "-" + filename

    filename = unidecode(parser.unescape(filename))

    path = "projects\_posts\\" + filename + ".md"
    if project["image"]:
        image_url = "http://cb.uu.se/research_images/" + project["image"]
        localImagePath = "images\projects\\" + filename + os.path.splitext(project["image"])[1]
        r = requests.get(image_url, allow_redirects=True, auth=HTTPBasicAuth(user, pwd))
        if not os.path.isdir(os.path.dirname(localImagePath)):
            os.makedirs(os.path.dirname(localImagePath))
        open(localImagePath, 'wb').write(r.content)

        project["image"] = "/" + localImagePath.replace("\\","/")
    
    outputFile = template.format(**project)

    #print (localImagePath, path)
    #print (project["id_project"],"\n","  ",project["initdate"],"\n","  ",project["external"],"\n","  ",project["title"])
    #print (project["id_project"],"\n","  ",project["image"],"\n","  ",project["image2"],"\n","  ",project["image3"])
    #print (outputFile)
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path,'w') as projectFile:
        projectFile.write(outputFile)
    