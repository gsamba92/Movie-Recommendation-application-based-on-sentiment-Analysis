import sqlite3 as lite

def createTable():
    try:
       
        conn.execute('CREATE TABLE IF NOT EXISTS WATCHLIST(movie_ID INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, img TEXT NOT NULL, rating TEXT NOT NULL, isWatch INTEGER);')
        print("Table created successfully.")
        
    except Exception as e:
        print("\n Error in creating Table. Table already exists.%s" % e.args[0])
        exit()

def insertMovies(data):
    try:
        for i,j,k in data:
            values=(i,j,k,0)
            conn.execute("INSERT INTO WATCHLIST (title,img,rating,isWatch) VALUES (?,?,?,?)",values)
            conn.commit()
  
    except Exception:
        conn.rollback()
        print("Error:", name, ".The contact already exists.")


def fetchWatchlist():
    try:
        saved = []
        cur.execute("SELECT * FROM WATCHLIST WHERE isWatch=1")
        rows = cur.fetchall()
        for movie in rows:
            saved.append(movie)
        return saved
    except Exception:
        return 0

def fetchMovies():
    try:
        movies = []
        value = 0
        cur.execute("SELECT * FROM WATCHLIST WHERE isWatch=0")
        rows = cur.fetchall()
        for movie in rows:
            movies.append(movie)
        return movies
    except Exception as e:
        print(e)
        return 0

def updateMovie(movieid):
    try:
        values=(1,movieid)
        cur.execute(
            "UPDATE WATCHLIST SET isWatch=? WHERE movie_ID=?",values)
        conn.commit()
   
    except Exception:
        conn.rollback()
        print("Error in updating the contact")

def dropTable():
     conn.execute('DROP TABLE IF EXISTS WATCHLIST')
     conn.commit()
     print("Table dropped")
conn = None



try:
    conn = lite.connect('watchlist.db')
    cur = conn.cursor()  
    

except lite.Error as e:
    print ("Error %s" % e.args[0])
    sys.exit(1)
