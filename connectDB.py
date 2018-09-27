# import sqlite3
#
#
# con = sqlite3.connect('dbConnect.db')
#
# if con:
#     print("Database connected Successfully")
#     con.execute('''
#       CREATE TABLE IF NOT EXISTS Comment(
#         ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
#         Comment TEXT NOT NULL
#       );
#     ''')
#     if con:
#         print("Table Created successfully")
#         # con.execute("INSERT INTO Comment(ID,Comment) VALUES (1,\"Umer Tariq\")")
#         # con.commit()
#         con.execute('DELETE FROM Comment WHERE ID=2')
#         con.commit()
#         cursor = con.execute('SELECT * FROM Comment')
#         for row in cursor:
#             print("ID = ",str(row[0]))
#             print("Comment = ",str(row[1]))
