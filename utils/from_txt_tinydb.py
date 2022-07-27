from tinydb import TinyDB
from orjson_storage import ORJSONStorage
db = TinyDB('eng-cze.json', storage=ORJSONStorage)
eng_cze = db.table('eng_cze')

def remove_empty(line):
	dict_row = {}
	line_list = line.split("\t")
	dict_row["eng"] = line_list[0] # english translation will be here always
	dict_row["cze"] = line_list[1] # czech translation will be here always
	if line_list[2]:
		dict_row["notes"] = line_list[2]
	if line_list[3]:
		dict_row["special"] = line_list[3]
	removed_new_line = str(line_list[4]).replace("\n", "")
	if removed_new_line:
		dict_row["author"] = removed_new_line
	return dict_row

whole_list = [] 
with open("en-cs.txt") as file:
	for line in file:
		dict_row = remove_empty(line)
		whole_list.append(dict_row)
# tinydb is slow at all, so we need to put whole dictionary to orjson together
eng_cze.insert_multiple(whole_list)


#this is for testing purposes
#with open("en-cs.txt") as file:
	#for line in file:
		#print(remove_empty(line))

# this was first working version
#whole_list = []
#with open("en-cs.txt") as file:
	#for line in file:
	#line_list = line.split("\t")
	#dict_row = {"eng": line_list[0],
	#"cze": line_list[1],
	#"notes": line_list[2],
	#"special": line_list[3],
	#"author": line_list[4],
	#}
	#whole_list.append(dict_row)

#eng_cze.insert_multiple(whole_list)
