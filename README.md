# Information visualization in increasing filter bubble awareness
 - Main Aim: Increasing user's awareness of their filter bubble by showing them the information that is usually hidden from them (Blind-spots). 
 - Domain: Music (Millionsong Dataset) , Movies (Movielens data)
 - Data structure (Movielens): Movie lens data set contains four individual csv files with the structure as below:
  1. movies.csv with fields 'movieId','title','genres'. A movie can belong to multiple genres and each genre is seperated by a '|'.            Example row: 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
  2. ratings.csv with fields 'userId','movieId','ratings','timestamp'. Ratings are from 1 to 5. Example row: 1,31,2.5,1260759144
  3. tags.csv with fields 'userId','movieId','tags','timestamp'. Example row: 15,339,sandra 'boring' bullock,1138537770
  4. links.csv with fields 'movieId','imdbId','tmdbId'. Example row: 1,0114709,862
  For my analysis only movies.csv and ratings.csv are relevant. 
## Implementation steps: 
### Frequent itemset mining:
   - (Data preprocessing): For each row in ratings.csv, the genre of the movie is obtained from movies.csv and it is merged with 'userId', 'movieId' and 'ratings' column to create a new file 'usergenres.csv'.
   - For all the movies in usergenres.csv, most frequent genres are computed using frequent pattern mining algorithm. This is also called as 'global listening pattern'. **Pymining** package provides a collection of datamining algorithms in python fromw which the **frequent itemset mining algorithm** was used. It takes as input the 'genres' column of 'usergenres.csv' (after changing the format a bit and removing the '|'), and gives as output all the genres and genre combinations with their frequency value. Frequency denotes the number of times the genre or genre combination has been rated.
   - The next step is to obtain the frequent genre combination for a specific user ('user-specific listening pattern'). A dummy user (user2) was selected and the above step was carried out for all the movies rated by the specific user. This gives the most frequent genres/genre combinations and frequency for the specific user. Now we have the data required for plotting. Next step is to organize the data a bit before plotting. 
### Barchart: 
 - After computing the frequent genre combinations and their frequencies, I used a simple barchart to compare the global and user specific listening pattern. For ease of representation, I chose the top 20 frequent genre/combinations each from global and user-specific patterns. Before plotting, the frequency values were normalized to lie between range [0,1]. Screenshots: [global](https://github.com/jayachithra/Recsys/blob/master/code/barchart_global.JPG) and [user-specific](https://github.com/jayachithra/Recsys/blob/master/code/barchart_user.JPG)
 
### Data Processing: 
   - I created a 'frequent_genres.csv' file to put all the data together in one place and give them some structure. The file has the following fields: "genres","frequency","norm_frequency","ratings","user". 

