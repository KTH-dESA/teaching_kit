def table_extract(shape, text):
    from special_char import special_char

    tab=shape.table
    rows=tab.rows
    n_rows=len(rows)
    col=tab.columns
    n_col=len(col)
    for r in range(n_rows):
        text.append("\n")
        for c in range(n_col):
             if r == 1 and c == 0: # this step is needed to add the intermediate row
                # Add intermediate row after headers
                intermediate = "|" + "-|" * n_col + "\n"
                text.append(intermediate)
                #  text.append(":---|---:| ---:| ---:| ---:|\n")
                text.append(" |" + tab.cell(r,c).text + " |")
             else:
                text.append(tab.cell(r,c).text+" |")
