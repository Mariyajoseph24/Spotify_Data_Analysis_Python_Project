<h1>Spotify Data Analysis Python Project🎼🎧</h1>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/43749cf9-4eb1-476c-89ea-bf1625b17168">
<h1>Contents📖</h1>
<ul>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#importrequiredlibraries">Import Required Libraries</a></li>
  <li><a href="#exploringthedataset">Exploring the Dataset</a></li>
  <li><a href="#identifyingnullvaluesinthedataset">Identifying Null Values in the Dataset</a></li>
  <li><a href="#datasetoverviewrowscolumnsdatatypesandmemoryusage">Dataset Overview: Rows, Columns, Data Types, and Memory Usage</a></li>
  <li><a href="#extractinginsightsfromthedatasetthroughanalysis">Extracting Insights from the Dataset through Analysis📊</a></li>
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
  <h1><a name="extractinginsightsfromthedatasetthroughanalysis">Extracting Insights from the Dataset through Analysis📊</a></h1>
  <ol>
  <li>Exploring the 10 Least Popular Songs in the Spotify Dataset</li>

  ```python
a=sp_tracks.sort_values('popularity',ascending=True)[0:10]
a[['name','popularity']]
```
<h6>Answer:</h6>
<img width="300" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/fbc7e495-5d30-4bca-9f80-ab8036cb76d9">
<ul>
  <li><code>a = sp_tracks.sort_values('popularity', ascending=True)[0:10]</code>: This line of code creates a new DataFrame <code>a</code> by sorting the 'sp_tracks' DataFrame based on the 'popularity' column in ascending order. The <code>[0:10]</code> notation selects the first 10 rows of the sorted DataFrame, effectively selecting the 10 least popular tracks.</li>
  <li><code>a[['name', 'popularity']]</code>: This line of code selects specific columns, namely 'name' and 'popularity', from the DataFrame <code>a</code> created in the previous line. This will show the names of the 10 least popular tracks along with their corresponding popularity values.</li>
</ul>
<br>

  <li>Descriptive Statistics </li>

```python
#descriptive statistics of tracks
sp_tracks.describe().transpose()
```
<h6>Answer:</h6>
<img width="450" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/6a0cbdba-0dfd-4507-9fc5-d6695a6b75b3">
<ul>
  <li><code>#descriptive statistics of tracks</code>: This comment indicates that the following line of code is intended to compute and display descriptive statistics of the 'sp_tracks' DataFrame.</li>
  <li><code>sp_tracks.describe().transpose()</code>: This line of code calls the <code>describe()</code> method on the 'sp_tracks' DataFrame, which calculates various summary statistics for each numeric column in the DataFrame. The <code>.transpose()</code> method is then used to transpose the resulting statistics table, making it easier to read with columns as rows and vice versa.</li>
</ul>
<br>

```python
#descriptive of feature
sp_feature.describe().transpose()
```
<h6>Answer:</h6>
<img width="450" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/4e64d105-0b80-4d2b-a1a0-3f3991c5056e">
<ul>
  <li><code>#descriptive statistics of feature</code>: This comment indicates that the following line of code is intended to compute and display descriptive statistics of the 'sp_feature' DataFrame.</li>
  <li><code>sp_feature.describe().transpose()</code>: This line of code calls the <code>describe()</code> method on the 'sp_feature' DataFrame, which calculates various summary statistics for each numeric column in the DataFrame. The <code>.transpose()</code> method is then used to transpose the resulting statistics table, making it easier to read with columns as rows and vice versa.</li>
</ul>
<br>

  <li>Discovering the Top 10 Popular Songs in the Spotify Dataset</li>

```python
a=sp_tracks
b=a[a['popularity']>90].sort_values('popularity',ascending=False)[:10]
b[['name','popularity','artists']]
```
<h6>Answer:</h6>
<img width="450" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/c4e88855-675e-409a-a61a-a2b4c987690b">
<ul>
  <li><code>a = sp_tracks</code>: This line of code assigns the 'sp_tracks' DataFrame to a new DataFrame variable <code>a</code>.</li>
  <li><code>b = a[a['popularity'] > 90].sort_values('popularity', ascending=False)[:10]</code>: This line of code creates a new DataFrame <code>b</code> by selecting rows from the DataFrame <code>a</code> where the 'popularity' column is greater than 90. The DataFrame is then sorted in descending order based on the 'popularity' column, and the first 10 rows are selected. This effectively gives you the top 10 most popular tracks.</li>
  <li><code>b[['name', 'popularity', 'artists']]</code>: This line of code selects specific columns ('name', 'popularity', and 'artists') from the DataFrame <code>b</code> created in the previous line. This will display the names, popularity values, and artist information of the top 10 most popular tracks.</li>
</ul>
<br>

  <li>Setting Release Date as the Index Column</li>

```python
sp_tracks.set_index('release_date',inplace=True)
sp_tracks.index=pd.to_datetime(sp_tracks.index)
sp_tracks.head()
```
<h6>Answer:</h6>
<img width="450" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/9c463e8a-58f3-45f9-9a51-1996eba4bb16">
<ul>
  <li><code>sp_tracks.set_index('release_date', inplace=True)</code>: This line of code sets the 'release_date' column as the index of the 'sp_tracks' DataFrame. The <code>inplace=True</code> argument modifies the DataFrame in place, meaning the change is applied directly to the original DataFrame.</li>
  <li><code>sp_tracks.index = pd.to_datetime(sp_tracks.index)</code>: This line of code converts the index of the 'sp_tracks' DataFrame to a datetime format using the <code>pd.to_datetime()</code> function. This is often done to ensure that the index represents dates in a meaningful way, allowing for time-based operations.</li>
  <li><code>sp_tracks.head()</code>: This line of code calls the <code>head()</code> method on the 'sp_tracks' DataFrame, which will display the first few rows of the DataFrame with the updated index.</li>
</ul>
<br>

  <li>Extracting Artist Name from the 18th Row of the Dataset</li>

```python
sp_tracks[['artists']].iloc[18]
```
<h6>Answer:</h6>
<img width="300" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/ee0d8e5c-1657-40b9-b80c-258c67f4da87">
<ul>
  <li><code>sp_tracks[['artists']].iloc[18]</code>: This line of code selects the 'artists' column from the 'sp_tracks' DataFrame and then uses the <code>iloc[18]</code> indexer to retrieve the value at the 18th row of the 'artists' column. This will display the artists' information for the track at index 18.</li>
</ul>
<br>

  <li>Converting Song Duration from Milliseconds to Seconds</li>

```python
sp_tracks['duration'] = sp_tracks['duration_ms'].apply (lambda x : round(x/1000))
sp_tracks.drop('duration_ms', inplace = True, axis=1)
sp_tracks.duration.head()
```
<h6>Answer:</h6>
<img width="200" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/12be7462-32ff-4b02-b048-630249000c96">
<ul>
  <li><code>sp_tracks['duration'] = sp_tracks['duration_ms'].apply(lambda x: round(x/1000))</code>: This line of code creates a new column called 'duration' in the 'sp_tracks' DataFrame. It calculates the duration in seconds by applying a lambda function to the 'duration_ms' column. The lambda function divides the 'duration_ms' value by 1000 and rounds it to get the duration in seconds.</li>
  <li><code>sp_tracks.drop('duration_ms', inplace=True, axis=1)</code>: This line of code removes the original 'duration_ms' column from the 'sp_tracks' DataFrame. The <code>inplace=True</code> argument makes the change directly to the DataFrame.</li>
  <li><code>sp_tracks.duration.head()</code>: This line of code displays the first few values from the newly created 'duration' column in the 'sp_tracks' DataFrame.</li>
</ul>
<br>

  <li>Visualization: Pearson Correlation Heatmap for Two Variables</li>

```python
td = sp_tracks.drop(['key','mode','explicit'], axis=1).corr(method = 'pearson')
plt.figure(figsize=(9,5))
hmap = sns.heatmap(td, annot = True, fmt = '.1g', vmin=-1, vmax=1, center=0, cmap='Greens', linewidths=0.1, linecolor='black')
hmap.set_title('Correlation HeatMap')
hmap.set_xticklabels(hmap.get_xticklabels(), rotation=90)
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/5105709b-dd48-40d5-827f-dc9d1e68bcc2">
<ul>
  <li><code>td = sp_tracks.drop(['key', 'mode', 'explicit'], axis=1).corr(method='pearson')</code>: This line of code creates a correlation matrix by calculating Pearson correlation coefficients between numeric columns in the 'sp_tracks' DataFrame. It drops the columns 'key', 'mode', and 'explicit' before calculating the correlations.</li>
  <li><code>plt.figure(figsize=(9, 5))</code>: This line of code sets the figure size for the upcoming heatmap visualization using Matplotlib.</li>
  <li><code>hmap = sns.heatmap(td, annot=True, fmt='.1g', vmin=-1, vmax=1, center=0, cmap='Greens', linewidths=0.1, linecolor='black')</code>: This line of code uses Seaborn's <code>heatmap()</code> function to create a heatmap visualization of the correlation matrix. It displays the correlation values as annotations, uses a color map ('Greens') to represent the correlation strength, and sets the range of correlation values to be between -1 and 1.</li>
  <li><code>hmap.set_title('Correlation HeatMap')</code>: This line of code sets the title for the heatmap visualization.</li>
  <li><code>hmap.set_xticklabels(hmap.get_xticklabels(), rotation=90)</code>: This line of code rotates the x-axis labels of the heatmap for better readability.</li>
</ul>
<br>

  <li>Creating a 4% Sample of the Entire Dataset</li>

```python
sample_sp=sp_tracks.sample(int(0.004*len(sp_tracks)))
print(len(sample_sp))
```
<h6>Answer:</h6>
<img width="100" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/ba287e70-cbf5-474a-b8e6-765db4903f16">
<ul>
  <li><code>sample_sp = sp_tracks.sample(int(0.004 * len(sp_tracks)))</code>: This line of code creates a random sample of the 'sp_tracks' DataFrame. The <code>sample()</code> function is used to select a random subset of rows. The argument <code>int(0.004 * len(sp_tracks))</code> determines the number of rows to be sampled. In this case, it's approximately 0.4% of the total number of rows in the 'sp_tracks' DataFrame.</li>
  <li><code>print(len(sample_sp))</code>: This line of code prints the length (number of rows) of the <code>sample_sp</code> DataFrame to the console. This will show you the number of rows in the sampled subset.</li>
</ul>
<br>

  <li>Regression Plot of Loudness vs. Energy with Regression Line</li>

```python
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='loudness', x='energy', color='#054907').set(title='Regression Plot - Loudness vs Energy Correlation')
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/05f1fe1b-11d8-4ddf-bf9d-5b5fc36d1715">
<ul>
  <li><code>plt.figure(figsize=(8, 4))</code>: This line of code sets the figure size for the upcoming visualization using Matplotlib.</li>
  <li><code>sns.regplot(data=sample_sp, y='loudness', x='energy', color='#054907')</code>: This line of code uses Seaborn's <code>regplot()</code> function to create a regression plot. It visualizes the relationship between the 'loudness' and 'energy' columns from the <code>sample_sp</code> DataFrame. The <code>color='#054907'</code> argument sets the color of the plot.</li>
  <li><code>.set(title='Regression Plot - Loudness vs Energy Correlation')</code>: This line of code sets the title for the regression plot.</li>
</ul>
<br>

  <li>Regression Plot of Popularity vs. Acousticness with Regression Line</li>

```python
plt.figure(figsize=(8,4))
sns.regplot(data=sample_sp, y='popularity', x='acousticness', color='#008000').set(title='Regression Plot - Popularity vs Acousticness Correlation')
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/b611829a-cfb2-49d5-a115-129ab83ebc9f">
<ul>
  <li><code>plt.figure(figsize=(8, 4))</code>: This line of code sets the figure size for the upcoming visualization using Matplotlib.</li>
  <li><code>sns.regplot(data=sample_sp, y='popularity', x='acousticness', color='#008000')</code>: This line of code uses Seaborn's <code>regplot()</code> function to create a regression plot. It visualizes the relationship between the 'popularity' and 'acousticness' columns from the <code>sample_sp</code> DataFrame. The <code>color='#008000'</code> argument sets the color of the plot.</li>
  <li><code>.set(title='Regression Plot - Popularity vs Acousticness Correlation')</code>: This line of code sets the title for the regression plot.</li>
</ul>
<br>

  <li>Adding a New Column to the Tracks Table</li>

```python
sp_tracks['dates']=sp_tracks.index.get_level_values('release_date')
sp_tracks.dates=pd.to_datetime(sp_tracks.dates)
years=sp_tracks.dates.dt.year
sp_tracks.head()
```
<h6>Answer:</h6>
<img width="450" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/0d89abb2-fba5-4bfa-b37d-e1e6d5d7063c">
<ul>
  <li><code>sp_tracks['dates'] = sp_tracks.index.get_level_values('release_date')</code>: This line of code creates a new column called 'dates' in the 'sp_tracks' DataFrame. It uses the <code>get_level_values()</code> method on the index of the DataFrame to extract the 'release_date' values and assigns them to the 'dates' column.</li>
  <li><code>sp_tracks.dates = pd.to_datetime(sp_tracks.dates)</code>: This line of code converts the values in the 'dates' column to datetime format using the <code>pd.to_datetime()</code> function. This ensures that the dates are treated as proper datetime objects.</li>
  <li><code>years = sp_tracks.dates.dt.year</code>: This line of code extracts the year component from the 'dates' column using the <code>dt.year</code> attribute of the datetime objects. It assigns the extracted years to the 'years' variable.</li>
  <li><code>sp_tracks.head()</code>: This line of code displays the first few rows of the modified 'sp_tracks' DataFrame, which now includes the 'dates' column and the extracted 'years' variable.</li>
</ul>
<br>

  <li>Graph: Number of Songs per Year</li>

```python
sns.displot(years, discrete=True, aspect=2, height=4, kind='hist',color='g').set(title='No of songs - per year')
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/6581495b-3540-4ad5-911e-9d2146ac2010">
<ul>
  <li><code>sns.displot(years, discrete=True, aspect=2, height=4, kind='hist', color='g')</code>: This line of code uses Seaborn's <code>displot()</code> function to create a histogram plot. It visualizes the distribution of the 'years' variable, which contains the release years of the songs. The <code>discrete=True</code> argument indicates that the data is discrete (years), <code>aspect=2</code> adjusts the width-to-height ratio of the plot, <code>height=4</code> sets the height of the plot, <code>kind='hist'</code> specifies that it's a histogram plot, and <code>color='g'</code> sets the color of the plot.</li>
  <li><code>.set(title='No of songs - per year')</code>: This line of code sets the title for the histogram plot.</li>
</ul>
<br>

  <li>Line Graph: Duration of Songs Over Each Year</li>

```python
total_dr = sp_tracks.duration
fig_dims = (15,5)
fig, ax = plt.subplots(figsize=fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title='Years vs Duration')
plt.xticks(rotation=90)
```
<h6>Answer:</h6>
<img width="600" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/34f4e389-b441-425a-8456-ab98d5bd96ec">
<ul>
  <li><code>total_dr = sp_tracks.duration</code>: This line of code creates a new variable <code>total_dr</code> and assigns the values from the 'duration' column of the 'sp_tracks' DataFrame to it.</li>
  <li><code>fig_dims = (15, 5)</code>: This line of code sets the dimensions of the figure for the upcoming visualization.</li>
  <li><code>fig, ax = plt.subplots(figsize=fig_dims)</code>: This line of code uses Matplotlib to create a subplot figure with the specified dimensions. It returns two variables: <code>fig</code> (the figure) and <code>ax</code> (the axis).</li>
  <li><code>fig = sns.barplot(x=years, y=total_dr, ax=ax, errwidth=False)</code>: This line of code uses Seaborn's <code>barplot()</code> function to create a bar plot. It plots the 'years' on the x-axis and 'total_dr' (duration) on the y-axis, using the provided axis <code>ax</code>. The <code>errwidth=False</code> argument disables error bars.</li>
  <li><code>.set(title='Years vs Duration')</code>: This line of code sets the title for the bar plot.</li>
  <li><code>plt.xticks(rotation=90)</code>: This line of code rotates the x-axis tick labels for better readability.</li>
</ul>
<br>

  <li>Horizontal Bar Plot: Song Duration Across Different Genres</li>

```python
plt.title('Duration of songs in different Genres')
sns.color_palette('crest', as_cmap=True)
sns.barplot(y='genre', x='duration_ms', data=sp_feature)
plt.xlabel('Duration in ms')
plt.ylabel('Genres')
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/944cdf33-f60e-48da-bcb3-4776d8bc8125">
<ul>
  <li><code>plt.title('Duration of songs in different Genres')</code>: This line of code sets the title for the upcoming visualization using Matplotlib.</li>
  <li><code>sns.color_palette('crest', as_cmap=True)</code>: This line of code sets the color palette for the visualization. The 'crest' palette is being used here.</li>
  <li><code>sns.barplot(y='genre', x='duration_ms', data=sp_feature)</code>: This line of code uses Seaborn's <code>barplot()</code> function to create a bar plot. It plots the 'genre' on the y-axis and 'duration_ms' on the x-axis from the 'sp_feature' DataFrame.</li>
  <li><code>plt.xlabel('Duration in ms')</code>: This line of code sets the label for the x-axis.</li>
  <li><code>plt.ylabel('Genres')</code>: This line of code sets the label for the y-axis.</li>
</ul>
<br>

  <li>Bar Plot: Top Five Genres by Popularity</li>

```python
sns.set_style(style='darkgrid')
plt.figure(figsize=(8,4))
Top = sp_feature.sort_values('popularity', ascending=False)[:10]
sns.barplot(y = 'genre', x = 'popularity', data = Top).set(title='Genres by Popularity-Top 5')
```
<h6>Answer:</h6>
<img width="400" alt="Coding" src="https://github.com/Mariyajoseph24/Spotify_Data_Analysis_Python_Project/assets/91487663/09b75262-dc3e-4314-b21e-08db24de6e1e">
<ul>
  <li><code>sns.set_style(style='darkgrid')</code>: This line of code sets the style of the Seaborn plots to 'darkgrid' style, which includes a dark grid in the background of the plot.</li>
  <li><code>plt.figure(figsize=(8, 4))</code>: This line of code sets the figure size for the upcoming visualization using Matplotlib.</li>
  <li><code>Top = sp_feature.sort_values('popularity', ascending=False)[:10]</code>: This line of code creates a new DataFrame <code>Top</code> by sorting the 'sp_feature' DataFrame in descending order based on the 'popularity' column and selecting the top 10 rows.</li>
  <li><code>sns.barplot(y='genre', x='popularity', data=Top).set(title='Genres by Popularity-Top 5')</code>: This line of code uses Seaborn's <code>barplot()</code> function to create a bar plot. It plots the 'genre' on the y-axis and 'popularity' on the x-axis from the <code>Top</code> DataFrame. The <code>.set()</code> function sets the title for the plot.</li>
</ul>


  </ol>
