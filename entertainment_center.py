import media
import fresh_tomatoes
# create the interstellar instance
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole \
                            in space in an attempt \
                            to ensure humanity's survival.",
                           "http://i2.muimg.com/588926/64a43aba36cb7a0d.jpg",
                           "https://www.youtube.com/watch?v=480Z_brE6Qs")

movie = [interstellar]
# translate the data into HTML , produce a HTML file ,then open the file
fresh_tomatoes.open_movies_page(movie)
