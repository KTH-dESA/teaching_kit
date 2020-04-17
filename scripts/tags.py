import os, frontmatter
from content_list import content_list

path = '_posts/modules'

folder = os.fsencode(path)

tag_list = ''
tag = 1

for file in os.listdir(folder):
    tag=''
    t=1
    
    filename = os.fsdecode(file)
    title, file_extension = os.path.splitext(filename)
    
    # Select presentations
    if file_extension==".html":
        print("\nModule: "+title)
        prs = frontmatter.load(path+"/"+filename)
        
        # Print tags of the presentation
        try: print("Tags already assigned to presentation: "+str(prs["tags"]))
        
        # if presentation has no tags assign some
        except: 
            print("this presentation has no tags, give it some tags:")
            print("- assign tags to the presentation "+title+", press 0 when finished")
            while t!="0":
                t = input("type tag: ")
                if t == "0" or t=="":
                    continue
                else:
                    #tag.append(t)#+"; ")#do something
                    tag = tag +" "+t
            prs['tags']=tag
            

        # assign/change tags of one presentation
        while True:
            i=""
            i=input("Do you want to keep these tags? [y/n] ")
            t=""
            if i == "y":
                #tag_list= tag_list + prs["tags"]
                #tag_list=tag_list + prs["tags"]
                break
            elif i == "n":
                print("- assign tags to the presentation "+title+", press 0 when finished")
                
                tag=''
                while t!="0":
                    t = input("type tag: ")
                    if t == "0" or t=="":
                        continue
                    else:
                        #tag.append(t)
                        tag = tag +" "+t
                prs['tags']=tag
                break

            else: 
                print("wrong entry")
            
        print("new tags: "+str(prs["tags"]))
        #tag_list= tag_list + prs["tags"]       
        #tag_list=tag_list + prs["tags"]
        
        # save new tags 
        with open(path+"/"+title+".html","w") as presentation_file:
            presentation_file.writelines(frontmatter.dumps(prs))

#tag_list=list(set(tag_list))
#tag_list=sorted(tag_list)
#print("\nThis is the list of tags used: "+str(tag_list))

# Create "tag_page.md" with a list of the tags used
#text=[]
#text.append("### Here is the list of the tags used and the related modules \n")
#for t in tag_list:
#    text.append("\n- ***"+t+":***")
#    i=0
#    for file in os.listdir(folder):
#        filename = os.fsdecode(file)
#        title, file_extension = os.path.splitext(filename)
#        if file_extension==".html":
#            prs = frontmatter.load(path+"/"+filename)
#            if t in prs["tag"]:
#                i=i+1
#                if i!=1: text.append(",")
#                text.append(" ["+title+"](presentations/modules/"+filename+")")
#            else: continue
#    
#    with open("_includes/tags_list.md","w") as file:
#        file.writelines(text)


print("\nAssigned a tag to all presentations in "+path)

# Update content list
#content_list()

