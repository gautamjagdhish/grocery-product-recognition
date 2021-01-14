import json
import collections

with open("mvtec_classes.json", "r") as json_file :
    json_data = json.load(json_file)

id_name = sorted(json_data["categories"], key = lambda x:x["id"])

for record in id_name :
    with open("mvtec_coco.names", "a") as out_file :
        out_file.write(record["name"] + "\n")