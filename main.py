from flask import Flask,request,render_template
#user-defined modules
import ImdbWebScrape
import CaptureImage
import CloudVisionAnaylsis
import watchlist_db

app = Flask(__name__)

#Capture User Picture
CaptureImage.clickPicture()
#Run analysis with Google Cloud Vision Api
emotion = CloudVisionAnaylsis.getSentiment()

#Get scraped data by passing the emotion state to imdb website
data = ImdbWebScrape.getMovies(emotion)

#Storing in database
watchlist_db.dropTable()
watchlist_db.createTable()
watchlist_db.insertMovies(data)




@app.route("/")
def index():
    movies = []
    img = '/static/output_'+emotion+'.jpeg'
    movies=watchlist_db.fetchMovies()
    return render_template("index.html",movies=movies,emotion=emotion,img=img)
@app.route("/test")
def test():

    return render_template("test.html",data=data)

@app.route("/watchlist")
def watchlist():
    movies = []
    movies=watchlist_db.fetchWatchlist()
    return render_template("watchlist.html",movies=movies)

@app.route("/<int:id>")
def updateWatchlist(id):
    movies = []
    img = '/static/output_'+emotion+'.jpeg'
    watchlist_db.updateMovie(id)
    movies=watchlist_db.fetchMovies()   
    return render_template("index.html",movies=movies,emotion=emotion,img=img,id=id)

if __name__ == '__main__':
    app.run()
