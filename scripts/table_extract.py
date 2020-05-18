def table_extract(shape, text):
    from special_char import special_char
    
    tab=shape.table
    rows=tab.rows
    n_rows=len(rows)
    col=tab.columns
    n_col=len(col)
    for r in range(n_rows):
        text.append("\n |")
        for c in range(n_col):
             if r == 1 and c == 0: # this step is needed to add the intermediate row 
                 text.append(":---|---:| ---:| ---:| ---:|\n")
                 s = special_char(tab.cell(r,c).text)
                 text.append(" |"+s+" |")
             else:
                 s = special_char(tab.cell(r,c).text)
                 text.append(s+" |")