from numpy.lib.shape_base import split


class movie:
    def __init__(self,movie_id,movie_title,release_date,video_release_date,IMDB_URL,Types):
       self.movie_id=movie_id
       self.movie_title=movie_title
       self.release_date=release_date
       self.video_release_date=video_release_date
       self.IMDB_URL=IMDB_URL
       self.Types=Types
    
    def printMovieInfor(self):
        print("movie id="+str(self.movie_id))
        print("movie title="+self.movie_title)
        print("release data="+self.release_date)
        print("video release date="+self.video_release_date)
        print("IMDB URL="+self.IMDB_URL)
        print("type="+self.Types)


def getTypes(string):
    splits=string.split('|') 
    types=""

    if splits[0]=='1':
        types+="unknown,"
    if splits[1]=='1':
        types+="Action,"
    if splits[2]=='1':
        types+="Adventure,"
    if splits[3]=='1':
        types+="Animation,"
    if splits[4]=='1':
        types+="Children's,"
    if splits[5]=='1':
        types+="Comedy,"
    if splits[6]=='1':
        types+="Crime,"
    if splits[7]=='1':
        types+="Documentary,"
    if splits[8]=='1':
        types+="Drama," 
    if splits[9]=='1':
        types+="Fantasy," 
    if splits[10]=='1':
        types+="Film-Noir," 
    if splits[11]=='1':
        types+="Horror," 
    if splits[12]=='1':
        types+="Musical," 
    if splits[13]=='1':
        types+="Mystery," 
    if splits[14]=='1':
        types+="Romance," 
    if splits[15]=='1':
        types+="Sci-Fi," 
    if splits[16]=='1':
        types+="Thriller," 
    if splits[17]=='1':
        types+="War," 
    if splits[18]=='1':
        types+="Western," 

    return types[:-1]