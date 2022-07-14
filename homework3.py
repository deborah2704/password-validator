data_set = {
            0: {"name": "deborah", "age": 21, "sex": "female"},
            1: {"name": "esther", "age": 25, "sex": "female"},
            2: {"name": "noa", "age": 34, "sex": "male"}
            }

def split_male_female(data_set):
    male = []
    female = []
    for key, item in data_set.items():
        if item["sex"] == "male":
            male.append(item)
        else:
            female.append(item)
    print(male)
    print(female)
split_male_female(data_set)

def find_median_average(data_set):
    aavg = []
    for key, item in data_set.items():
        aavg.append(item["age"])
    avg = sum(aavg) / len(aavg)
    aavg = sorted(aavg)
    print(aavg)
    print(avg)
find_median_average(data_set)

def print_values_above(data_set, min):
    res = {}
    for key, item in data_set.items():
        if item["age"] >= min:
            res[key] = item
    print(res)
print_values_above(data_set, 22)