#===============Import section:=====================
import spacy
nlp = spacy.load('en_core_web_md')

#===================Function========================
# Function will read this file and get a similiar movie to the compared sentence
def movie_similiar(compare_sentence):
    # Default values are set
    movies = {}
    movie = ""
    movie_line = ""
    movie_lines = []
    
    # Read the file to add certian part of the line to certian list
    with open("movies.txt","r+") as f:
        for line in f:
            lines_list = []
            lines_list = line.strip("\n").split(" ")
            movie = " ".join(lines_list[0:2])
            movie_line = " ".join(lines_list[3:])
            movie_lines.append(movie_line)
            # This dictionary will be used to call on the movie that is similiar to compared movie
            movies[movie_line] = movie
    
    # Changed sentence to nlp    
    model_sentence =  nlp(compare_sentence)

    list_similarities = []
    list_similarities_dict = {}
    # For loop is used to get similarities between movies and add the similarities to a list
    for sentence in movie_lines:
        similarity = nlp(sentence).similarity(model_sentence)
        list_similarities.append(similarity)
        list_similarities_dict[similarity] = sentence
    
    # Used the max function to get most similiar movie   
    max_similarity = max(list_similarities)
    # Used dictionary to get that certian movie and use it to get the movies name
    that_movie = list_similarities_dict[max_similarity]

    #Return the movie that is most similiar
    return print(movies[that_movie])

#=====================Execution of the function:==========================
compare_sentence = "Will he save their world or destroy it?When the Hulk becomes too dangerous for the Earth , the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as agladiator."
print("The most similiar movie is :")
movie_similiar(compare_sentence)