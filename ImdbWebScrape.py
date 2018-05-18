# Python3 code for movie
# recommendation based on
# emotion

# Import library for web
# scrapping
from bs4 import BeautifulSoup as SOUP
import requests as HTTP

# Function for scraping
def getMovies(emotion):
        urlhere="No url"
        data = []
	# IMDb Url for Drama genre of
	# movie against emotion Sad
        if(emotion == "Sad"):
                urlhere = 'http://www.imdb.com/search/title?genres=drama&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Musical genre of
	# movie against emotion Disgust
        elif(emotion == "Disgust"):
                urlhere = 'http://www.imdb.com/search/title?genres=musical&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Family genre of
	# movie against emotion Anger
        elif(emotion == "Angry"):
                urlhere = 'http://www.imdb.com/search/title?genres=family&amp;title_type=feature&amp;sort=moviemeter, asc'


	# IMDb Url for Thriller genre of
	# movie against emotion Anticipation
        elif(emotion == "Anticipation"):
                urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Sport genre of
	# movie against emotion Fear
        elif(emotion == "Surprised"):
                urlhere = 'http://www.imdb.com/search/title?genres=sport&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Thriller genre of
	# movie against emotion Enjoyment
        elif(emotion == "Happy"):
                urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Western genre of
	# movie against emotion Trust
        elif(emotion == "Trust"):
                urlhere = 'http://www.imdb.com/search/title?genres=western&amp;title_type=feature&amp;sort=moviemeter, asc'

	# IMDb Url for Film_noir genre of
	# movie against emotion Surprise
        elif(emotion == "Surprise"):
                urlhere = 'http://www.imdb.com/search/title?genres=film_noir&amp;title_type=feature&amp;sort=moviemeter, asc'
        if(urlhere != "No url"):
                
                # HTTP request to get the data of
                # the whole page
                response = HTTP.get(urlhere)
                data = response.text

                # Parsing the data using
                # BeautifulSoup
                soup = SOUP(data, "lxml")

                # Extract movie titles from the
                # data using regex
                
                samples = soup.find_all("div", "lister-item")
                ratings = soup.find_all("div","ratings-bar")
                #print(ratings[0].contents[1].attrs['data-value'])
                #data = []
                name = []
                img = []
                rating = []
                for a in samples:
                    name.append(a.contents[5].contents[1].contents[3].text)
                    img.append(a.contents[3].contents[1].contents[1].attrs['loadlate'])
                    
                for rate in ratings:
                    rating.append(rate.contents[1].attrs['data-value'])
                    

                data = zip(name,img,rating)
                data = list(data)                
        return data

# Driver Function
"""if __name__ == '__main__':

    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0
 
    if(emotion == "Happy" or emotion == "Angry"
                           or emotion=="Surprise"):
       
        for i in a:
            
            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split('>;')
 
            if(count > 13):
                break
            count += 1
            #print(tmp)
    else:
        for i in a:
            tmp = str(i).split('>')
 
            if(len(tmp) == 3):
                print(tmp[1][:-3])
 
            if(count > 11):
                break
            count+=1
"""
