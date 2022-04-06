import os

def figure_extract(shape, text, n, title):
    """Extract a figure from a shape
    """
    img = shape.image
    name = str(n) + "_" + img.filename
    if not os.path.exists("assets/img/"+title):
         os.makedirs("assets/img/"+title)
    with open("assets/img/"+title+"/"+name, 'wb') as presentation_image:
         presentation_image.write(img.blob)

    text.append("![](../../assets/img/" + title + "/" + name + ")")
