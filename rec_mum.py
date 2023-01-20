#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 

place=pd.read_csv('last_mum.csv')
ratings=pd.read_csv('rat_mum.csv')


# In[2]:


ratings_with_name=ratings.merge(place,on='id')
print(ratings_with_name)


# In[4]:


ratings_with_name.groupby('name').count()['no_votes'].reset_index()


# In[5]:


avg_rating_df=ratings_with_name.groupby('name').mean()['rating'].reset_index()
avg_rating_df.rename(columns={'rating':'avg_ratings'},inplace=True)
print(avg_rating_df)


# In[6]:


num_rating_df=ratings_with_name.groupby('name').count()['rating'].reset_index()
num_rating_df.rename(columns={'rating':'num_ratings'},inplace=True)
avg_rating_df=ratings_with_name.groupby('name').mean()['rating'].reset_index()
avg_rating_df.rename(columns={'rating':'avg_ratings'},inplace=True)
print(avg_rating_df)


# In[7]:


popular_df=num_rating_df.merge(avg_rating_df,on='name')
popular_df=popular_df[popular_df['avg_ratings']>4].sort_values('avg_ratings',ascending=False)


# In[10]:


popular_df=popular_df.merge(ratings_with_name,on='name')


# In[11]:


print(popular_df)


# In[ ]:




