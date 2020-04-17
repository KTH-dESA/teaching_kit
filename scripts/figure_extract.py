def figure_extract(shape, text, n, title):
    img=shape.image
    name=str(n)+"_"+img.filename
    with open("_posts/figures/"+title+"/"+name, 'wb') as presentation_image: 
         presentation_image.write(img.blob)
    width=str(shape.width.pt)
    height=str(shape.height.pt)
    top=str(shape.top.pt)
    left=str(shape.left.pt)
    style = "style"+str(n)
    #text.append("\n<img src=figures/"+title+"/"+name+" position=absolute top="+top+"px left="+left+"px width="+width+"px height="+height+"px />")
    text.append("\n<style> div."+style+" {position: absolute; left: "+left+"px; top:"+top+"px} </style>\n<div class="+style+"><img src=figures/"+title+"/"+name+" width="+width+"px height="+height+"px /></div>")
    
