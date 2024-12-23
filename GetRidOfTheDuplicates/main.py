studentdata = {"id1":
               {"name" : ['Rajesh'], "class": ['5'], "Subjects": ["Engish, Math, Science"]},
                "id2": 
                {"name" : ['Suryansh'], "class": ['5'], "Subjects": ["Engish, Math, Science"]},
                "id3": 
                {"name" : ['Rajesh'], "class": ['5'], "Subjects": ["Engish, Math, Science"]},
                "id4": 
                {"name" : ['Mahesh'], "class": ['5'], "Subjects": ["Engish, Math, Science"]},

              }

result = {}
for key, value in studentdata.items():
    if value not in result.values():
        result[key] = value

print(result)
