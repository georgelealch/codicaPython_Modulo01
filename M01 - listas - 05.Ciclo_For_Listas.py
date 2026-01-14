
def calculate_average(temperatures):
    if temperatures == []:
        return None

    sum = 0
    for i in temperatures:
        sum += i
    return sum / len(temperatures)

print(calculate_average([38, 40, 3, 25, 5]))


####### EJEMPLO CICLO FOR IN RAGE() ############

user_names = ['Carlos', 'Juan', 'Luis']
end = len(user_names)
for i in range(0, end):
    print(user_names[i])

############ EJEMPLO CICLO FOR IN RAGE() ############

def add_prefix(names, prefix):
    end = len(names)
    new_names = []

    for i in range(0, end):
        new_names.append(prefix + ' ' + names[i])
    return new_names

names = ['john', 'smith', 'karl']
new_names = add_prefix(names, 'Mr')
print(new_names)
print(names)
    