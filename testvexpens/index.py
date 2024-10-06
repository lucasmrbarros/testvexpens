import pandas
import matplotlib.pyplot as plt

# Loading the data
data = pandas.read_csv('netflix_titles.csv')

# Filter for movies
movies = data[data['type'] == 'Movie']

# Count the number of movies
num_movies = len(movies)

# Group by director and count the number of movies/series
director_counts = data['director'].value_counts()

# Get the top 5 directors
top_5_directors = director_counts.head(5)

# Drop rows with NaN values in 'cast' or 'director' columns
data = data.dropna(subset=['cast', 'director'])

# Force 'cast' and 'director' columns into strings
data['cast'] = data['cast'].astype(str)
data['director'] = data['director'].astype(str)

# Filter for directors who worked on their own productions
own_productions = data[data.apply(lambda row: row['director'] in row['cast'], axis=1)]

# Get the unique directors, remove 'nan', and sort alphabetically
directors_own_productions = sorted([director for director in own_productions['director'].unique() if director != 'nan'])

#show the columns
print("Columns:")
print(data.columns)
print("_____________________________________")

#Show  the ammoount of movies
print(f"There are: {num_movies} movies on Netflix")
print("_____________________________________")


#show the top 5 directors
print("Top 5 directors with the most movies and series:")
print(top_5_directors)
print("_____________________________________")


#Show the directors that worked on their own productions
print("Directors who worked on their own productions:")
print(directors_own_productions)

###############Insights Zone#############################

# Extract the year from the 'date_added' column
data['year_added'] = data['date_added'].str[-4:].astype('Int64')

# Drop rows with NaN values in 'year_added'
data = data.dropna(subset=['year_added'])

#####Cast related stuff########

# Drop rows with NaN values in 'cast'
data = data.dropna(subset=['cast'])

# Split the 'cast' column into individual cast members
cast_members = data['cast'].str.split(', ').explode()

# Group by cast member and count the number of appearances
cast_counts = cast_members.value_counts()

# Get the top 5 cast members
top_5_cast_members = cast_counts.head(5)

# Function to get top 5 cast members for a given type
def get_top_5_cast(data, content_type):
    filtered_data = data[data['type'] == content_type]
    cast_members = filtered_data['cast'].str.split(', ').explode()
    cast_counts = cast_members.value_counts()
    return cast_counts.head(5)

# Get top 5 cast members for movies
top_5_cast_movies = get_top_5_cast(data, 'Movie')
print("Top 5 cast members with the most appearances in Movies:")
print(top_5_cast_movies)
print("_____________________________________")

# Get top 5 cast members for TV shows
top_5_cast_tv_shows = get_top_5_cast(data, 'TV Show')
print("Top 5 cast members with the most appearances in TV Shows:")
print(top_5_cast_tv_shows)

# Display the top 5 cast members
print("Global Top 5 cast members with the most appearances:")
print(top_5_cast_members)

##########Graphics####################


# Group by the extracted year and type
grouped_data = data.groupby(['year_added', 'type']).size().unstack(fill_value=0)

''''
# Plotting the data
plt.figure(figsize=(14, 8))
grouped_data.plot(kind='bar', stacked=False, width=0.8)

# Adding titles and labels
plt.title('Number of Movies and TV Shows Added per Year')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Type')
plt.tight_layout()

# Show the plot
plt.show()
'''