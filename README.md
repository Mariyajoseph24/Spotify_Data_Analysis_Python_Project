<h1>Spotify Data Analysis Python Project</h1>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/43749cf9-4eb1-476c-89ea-bf1625b17168">
<h1>Contents</h1>
<ul>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#importrequiredlibraries">Import Required Libraries</a></li>
  <li><a href="#exploringthedataset">Exploring the Dataset</a></li>
  <li><a href="#identifyingnullvaluesinthedataset">Identifying Null Values in the Dataset</a></li>
  <li><a href="#datasetoverviewrowscolumnsdatatypesandmemoryusage">Dataset Overview: Rows, Columns, Data Types, and Memory Usage</a></li>
  <li><a href="#extractinginsightsfromthedatasetthroughanalysis">Extracting Insights from the Dataset through Analysis</a></li>
</ul>

<h1><a name="introduction">Introduction</a></h1>
<p>The Spotify Data Analysis Project: In todays changing world data analysis has become crucial in fields such, as business, research and meteorology. This project showcases the role that data plays in making decisions advancing research initiatives and even predicting weather patterns.

  The immense potential of data analysis is evident in this project, which focuses on extracting insights from music related datasets using Python. At its core Spotify takes stage as an audio streaming giant with captivating features like seamless song sharing and synchronized lyrics display.

Throughout this project I delved into the realm of data using Pythons libraries and functions. From analyzing to visualizing the data this project covers all aspects of data processing. The interactive environment provided by Jupyter notebook enhanced my experience by allowing me to engage with the data and discover patterns.

Through the Spotify Data Analysis Project I not sharpened my skills but also gained a deep understanding of how data intertwines, with the world of music. This journey provided insights. Equipped me with confidence to undertake similar projects in the future.

<p>Feel free to reach out for any questions or suggestions about this project. I'm open to discussions and eager to assist.
 <a href="https://www.linkedin.com/in/mariya-jos/">
  <img src=" Linkedln | Mariya Joseph" alt=""> Linkedln | Mariya Joseph</a><br>
  
  Don't forget to follow and star ⭐ the repository if you find it valuable.</p>

<ul>Tools Used🛠️:<br>
<li>Programming Language: Python<br></li>
<li>Libraries: Pandas, Numpy, Matplotlib, Seaborn<br></li>
<li>IDE: Jupyter Notebook<br></li></ul>

Dataset: <a href="https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=artists.csv">
         <img src=" Spotify Dataset" alt=""> Spotify Dataset</a><br>
</p>

  <h1><a name="importrequiredlibraries">Import Required Libraries</a></h1>
  
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
<ul>
  <li><code>import numpy as np</code>: This imports the NumPy library and aliases it as 'np'. NumPy is used for numerical computations and provides support for arrays and matrices.</li>
  <li><code>import pandas as pd</code>: This imports the Pandas library and aliases it as 'pd'. Pandas is used for data manipulation and analysis, providing data structures like DataFrames for tabular data.</li>
  <li><code>import matplotlib.pyplot as plt</code>: This imports the Pyplot module from the Matplotlib library and aliases it as 'plt'. Matplotlib is a popular plotting library in Python, and Pyplot provides a convenient interface to create visualizations.</li>
  <li><code>import seaborn as sns</code>: This imports the Seaborn library and aliases it as 'sns'. Seaborn is built on top of Matplotlib and offers a higher-level interface for creating attractive statistical visualizations.</li>
</ul>


  <h1><a name="exploringthedataset">Exploring the Dataset</a></h1>

```python
sp_tracks = pd.read_csv('D:/spotifydata/tracks.csv')
sp_feature = pd.read_csv('D:/spotifydata/SpotifyFeatures.csv')
```
<ul>
  <li><code>sp_tracks = pd.read_csv('D:/spotifydata/tracks.csv')</code>: This line reads a CSV file named 'tracks.csv' located at the 'D:/spotifydata/' directory and loads its data into a Pandas DataFrame called <code>sp_tracks</code>. This DataFrame is likely to contain information about tracks.</li>
  <li><code>sp_feature = pd.read_csv('D:/spotifydata/SpotifyFeatures.csv')</code>: This line reads another CSV file named 'SpotifyFeatures.csv' from the same directory and loads its data into a separate Pandas DataFrame called <code>sp_feature</code>. This DataFrame probably contains additional features or attributes related to the Spotify tracks.</li>
</ul>

```python
#viewing the tracks data
sp_tracks.head()
```
<p>NOTE:The image provided is not the entirety of the complete image, as there are restrictions in capturing full images through screenshots. To access the comprehensive table, please refer to the Jupyter notebook folder within this repository.</p>
<h6>Answer:</h6>
<img width="500" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/b778a861-fbf5-49ec-87f8-54f6db2c5721">
<ul>
  <li><code>#viewing the tracks data</code>: This is a comment that indicates the following line of code is meant to display or view the data in the 'sp_tracks' DataFrame.</li>
  <li><code>sp_tracks.head()</code>: This line of code calls the <code>head()</code> method on the 'sp_tracks' DataFrame. The <code>head()</code> method is used to display the first few rows of the DataFrame. This is useful for quickly getting an overview of the data.</li>
</ul>

```python
#viewing the feature data
sp_feature.head()
```
<p>NOTE:The image provided is not the entirety of the complete image, as there are restrictions in capturing full images through screenshots. To access the comprehensive table, please refer to the Jupyter notebook folder within this repository.</p>
<h6>Answer:</h6>
<img width="500" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/11c99ded-b241-485d-a618-ba8b17c7ed75">
<ul>
  <li><code>#viewing the feature data</code>: This is a comment that indicates the following line of code is intended to display or view the data in the 'sp_feature' DataFrame.</li>
  <li><code>sp_feature.head()</code>: This line of code calls the <code>head()</code> method on the 'sp_feature' DataFrame. The <code>head()</code> method is used to display the first few rows of the DataFrame. This allows you to quickly inspect the initial records and get a sense of the data.</li>
</ul>


  <h1><a name="identifyingnullvaluesinthedataset">Identifying Null Values in the Dataset</a></h1>

```python
#checking null in tracks data
pd.isnull(sp_tracks).sum()
```

<h6>Answer:</h6>
<img width="200" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/891dc6d1-7ad4-42b4-be19-d04c5db990ea">
<ul>
  <li><code>#checking null in tracks data</code>: This comment indicates that the following line of code is used to identify and count the missing (null) values in the 'sp_tracks' DataFrame.</li>
  <li><code>pd.isnull(sp_tracks).sum()</code>: This line of code uses the <code>pd.isnull()</code> function on the 'sp_tracks' DataFrame to create a boolean DataFrame where each cell contains <code>True</code> if the corresponding cell in the original DataFrame is null and <code>False</code> otherwise. The <code>.sum()</code> function is then used to count the number of <code>True</code> values in each column, effectively giving you the count of missing values in each column.</li>
</ul>

```python
#checking null in feature data
pd.isnull(sp_feature).sum()
```

<h6>Answer:</h6>
<img width="200" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/11bf6cd1-ec0f-43c0-9ce8-fb9b721b930e">
<ul>
  <li><code>#checking null in feature data</code>: This comment indicates that the following line of code is intended to identify and count the missing (null) values in the 'sp_feature' DataFrame.</li>
  <li><code>pd.isnull(sp_feature).sum()</code>: This line of code uses the <code>pd.isnull()</code> function on the 'sp_feature' DataFrame to create a boolean DataFrame where each cell contains <code>True</code> if the corresponding cell in the original DataFrame is null and <code>False</code> otherwise. The <code>.sum()</code> function is then used to count the number of <code>True</code> values in each column, effectively giving you the count of missing values in each column.</li>
</ul>

  <h1><a name="datasetoverviewrowscolumnsdatatypesandmemoryusage">Dataset Overview: Rows, Columns, Data Types, and Memory Usage</a></h1>

```python
#checking info in tracks data
sp_tracks.info()
```

<h6>Answer:</h6>
<img width="300" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/d8436fee-1e13-4c39-9ddf-abfba1cc8b34">
<ul>
  <li><code>#checking info in tracks data</code>: This comment indicates that the following line of code is meant to display information about the 'sp_tracks' DataFrame.</li>
  <li><code>sp_tracks.info()</code>: This line of code calls the <code>info()</code> method on the 'sp_tracks' DataFrame. The <code>info()</code> method provides a concise summary of the DataFrame, including the data types of each column, the number of non-null values, and memory usage. It's a useful way to get a quick overview of the data and its structure.</li>
</ul>


```python
#checking info in feature data
sp_feature.info()
```
<h6>Answer:</h6>
<img width="300" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/f5321efd-cceb-45e4-a7ac-ad3b201638cd">
<ul>
  <li><code>#checking info in feature data</code>: This comment indicates that the following line of code is intended to display information about the 'sp_feature' DataFrame.</li>
  <li><code>sp_feature.info()</code>: This line of code calls the <code>info()</code> method on the 'sp_feature' DataFrame. The <code>info()</code> method provides a concise summary of the DataFrame, including the data types of each column, the number of non-null values, and memory usage. This summary helps you understand the structure and content of the DataFrame.</li>
</ul>

----------------------------------------------------------------------------
  <h1><a name="extractinginsightsfromthedatasetthroughanalysis">Extracting Insights from the Dataset through Analysis</a></h1>
  <ol>
  <li>Exploring the 10 Least Popular Songs in the Spotify Dataset</li>

  ```python
a=sp_tracks.sort_values('popularity',ascending=True)[0:10]
a[['name','popularity']]
```
  <li>Descriptive Statistics </li>

```python
#descriptive statistics of tracks
sp_tracks.describe().transpose()
```
```python
#descriptive of feature
sp_feature.describe().transpose()
```
  <li>Discovering the Top 10 Popular Songs in the Spotify Dataset</li>

```python
a=sp_tracks
b=a[a['popularity']>90].sort_values('popularity',ascending=False)[:10]
b[['name','popularity','artists']]
```
  <li>Setting Release Date as the Index Column</li>

```python
sp_tracks.set_index('release_date',inplace=True)
sp_tracks.index=pd.to_datetime(sp_tracks.index)
sp_tracks.head()
```
  <li>Extracting Artist Name from the 18th Row of the Dataset</li>

```python
sp_tracks[['artists']].iloc[18]
```
  <li>Converting Song Duration from Milliseconds to Seconds</li>

```python
sp_tracks['duration'] = sp_tracks['duration_ms'].apply (lambda x : round(x/1000))
sp_tracks.drop('duration_ms', inplace = True, axis=1)
sp_tracks.duration.head()
```
  <li>Visualization: Pearson Correlation Heatmap for Two Variables</li>

```python
td = sp_tracks.drop(['key','mode','explicit'], axis=1).corr(method = 'pearson')
plt.figure(figsize=(9,5))
hmap = sns.heatmap(td, annot = True, fmt = '.1g', vmin=-1, vmax=1, center=0, cmap='Greens', linewidths=0.1, linecolor='black')
hmap.set_title('Correlation HeatMap')
hmap.set_xticklabels(hmap.get_xticklabels(), rotation=90)
```
  <li>Creating a 4% Sample of the Entire Dataset</li>

```python
sample_sp=sp_tracks.sample(int(0.004*len(sp_tracks)))
print(len(sample_sp))
```
  <li>Regression Plot of Loudness vs. Energy with Regression Line</li>

```python
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='loudness', x='energy', color='#054907').set(title='Regression Plot - Loudness vs Energy Correlation')
```
  <li>Regression Plot of Popularity vs. Acousticness with Regression Line</li>

```python
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='popularity', x='acousticness', color='#008000').set(title='Regression Plot - Popularity vs Acousticness Correlation')
```
  <li>Adding a New Column to the Tracks Table</li>

```
sp_tracks['dates']=sp_tracks.index.get_level_values('release_date')
sp_tracks.dates=pd.to_datetime(sp_tracks.dates)
years=sp_tracks.dates.dt.year
sp_tracks.head()
```
  <li>Graph: Number of Songs per Year</li>

```python
sns.displot(years, discrete=True, aspect=2, height=4, kind='hist',color='g').set(title='No of songs - per year')
```
  <li>Line Graph: Duration of Songs Over Each Year</li>

```python
total_dr = sp_tracks.duration
fig_dims = (15,5)
fig, ax = plt.subplots(figsize=fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title='Years vs Duration')
plt.xticks(rotation=90)
```
  <li>Horizontal Bar Plot: Song Duration Across Different Genres</li>

```python
plt.title('Duration of songs in different Genres')
sns.color_palette('crest', as_cmap=True)
sns.barplot(y='genre', x='duration_ms', data=sp_feature)
plt.xlabel('Duration in ms')
plt.ylabel('Genres')
```
  <li>Bar Plot: Top Five Genres by Popularity</li>

```python
sns.set_style(style='darkgrid')
plt.figure(figsize=(8,4))
Top = sp_feature.sort_values('popularity', ascending=False)[:10]
sns.barplot(y = 'genre', x = 'popularity', data = Top).set(title='Genres by Popularity-Top 5')
```
  </ol>
