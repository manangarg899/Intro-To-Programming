#import statement import different files that are to be used.
#here imported file fresh_tomatoes file is imported to make website from given data in this file.
#media is also used to make website.It is a file which is used to create different variables of movies like title,storyline etc..
import fresh_tomatoes
import media
#here we are adding properties of a movie like title,storyline,poster image link,youtube trailer link,and runtime of movie in a variable.
#pink is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
pink = media.Movie("Pink",
                   "A lawyer with wild mood swings helps three women sue the men who attacked them.",
                   "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ-ROm_VcWvzz-0Br5d6obk0fK9XC1QbBz9YGmrRTG68Nu3SUOi",
                   "https://www.youtube.com/watch?v=AL2TShb6fFs",
                   "2h 16m")
#The_Intern is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
The_Intern = media.Movie("The Intern",
                   "Seventy-year-old Ben Whittaker realises that retirement isn't an enjoyable experience. As a result, he decides to work as an intern at an online fashion store managed by an extremely sceptical boss.",
                   "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAADn_UURWZcEX05pIofVnAOmpWaxM_cOEkTT0xJ9RPCVhNcnAUw",
                   "https://www.youtube.com/watch?v=ZU3Xban0Y6A",
                   "2h 1m")
#Inception is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
Inception = media.Movie("Inception",
                   "Cobb steals information from his targets by entering their dreams. He is wanted for his alleged role in his wife's murder and his only chance at redemption is to perform the impossible, an inception.",
                   "http://www.impawards.com/2010/posters/inception.jpg",
                   "https://www.youtube.com/watch?v=YoHD9XEInc0",
                   "2h 28m" )
#ms_Dhoni is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
ms_Dhoni = media.Movie("M.S Dhoni",
                   "Mahendra Singh Dhoni is an Indian cricketer and the current captain of the Indian national cricket team in limited-overs formats.",
                   "http://i.imgur.com/tYG8ZpK.jpg",
                   "https://www.youtube.com/watch?v=6L6XqWoS8tw",
                   "3h 10m")
#captain_america is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
captain_america = media.Movie("Captain America:Civil War",
                   "Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage. The new status quo deeply divides members of the team. Captain America (Chris Evans) believes superheroes should remain free to defend humanity without government interference. Iron Man (Robert Downey Jr.) sharply disagrees and supports oversight. As the debate escalates into an all-out feud, Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner) must pick a side.",
                   "https://i.jeded.com/i/captain-america-civil-war.44269.jpg",
                   "https://www.youtube.com/watch?v=dKrVegVI0Us",
                   "2h 27m")
#Deadpool is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
Deadpool = media.Movie("Deadpool",
                   "Wade Wilson (Ryan Reynolds) is a former Special Forces operative who now works as a mercenary. His world comes crashing down when evil scientist Ajax (Ed Skrein) tortures, disfigures and transforms him into Deadpool. The rogue experiment leaves Deadpool with accelerated healing powers and a twisted sense of humor. With help from mutant allies Colossus and Negasonic Teenage Warhead (Brianna Hildebrand), Deadpool uses his new skills to hunt down the man who nearly destroyed his life.",
                   "http://i.imgur.com/uvlFQrT.jpg",
                   "https://www.youtube.com/watch?v=ZIM1HydF9UA&oref=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DZIM1HydF9UA&has_verified=1",
                   "1h 48m")
#me_befor_you is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
me_befor_you = media.Movie("Me Before You",
                   "Young and quirky Louisa 'Lou' Clark (Emilia Clarke) moves from one job to the next to help her family make ends meet. Her cheerful attitude is put to the test when she becomes a caregiver for Will Traynor (Sam Claflin), a wealthy young banker left paralyzed from an accident two years earlier. Will's cynical outlook starts to change when Louisa shows him that life is worth living. As their bond deepens, their lives and hearts change in ways neither one could have imagined.",
                   "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSu-AX8VWfLNkbuzQSHmVrSTaIXcK1LMGjNRIh7UtvV90Vrl39m",
                   "https://www.youtube.com/watch?v=Eh993__rOxA",
                   "1h 50m")
#inside_out is a variable which is also the movie title here and other items in the list are storyline,poster image link,youtube trailer link,and runtime of movie.
inside_out = media.Movie("Inside Out",
                   "Eleven-year-old Riley has moved to San Francisco, leaving behind her life in Minnesota. She and her five core emotions, Fear, Anger, Joy, Disgust and Sadness, struggle to cope with her new life.",
                   "https://i.jeded.com/i/inside-out-2015.36698.jpg",
                   "https://www.youtube.com/watch?v=seMwpP0yeu4",
                   "1h 42m")
#here we created an list(movies) of movie name variables which indicate different movie title variable and is used to access data of that movie.
movies = [pink,The_Intern,Inception,ms_Dhoni,captain_america,Deadpool,me_befor_you,inside_out]
#this statement is used to access fresh_tomatoes file and finally create the website and values are passed in the form of list and for every variable i.e movie in list a poster with specifications is generated on website.
fresh_tomatoes.open_movies_page(movies)
