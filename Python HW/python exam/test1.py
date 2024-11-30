

def list_of_names(scores = dict(), /,):
    "returns list of lastname, firstname"
    if not scores:
        print("There are no homework scores.")
        return None

    name_list = []

    for k , v in scores.items():
        name_list.append([v["lastname"] , v["firstname"]])
    
    name_list.sort(key=lambda x: x[0])
    return name_list


def student_hw_avg(scores = dict, /, *, id):
    if id not in scores:
        print("ID doesn't exist")
        return None

    sum = 0
    for i in scores[id]["HW_scores"]:
        sum += i

    return sum/len(scores[id]["HW_scores"])


def class_hw_avg(scores = dict, *, index):
    for person_info in scores.values():
        hw_scores = person_info["HW_scores"]
    if index >= len(hw_scores):
        print("Invalid index")
        return None

    sum = 0
    for k, v in scores.items():
        sum += v["HW_scores"][index]

    return sum/len(scores)



