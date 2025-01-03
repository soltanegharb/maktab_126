#from cw import company_work
#from cw2 import clinet_budget

#Input_Example=[("001", "Alpha Corp", "Technology"),("002", "Beta LLC", "Health"), ("003", "Gamma Inc","Technology")]
projects = [
{'project_id': 1, 'client_id': 101, 'start_date': '2024-01-15', 'end_date': '2024-06-30', 'budget': '50000'},
{'project_id': 2, 'client_id': 102, 'start_date': '2024-02-01', 'end_date': '2024-07-15', 'budget': 80000},
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
    print(project)
    if isinstance(project,list):
        for i in project:
            if not isinstance(i,dict):
                return "Input type is not a dictionary"
            else:

                outputlist=[]
                try:
                    for i in project:
                        outputlist.append([i['budget'],i['project_id']])
                    new_outputlist=[]
                    try:
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

def report( cb):
    res = clinet_budget(cb)
    with open("output.txt","w") as file:
        file.write("""The File Report:\n/////////////////////\n\n""")
        try:    
            for i in res:
                file.write(f"The Amount of Budget for the Project Id:{i[1]} is {i[0]}\n")
        except:
            return "Something went wrong!"
report(projects)
