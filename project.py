import media
import fresh_tomatoes

# Following are 6 objects of class Movie.
# This code makes an instance of Movie class and initialises it with 4 values
# as arguments which become title, storyline, poster_image_url and
# trailer_youtube_url of object.
The_Theory_Of_Everything = media.Movie("The Theory of Everything",
                                       "The Theory of Everything is the story "
                                       "of the most brilliant and celebrated p"
                                       "hysicist of our time, Stephen Hawking",
                                       "https://c1.staticflickr.com/1/741/"
                                       "32696525795_9d37c7db0e_q.jpg",
                                       "https://www.youtube.com/watch?v="
                                       "Salz7uGp72c")
Minions = media.Movie("Minions",
                      "The story of three minions(small, yellow creatures)"
                      " journey to New York.",
                      "https://c1.staticflickr.com/1/761/32696525405_799304dc1"
                      "c_q.jpg",
                      "https://www.youtube.com/watch?v=eisKxhjBnZ0")
Harry_Potter_and_the_Prisoner_of_Azkaban = media.Movie("Harry Potter and the "
                                                       "Prisoner of Azkaban",
                                                       "P"
                                                       "he book follows Harry "
                                                       "Potter, a young wizard"
                                                       ", in his third year at"
                                                       " Hogwarts School of Wi"
                                                       "tchcraft and Wizardry",
                                                       "https://c1.staticflic"
                                                       "kr.com/1/370/326557506"
                                                       "06_e30ce85acc_q.jpg",
                                                       "https://www.youtube.c"
                                                       "om/watch?v=lAxgztbYDbs"
                                                       )
Hotel_Transylvania = media.Movie("Hotel Transylvania",
                                 "Story of a Dracula, who operates a high-end"
                                 " resort away from the human world and a boy,"
                                 " who discovers the resort.",
                                 "https://c1.staticflickr.com/1/723/"
                                 "31853552714_789e5b25e2_q.jpg",
                                 "https://www.youtube.com/watch?v=q4RK3jY7AVk")
Orphan = media.Movie("Orphan",
                     "The plot centers on a couple who, after the death of "
                     "their unborn child, adopt a mysterious 9-year-old girl.",
                     "https://c1.staticflickr.com/1/321/32696441625_dd4cab3de0"
                     "_q.jpg",
                     "https://www.youtube.com/watch?v=2ywOPNNii9w")
Now_You_See_Me = media.Movie("Now You See Me",
                             "Story of an FBI agent and an Interpol detective "
                             "who track a team of illusionists who pull off "
                             "bank heists during their performances and reward"
                             " their audiences with the money.",
                             "https://c1.staticflickr.com/1/462/32696432895_5f"
                             "30d630ac_q.jpg",
                             "https://www.youtube.com/watch?v=KzJNYYkkhzc")
# list named movies that contains objects created above.
movies = [Minions, Hotel_Transylvania, Now_You_See_Me,
          The_Theory_Of_Everything, Harry_Potter_and_the_Prisoner_of_Azkaban,
          Orphan]
# list is passed as argument to open_movies_page function of fresh_tomatoes.
fresh_tomatoes.open_movies_page(movies)
