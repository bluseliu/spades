
tag_dict = {}
path = 'E:\資策會-DB106\專題\Instagram\士林美食\Tag.txt'
with open(path , 'r', encoding='utf8') as f:
    txt_line_list = f.readlines()

for each_line in txt_line_list:
    for each_tah in each_line.split('#')[1:-1] :
        if each_tah in tag_dict:
            tag_dict[each_tah] += 1
        else:
            tag_dict[each_tah] = 1



print(tag_dict)
print (sorted(tag_dict.items(), key=lambda d: d[1] ,reverse= True) )