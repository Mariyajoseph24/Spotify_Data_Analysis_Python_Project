#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sp_tracks = pd.read_csv('D:/spotifydata/tracks.csv')
sp_feature = pd.read_csv('D:/spotifydata/SpotifyFeatures.csv')


# In[3]:


#viewing the tracks data
sp_tracks.head()


# In[4]:


#viewing the feature data
sp_feature.head()


# In[5]:


#checking null
pd.isnull(sp_tracks).sum()


# In[6]:


pd.isnull(sp_feature).sum()


# In[7]:


#checking info
sp_tracks.info()


# In[8]:


#checking info
sp_feature.info()


# In[9]:


#finding 10 least popular songs in the spotify dataset
a=sp_tracks.sort_values('popularity',ascending=True)[0:10]
a[['name','popularity']]


# In[10]:


#descriptive statistics of tracks
sp_tracks.describe().transpose()


# In[11]:


#descriptive of feature
sp_feature.describe().transpose()


# In[12]:


#finding top 10 popular songs in the spotify dataset
a=sp_tracks
b=a[a['popularity']>90].sort_values('popularity',ascending=False)[:10]
b[['name','popularity','artists']]


# In[13]:


#Make the Release Date Column as the Index Column.
sp_tracks.set_index('release_date',inplace=True)
sp_tracks.index=pd.to_datetime(sp_tracks.index)
sp_tracks.head()


# In[14]:


#Find the Name of the Artist Present in the 18th Row of the Dataset.
sp_tracks[['artists']].iloc[18]


# In[15]:


#Convert the Duration of the Songs From Milliseconds to Seconds.
sp_tracks['duration'] = sp_tracks['duration_ms'].apply (lambda x : round(x/1000))
sp_tracks.drop('duration_ms', inplace = True, axis=1)
sp_tracks.duration.head()


# In[16]:


#Correlation HeatMap using Pearson Correlation method between two variables
td = sp_tracks.drop(['key','mode','explicit'], axis=1).corr(method = 'pearson')
plt.figure(figsize=(9,5))
hmap = sns.heatmap(td, annot = True, fmt = '.1g', vmin=-1, vmax=1, center=0, cmap='Greens', linewidths=0.1, linecolor='black')
hmap.set_title('Correlation HeatMap')
hmap.set_xticklabels(hmap.get_xticklabels(), rotation=90)


# In[17]:


#Sample Only 4 Percent of the Whole Dataset.
sample_sp=sp_tracks.sample(int(0.004*len(sp_tracks)))
print(len(sample_sp))


# In[18]:


#Create a Regression Plot Between Loudness and Energy. Let’s Plot It  in the Form of a Regression Line.
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='loudness', x='energy', color='#054907').set(title='Regression Plot - Loudness vs Energy Correlation')


# In[19]:


#Create a Regression Plot Between Popularity and Acousticness in the Form of a Regression Line.
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='popularity', x='acousticness', color='#008000').set(title='Regression Plot - Popularity vs Acousticness Correlation')


# In[20]:


#creating new column in tracks table
sp_tracks['dates']=sp_tracks.index.get_level_values('release_date')
sp_tracks.dates=pd.to_datetime(sp_tracks.dates)
years=sp_tracks.dates.dt.year
sp_tracks.head()


# In[21]:


sns.displot(years, discrete=True, aspect=2, height=4, kind='hist',color='g').set(title='No of songs - per year')


# In[22]:


#Plot a Line Graph to Show the Duration of the Songs for Each Year.
total_dr = sp_tracks.duration
fig_dims = (15,5)
fig, ax = plt.subplots(figsize=fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title='Years vs Duration')
plt.xticks(rotation=90)


# In[27]:


#spotify feature analysis

#Plot Duration of the Songs w.r.t. different Genres using a horizontal barplot.
plt.title('Duration of songs in different Genres')
sns.color_palette('crest', as_cmap=True)
sns.barplot(y='genre', x='duration_ms', data=sp_feature)
plt.xlabel('Duration in ms')
plt.ylabel('Genres')


# In[33]:


#Find top five genres by Popularity and pot a barplot for the same.
sns.set_style(style='darkgrid')
plt.figure(figsize=(8,4))
Top = sp_feature.sort_values('popularity', ascending=False)[:10]
sns.barplot(y = 'genre', x = 'popularity', data = Top).set(title='Genres by Popularity-Top 5')


# In[ ]:




