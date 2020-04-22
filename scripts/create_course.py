import os, frontmatter

print("Build a course connecting various lectures available")

course_title = input("title: ")
course_author = input("author: ")
course_description = input("Write a short description: ")

course_text=[]
course_text.append("---\ncategories: course\nlayout: page\nauthor: "+course_author+"\ntitle: "+course_title+"\n---\n")
course_text.append("<h1>{{ page.title }}</h1>\n\nAuthors: {{page.author}}\n\n"+course_description+"\n\n")

#course_text.append("\n# "+course_title+"\n\n"+course_description+"\n\nAuthor: "+course_author+"\n\n")


# Makes a list of all the lectures
path = '_posts/'
folder = os.fsencode(path)
lect_list =[]
lect_list_long = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    title, file_extension = os.path.splitext(filename)
    if file_extension==".html":
        prs = frontmatter.load(path+"/"+filename)
        if prs['categories'] == 'lecture':
            b=prs['title'].split('-')
            lect_list.append(b[-1])
            lect_list_long.append(filename)

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
            l_url = l.replace(' ','_')            
            course_text.append("1. ["+l+"]({{base.url}}/teaching_kit/lecture/"+l_url+".html)\n")
            

            # obtain full name of lecture
            i = lect_list.index(l)
            lect_fullname = lect_list_long[i]
            # Load lecture and apply new value to "course"
            lect=frontmatter.load(path+lect_fullname)
            try: 
                a = lect["course"]
                lect["course"]= a +", "+course_title
            except:
                lect["course"]=course_title
            # save lecture
            with open(path+lect_fullname,"w") as lecture_file:
                lecture_file.writelines(frontmatter.dumps(lect))


            break
        else:
            print("wrong entry")

#course_text.append('\n***Lectures contained in this course:***\n')
#course_text.append('<ul class="post-list">\n')
#course_text.append('{% assign lectures = site.posts | where: "categories","lecture" %}\n')
#course_text.append('{% for lecture in lectures %}\n')
#course_text.append('{% if lecture.course contains page.title%}\n')
#course_text.append('<p><a href="{{ lecture.url | relative_url }}">{{ lecture.title | escape }} </a></p>\n')
#course_text.append('{% endif %}{% endfor %}</ul>')


course_title_f = course_title.replace(' ','_')
with open("courses/"+course_title_f+".md","w") as file:
    file.writelines(course_text)



