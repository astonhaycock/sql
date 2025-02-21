from tabulate import tabulate

def get_all(db, tables):
    for table in tables:
        res = db.execute(f"Select * From {table}")
        data = res.fetchall()
        column_names = [description[0] for description in res.description]
        print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))
        
    return 
