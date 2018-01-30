# Information visualization in increasing filter bubble awareness
Main Aim: Increasing user's awareness of their filter bubble by showing them the information that is usually hidden from them (Blind-spots). 
Domain: Music (Millionsong Dataset) , Movies (Movielens data)
Data structure (Movielens): Movie lens data set contains four individual csv files with the structure as below:
  1. movies.csv with fields 'movieId','title','genres'. A movie can belong to multiple genres and each genre is seperated by a '|'.            Example row: 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
  2. ratings.csv with fields 'userId','movieId','ratings','timestamp'. Ratings are from 1 to 5. Example row: 1,31,2.5,1260759144
  3. tags.csv with fields 'userId','movieId','tags','timestamp'. Example row: 15,339,sandra 'boring' bullock,1138537770
  4. links.csv with fields 'movieId','imdbId','tmdbId'. Example row: 1,0114709,862
  For my analysis only movies.csv and ratings.csv are relevant. 
##Implementation steps: 
###Data preprocessing
