def text_extract(shape):
    """Extract text from a shape
    """

    text = []

    if shape.text == "" or shape.text == " ": #Skip if text box is empty
        text.append('')
    else:

        for paragraph in shape.text_frame.paragraphs:
            text.append("\n")

            for run in paragraph.runs:

                text.append(run.text)

        text.append("\n")

    return " ".join(text)
