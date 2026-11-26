scores={}
teams={}
with open("players.txt","r") as file:
    for line in file:
        if line.strip()=="":
            continue
        data=line.split()
        name=data[0]
        points=int(data[1])
        team=data[2]

        scores[name]=points
        if team not in teams:
            teams[team]=[]
        teams[team].append(name)
print("Scores:",scores)
print("Teams:",teams)
def points_by_team(scores,teams):
    result={}
    for team in teams:
        total=0
        for player in teams[team]:
            total+=scores[player]
        result[team]=total
    return result
print("Points by team:",points_by_team(scores,teams))
