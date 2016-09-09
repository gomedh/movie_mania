import media
import fresh_tomatoes

Rustam = media.Movie("Rustam","A movie based upon a true incident which changed the course of india judisicary",
	"http://t3.gstatic.com/images?q=tbn:ANd9GcT4H2JWKIA8a2_gGVSStPrGQNwGCJHbkbsx_q7Ue1cXN1k1wvC7",
	"https://www.youtube.com/watch?v=ndbDymVUvbQ")

Sultan = media.Movie("Sultan","A movie based upon a wrestlers journey",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcS1cK4t_uWmqHaRYD9uq69hLEWy7f7NpIfjPlQECdooplpkQcEp",
	"https://www.youtube.com/watch?v=wPxqcq6Byq0")

Mohenjo_daro = media.Movie("Mohenjo-daro","A movie based on premediveal period",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcS80mAtrrEQB4hgbfi6w-wLQI1N-EQ3tNuEgXU3fVK6XhDlocih",
	"https://www.youtube.com/watch?v=UPZ5FKEB02I")


Madaari = media.Movie("Madaari","A movie based upon the fight of a common indian man against the corrupt system",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcSDbkvgGHCrQMAyfx5TFB9DaIs5rTq4A-1c_r8NnMkLtANuFvgZ",
	"https://www.youtube.com/watch?v=j4s3JmLGLCA")

#can add more movies later on as stated above.

movies = [Rustam,Sultan,Mohenjo_daro,Madaari]
fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__

#print Rustam.storyline
#print Sultan.storyline
#print Mohenjo_daro.storyline

#Mohenjo_daro.show_trailer()
#Sultan.show_trailer()