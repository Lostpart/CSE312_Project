def drop_table(database, table: str):
    if table in database.list_collection_names():
        expect_table = database[table]
        expect_table.drop()
        # message = "Table " + table + "dropped"
        return True
    else:
        error_message = "Table " + table + " doesn't exist"
        return error_message