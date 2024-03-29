import os, frontmatter

print("Build a lecture connecting the modules available")
lect_title = input("title: ")
lect_author = input("author: ")
lect_date = input("date (YYYY-MM-DD): ")
lect_description = input("Write a short description: ")

lect_text = ['---','\n','categories: lecture','\n','layout: presentation','\n','author: ', lect_author,'\n','title: ',lect_title,'\n','date: ',str(lect_date), '\n---']
# First Slide
lect_text.append("\n#"+lect_title+"\n\n"+lect_description+"\n\nAuthor: "+lect_author+"\n\nDate: "+lect_date+"\n---\n")

# Makes a list of all the tags
path = '_posts/modules'
folder = os.fsencode(path)
tag_list =[]
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    title, file_extension = os.path.splitext(filename)
    if file_extension==".md":
        prs = frontmatter.load(path+"/"+filename)
        try:tag_list= tag_list + prs["tags"]
        except: continue
tag_list=list(set(tag_list))
tag_list=sorted(tag_list)

n=0
# Start creation of lecture
while True:
    n=n+1

    if n==1:
        print("Choose the first module")
    else:
        y=input("\nyour presentation contains "+str(n-1)+" modules, do you want to add more modules? [y/n] ")
        if y=="y":
            print("next selection")
        elif y=="n":
            break

    print(tag_list)

    # Choose tag
    while True:
        t = input("choose one tag: ")
        if t in tag_list:
            print("you selected: "+t)
            break
        else:
            print("wrong entry")

    # Show modules corresponding to the selected tag
    list_mod=[]
    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        title, file_extension = os.path.splitext(filename)
        if file_extension==".md":
            prs = frontmatter.load(path+"/"+filename)
            if t in prs["tags"]:
                b=title.split('-') # this is to remove date from title
                list_mod.append(b[-1])
            else: continue
    print("this is the list of modules with the tag "+t+": "+str(list_mod))

    # Choose one moduel
    while True:
        module=input("choose one module from this list (type 0 if you want to go back): ")
        if module in str(list_mod):
            print("oke")
            #module=frontmatter.load(path+"/"+module+".html")
            #lect_text.append("\n---\n{% include_relative modules/"+module+".html %}")
            #lect_text.append("\n---\n"+module.content)
            lect_text.append("\n{% include_relative /modules/2020-01-01-"+module+".md %}")
            break
        elif module=="0":
            n=n-1
            break
        else:
            print("wrong entry")

# Last slide
lect_text.append("\n#End")

# Save Lecture
lect_title_f = lect_title.replace(' ','_')
with open("_posts/" + lect_date + "-" + lect_title_f + ".md", "w") as presentation_file:
    presentation_file.writelines(lect_text)

# Update content list
#content_list()




