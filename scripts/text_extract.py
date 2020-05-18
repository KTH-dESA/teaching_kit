def text_extract(shape, text, n):
    from special_char import special_char
    
    if shape.text =="" or shape.text ==" ": #Skip if text box is empty
        text.append('')
    else:
        # read size and position of text box
        width=str(shape.width.pt)
        height=str(shape.height.pt)
        top=str(shape.top.pt)
        left=str(shape.left.pt)
        style = "box"+str(n)
        text.append("\n<style> div."+style+" {position: absolute; left: "+left+"px; top:"+top+"px; width: "+width+"px; height: "+height+"} </style>\n<div class="+style+">")
        #text.append(shape.text_frame.text)

        NoneType = type(None)

        l=0
        for paragraph in shape.text_frame.paragraphs:
            text.append("\n")
            l=l+1
            
            skip=0
            try: paragraph.runs[0].font.size  # try to read font size, if autosize in ppt then assign default size: 18pt
            except: skip=1

            if l==1 and skip==0 and isinstance(paragraph.runs[0].font.size, NoneType): #default size if not assigned in ppt
                size = 18
            elif l==1 and skip==0:          # l=1 means that it check the size only for the firs work of the paragraph
                size = paragraph.runs[0].font.size.pt
            elif l==1 and skip==1:
                size = 18


            text.append("<div style=font-size:"+str(size)+"px>")

            for run in paragraph.runs:
                
                
                if run.font.bold:
                    
                    s = special_char(run.text) # remove special characters
                    text.append("<b>"+s+"</b>")
                elif run.font.italic:
                    s = special_char(run.text) # remove special characters
                    text.append("<i>"+s+"</i>")
                else:
                    s = special_char(run.text) # remove special characters
                    text.append(s)
                
            text.append("</div><br>")
        text.append("\n</div>\n")
        