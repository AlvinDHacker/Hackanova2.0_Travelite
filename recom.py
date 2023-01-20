import numpy as np
import pandas as pd 

#Importing the data 
#Need to connect the data bases here 
book=pd.read_csv('Books.csv') 
ratings=pd.read_csv('Ratings.csv') 
users=pd.read_csv('Users.csv')

ratings_with_name=ratings.merge(book,on='ISBN')

num_rating_df=ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)

avg_rating_df=ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()
avg_rating_df.rename(columns={'Book-Rating':'avg_ratings'},inplace=True)

popular_df=num_rating_df.merge(avg_rating_df,on='Book-Title')
popular_df=popular_df[popular_df['num_ratings']>250].sort_values('avg_ratings',ascending=False)
popular_df.merge(book,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_ratings']]


x=ratings_with_name.groupby('User-ID').count()['Book-Rating']>200
stud_ppl=x[x].index
filt_rat=ratings_with_name[ratings_with_name['User-ID'].isin(stud_ppl)]

y=filt_rat.groupby('Book-Title').count()['Book-Rating']>=50
fam_book=y[y].index
final_ratings=filt_rat[filt_rat['Book-Title'].isin(fam_book)]
final_ratings.drop_duplicates()

pt=final_ratings.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')

pt.fillna(0,inplace=True)

from sklearn.metrics.pairwise import cosine_similarity
sim_score=cosine_similarity(pt)
print(sim_score)

def recommend(book_name):
    index=np.where(pt.index==book_name)[0][0]
    similar_items=sorted(list(enumerate(sim_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    for i in similar_items:
        print(pt.index[i[0]])

 