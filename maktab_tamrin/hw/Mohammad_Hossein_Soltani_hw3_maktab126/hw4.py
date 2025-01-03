string = "python code map filter reduce lambda"

def my_desired_output(string):
    from functools import reduce
    if isinstance(string,str):
        try:
            listed = string.split(" ")
            mapped = list(map(lambda s:s.upper(),listed))
            filtered = list(filter(lambda s:len(s) > 3,mapped))
            output = reduce(lambda s1,s2:s1 + "_" + s2 ,filtered)
            # output = reduce(lambda l,s:l+[s],filtered,[])
            # return "_".join(output)
            return output
        except:
            return "Something went wrong"
    else:
        return f"input must be a string but yours is{str(type(string))[6:-2]}"
print(my_desired_output(string))