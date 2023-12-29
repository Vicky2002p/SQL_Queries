from cs50 import SQL

db = SQL("sqlite:///database.db")

db.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age NUMBER, fav_food STRING)")

db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "eesa", 14, "pizza")

db.execute("INSERT INTO users (name, age, fav_food) VALUES(?, ?, ?)", "bob", 20, "burgers")

db.execute("UPDATE users SET fav_food='shawarma' WHERE name='eesa'")

db.execute("DELETE FROM users WHERE name='bob'") # goodbye bob

people = db.execute("SELECT * FROM users")
print(people) # [{'name': 'eesa', 'age': 14, 'fav_food': 'shawarma'}]
