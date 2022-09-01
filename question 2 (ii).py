# Create the new dictionary 
studentdict = {
    "first_name":"bhanu prakash",
    "last_name":"dhusari",
    "gender":"male",
    "age":"24",
    "marital_status":"unmarried",
    "skills": ["singing"],
    "country":"USA",
    "city":"lea manor",
    "address":"Missouri",
}
print("The dictionary length is: ", len(studentdict))
studentdict.get("skills")
print("The value of the skills key is: ", studentdict.get("skills"))
datatype= type(studentdict.get("skills"))
print("The datatype of the value of skills key is: ", datatype)
studentdict["skills"].append("cooking")
print("The updated value of the skills key is: ", studentdict.get("skills"))   
keys = list(studentdict.keys())
print(keys)           
print("Now printing the dictionary values as a list :", list(studentdict.values()))








