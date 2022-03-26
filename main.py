from website import create_app
import flask
import difflib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = create_app()

df2 = pd.read_csv('./model/tmdb.csv')

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])
all_titles = [df2['title'][i] for i in range(len(df2['title']))]

def get_recommendations(title):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    gen = df2['genres'].iloc[movie_indices]
    tag = df2['tagline'].iloc[movie_indices]
    hom = df2['homepage'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title','Year','Genres', 'Tagline', 'Homepage'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return_df['Genres'] = gen
    return_df['Tagline'] = tag
    return_df['Homepage'] = hom
    return return_df

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name']
        m_name = m_name.title()
        if m_name not in all_titles:
            return(flask.render_template('negative.html',name=m_name))
        else:
            result_final = get_recommendations(m_name)
            names = []
            dates = []
            genres = []
            tagline = []
            homepage = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                dates.append(result_final.iloc[i][1])
                genres.append(result_final.iloc[i][2])
                tagline.append(result_final.iloc[i][3])
                homepage.append(result_final.iloc[i][4])

            return flask.render_template('results.html',movie_names=names,movie_date=dates,movie_genres=genres,movie_tagline=tagline,movie_homepage=homepage,search_name=m_name)

if __name__ == '__main__':
    app.run(debug=True)
    