import json


def writeFile(root,fileName):
    ret = []
    count=0

    def dfs(now, id):
        nonlocal count
        if now is None:
            return
        if now.left is None and now.right is None:  # leaf node
            ret.append({"type": "leaf", "id": id, "lon": now.POIs[0].lon, "lat": now.POIs[0].lat})
            print("now:"+str(id)+" is leaf")
            
        else:  # branch node
            left, right = count + 1, count + 2
            count += 2
            ret.append({"type": "node", "id": id, "left": left, "right": right})
            print("now:"+str(id)+" is node")
            dfs(now.left, left)
            dfs(now.right, right)

    dfs(root,count)

    ret=sorted(ret,key=lambda a:a["id"])

    with open(fileName,"w") as output:
        output.write(json.dumps(ret))

