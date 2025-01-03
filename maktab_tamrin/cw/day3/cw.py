Input_Example=[("001", "Alpha Corp", "Technology"),("002", "Beta LLC", "Health"), ("003", "Gamma Inc","Technology")]

def company_work(input_ex):
    output = []
    output1 = []
    final_output = {}
    for i in input_ex:
        if i[2] not in output:
            output.append(i[2])
    
    for i in output:
        output1 = []
        for j in input_ex:
            if i == j[2]:
                output1.append((j[0],j[1]))
        final_output[i] = dict(output1)
    return final_output
print(company_work(Input_Example))