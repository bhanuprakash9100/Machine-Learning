it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("The length of the above set is :", len(it_companies))
it_companies.add("Twitter")
print("The updated set is :", it_companies)
mnc_companies = {'mrs.Fields', 'Nation wide', 'silicon valley'}
it_companies.update(mnc_companies)
print("The set after adding multiple IT companies :", it_companies)
it_companies.remove('Facebook')
print("The set after removing facebook is :", it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print("After joining A and B sets :", C)
x = A.intersection(B)
print("The intersection of A and B is :", x)
y = A.issubset(B)
print("A subset of B :", y)
z = A.isdisjoint(B)
print("Disjoint of A and B :", z)
X = A.union(B)
print("Joining A with B :", X)
Y = B.union(A)
print("Joining B with A :", Y)
abc = A.symmetric_difference(B)
print("The symmetric difference of A and B :", abc)
A.clear()
B.clear()
print("The set A after deleting completely :", A)
print("The set B after deleting completely :", B)
age_list = [22, 19, 24, 25, 26, 24, 25, 25]
print("The length of the given above age list is :", len(age_list))
age_set = set(age_list)
print("converted age list to age set :", age_set)


