projects = [
{'project_id': 1, 'client_id': 101, 'start_date': '2024-01-15', 'end_date': '2024-06-30', 'budget': 50000},
{'project_id': 2, 'client_id': 102, 'start_date': '2024-02-01', 'end_date': '2024-07-15', 'budget': "80000"},
{'project_id': 3, 'client_id': 101, 'start_date': '2024-03-20', 'end_date': '2024-08-20', 'budget': 120000},
{'project_id': 4, 'client_id': 103, 'start_date': '2024-04-10', 'end_date': '2024-09-05', 'budget': 25000},
{'project_id': 5, 'client_id': 102, 'start_date': '2024-05-15', 'end_date': '2024-11-30', 'budget': 60000},
{'project_id': 6, 'client_id': 104, 'start_date': '2024-06-01', 'end_date': '2024-12-15', 'budget': 150000},
{'project_id': 7, 'client_id': 105, 'start_date': '2024-07-01', 'end_date': '2024-12-01', 'budget': 45000},
{'project_id': 8, 'client_id': 103, 'start_date': '2024-08-10', 'end_date': '2025-02-28', 'budget': 75000},
{'project_id': 9, 'client_id': 106, 'start_date': '2024-09-05', 'end_date': '2025-03-30', 'budget': 200000},
{'project_id': 10, 'client_id': 107, 'start_date': '2024-10-01', 'end_date': '2025-04-30', 'budget': 90000},
]

def clinet_budget(project,your_budget=50000):
    if isinstance(project,list):
        for i in project:
            if not isinstance(i,dict):
                return "Input type is not a dictionary"
            else:

                try:
                    outputlist = [[i['budget'],i['project_id']] for i in project]
                    print(outputlist)
                    new_outputlist=[]
                    for i in outputlist:
                        i[0]=int(i[0])
                        if int(i[0]) >= your_budget:
                            new_outputlist.append(i)
                    return sorted(new_outputlist)
                except TypeError:
                    return "The Budget Must be an integer"
                except KeyError:
                    return "The dictionary Does'nt have the essential keys"
    else:
        return "Input type is not a list"






def client_budget2(project):
    if isinstance(project,list):
        try:
            outputlist=[]
            for i in project:
                outputlist.append([i['client_id'],i['budget']])
            outputset=set()
            for i in outputlist:
                outputset.add(i[0])
            budgets=dict()
            for i in outputset:
                z=0
                for j in project:
                    if j["client_id"]==i:
                        z+=int(j["budget"])
                budgets[i]=z            
            return budgets
        except:
            return "Something went wrong"
    else:
        return "Input type is not a list"
    
#print(clinet_budget(projects,50000))
print(client_budget2(projects))