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

  <h1><a name="exploringthedataset">Exploring the Dataset</a></h1>

```python
sp_tracks = pd.read_csv('D:/spotifydata/tracks.csv')
sp_feature = pd.read_csv('D:/spotifydata/SpotifyFeatures.csv')
```
```python
#viewing the tracks data
sp_tracks.head()
```
```python
#viewing the feature data
sp_feature.head()
```
  <h1><a name="identifyingnullvaluesinthedataset">Identifying Null Values in the Dataset</a></h1>

```python
#checking null in tracks data
pd.isnull(sp_tracks).sum()
```
```python
#checking null in tracks data
pd.isnull(sp_feature).sum()
```
  <h1><a name="datasetoverviewrowscolumnsdatatypesandmemoryusage">Dataset Overview: Rows, Columns, Data Types, and Memory Usage</a></h1>

```python
#checking info in tracks data
sp_tracks.info()
```
```python
#checking info in feature data
sp_feature.info()
```
  <h1><a name="extractinginsightsfromthedatasetthroughanalysis">Extracting Insights from the Dataset through Analysis</a></h1>
  <ol>
  <li>Exploring the 10 Least Popular Songs in the Spotify Dataset</li>
  <li>Descriptive Statistics </li>
  <li>Discovering the Top 10 Popular Songs in the Spotify Dataset</li>
  <li>Setting Release Date as the Index Column</li>
  <li>Extracting Artist Name from the 18th Row of the Dataset</li>
  <li>Converting Song Duration from Milliseconds to Seconds</li>
  <li>Visualization: Pearson Correlation Heatmap for Two Variables</li>
  <li>Creating a 4% Sample of the Entire Dataset</li>
  <li>Regression Plot of Loudness vs. Energy with Regression Line</li>
  <li>Regression Plot of Popularity vs. Acousticness with Regression Line</li>
  <li>Adding a New Column to the Tracks Table</li>
  <li>Graph: Number of Songs per Year</li>
  <li>Line Graph: Duration of Songs Over Each Year</li>
  <li>Horizontal Bar Plot: Song Duration Across Different Genres</li>
  <li>Bar Plot: Top Five Genres by Popularity</li>
  </ol>
