import json

def save_score(name,score):
    with open('files/score.json', 'r') as file:
        data = json.load(file)

    try:
        new_score = data.get(name) + score
    except:
        new_score = score
    
    data[name] = new_score

    with open('files/score.json', 'w') as outfile:
        json.dump(data, outfile)


def get_total_score():
    with open('files/score.json', 'r') as file:
        data = json.load(file)
    
    return data