import json
with open('test.json') as data_file:
    data = json.load(data_file)

set_file = set()
str = '{ "name":"Sacramento Budget 2015/16","children":['
sectionJSON ={}

def save_json(path, data):
    with open(path, 'w') as f:
        f.write(data)

for ele in data:

    set_file.add(ele['department'])
    if sectionJSON.has_key(ele['department']):
        #sectionJSON[ele['department']].append('{"name":"'+ele['spend_type']+'","children":[{"amount2016": "'+ele['amount2016']+'","amount2017": "'+ele['amount2017']+'","pct_change":"'+repr(ele['pct_change'])+'"}]}')
        sectionJSON[ele['department']].append('{"name":"'+ele['spend_type'] +'","amount2016":"'+ ele['amount2016'] +'","amount2017":"'+ ele['amount2017']+'","pct_change":'+ repr(ele['pct_change'])+'}')
    else:
        #sectionJSON[ele['department']] = ['{"name":"'+ele['spend_type']+'","children":[{"amount2016": "'+ele['amount2016']+'","amount2017": "'+ele['amount2017']+'","pct_change":"'+repr(ele['pct_change'])+'"}]}']
        sectionJSON[ele['department']] = ['{"name":"'+ele['spend_type'] +'","amount2016":"'+ ele['amount2016'] +'","amount2017":"'+ ele['amount2017']+'","pct_change":'+ repr(ele['pct_change'])+'}']

for department in set_file:
    str = str+'{"name":"'+department+'","children":['+ ','.join(sectionJSON[department])+']},'

str = str[:-1]
str = str+']}'
dat = json.loads(str)
save_json('t.json',json.dumps(dat))

