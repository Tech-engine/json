import json

# opening the given unformated json file and creating a list out of it and storing it in data
with open('test.json') as data_file:
    data = json.load(data_file)

# creating a set to all unique departments in json file
set_file = set()

# str is a string format of final formatted json
str = '{ "name":"Sacramento Budget 2015/16","children":['

# creating a dictionary whose keys will be department names and corresponding value will be an array of all children of respective department
sectionJSON ={}

# function to save the final json file
def save_json(path, data):
    with open(path, 'w') as f:
        f.write(data)

# loop through each department store in data
for ele in data:
    set_file.add(ele['department'])
    #if sectinJSON has already a key(deaparment) then add the string
    if sectionJSON.has_key(ele['department']):
        sectionJSON[ele['department']].append('{"name":"'+ele['spend_type']+'","children":[{"amount2016": "'+ele['amount2016']+'","amount2017": "'+ele['amount2017']+'","pct_change":"'+repr(ele['pct_change'])+'"}]}')
    # otherwise create a key named after the department and store the string in an array
    else:
        sectionJSON[ele['department']] = ['{"name":"'+ele['spend_type']+'","children":[{"amount2016": "'+ele['amount2016']+'","amount2017": "'+ele['amount2017']+'","pct_change":"'+repr(ele['pct_change'])+'"}]}']

# creating the final string version of json output
for department in set_file:
    str = str+'{"name":"'+department+'","children":['+ ','.join(sectionJSON[department])+']},'

# remove the last extra comma and preparing the fnal json string
str = str[:-1]
str = str+']}'

# converting the string to json and save the final formated output to a file "t.json"
dat = json.loads(str)
save_json('t.json',json.dumps(dat))

