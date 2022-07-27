from rethinkdb import RethinkDB

r = RethinkDB()
r.connect( "localhost", 28015).repl()
#r.db_create('dicts').run()
#r.db("dicts").table_create("eng-cze").run()

mydict = r.db("dicts").table("eng-cze")

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
		mydict.insert(dict_row).run(durability="soft")


#mydict.insert(whole_list).run()



#with open("en-cs.txt") as file:
	#for line in file:
		#line_list = line.split("\t")
		#dict_row = [{"eng": line_list[0],
					#"cze": line_list[1],
		            #"notes": line_list[2],
		            #"special": line_list[3],
		            #"author": line_list[4]}]
		#mydict.insert(dict_row).run(durability="soft")