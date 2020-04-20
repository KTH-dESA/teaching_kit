import os, frontmatter

print("Build a course connecting various lectures available")

course_title = input("title: ")
course_author = input("author: ")
course_description = input("Write a short description: ")

course_text=[]
course_text.append("---\ncategories: course\nlayout: page\nauthor: "+course_author+"\ntitle: "+course_title+"\n---\n")
course_text.append("\n# "+course_title+"\n\n"+course_description+"\n\nAuthor: "+course_author+"\n\n")

# Makes a list of all the lectures
path = '_posts/'
folder = os.fsencode(path)
lect_list =[]
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    title, file_extension = os.path.splitext(filename)
    if file_extension==".html":
        prs = frontmatter.load(path+"/"+filename)
        if prs['categories'] == 'lecture':
            b=prs['title'].split('-')
            lect_list.append(b[-1])
        else:
            continue

n=0

# Start creation of Course
while True:
    n=n+1

    if n==1:
        print("Choose the first lecture")
    else:
        y=input("\nYour course contains "+str(n-1)+" lectures, do you want to add more lectures? [y/n] ")    
        if y=="y":
            print("next selection")
        elif y=="n":
            break

    print(lect_list)

    # Choose Lecture
    while True:
        l = input("choose one lecture: ")
        if l in lect_list:
            print("you selected: "+l)
            course_text.append("1. ["+l+"]({{base.url}}/teaching_kit/_posts/"+l+".html)\n")
            break
        else:
            print("wrong entry")

course_title_f = course_title.replace(' ','_')
with open("courses/"+course_title_f+".md","w") as file:
    file.writelines(course_text)



