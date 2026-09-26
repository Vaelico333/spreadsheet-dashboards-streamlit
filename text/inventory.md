# Inventory management dashboard

A dashboard that explores the trends in music streaming in several countries around the world.  
In this project, I explored this [dataset](https://www.kaggle.com/datasets/atharvasoundankar/global-music-streaming-trends-and-listener-insights) from Kaggle to extract insight about the preferences and behaviour of the users of some of the world's biggest music streaming services.

---

Music streaming became popular between 2008 and 2015, partly due to the rise of Spotify as a seamless, on-demand service that offered a convenient alternative to piracy. This topic has been widely discussed in the media and news, as well as in the machine learning community.

### Purpose of this project

This project aims to transform raw data into a clear, visually engaging dashboard that reveals underlying structures and relationships between features. By leveraging Excel’s dynamic tables and interactive slicers, the design allows users to explore these relationships in detail, with key findings highlighted through targeted plots and KPIs.

### The dataset

The dataset explored in this project, created by Atharva Soundankar, is described as having high completeness and credibility. It offers a glimpse into some  interesting characteristics of music streaming users, including:

- **Age** of the user.
- **Country** of origin.
- **Streaming platform** used.
- **Top genre**, or the most streamed music genre.
- **Minutes streamed per day**.
- **Number of songs liked**.
- **Most played artist**, selected from a predefined list.
- **Subscription type**, either Free or Premium.
- Preferred **Listening Time**: morning, afternoon or night.
- **Discover Weekly Engagement**: use of automatically generated playlists.
- **Repeat Song Rate (%)**.

### Workflow

This dashboard was built the following way:  
  
CSV file  
**↓**  
Load data into an Excel table  
**↓**  
Create dynamic tables  
**↓**  
Create plots  
**↓**  
Add data slicers  
**↓**  
Setup and format the dashboard  


---

The dashboard is structured as follows:

### KPIs

I chose to display these three KPIs:

- **Number of users**: the number of users included in the current view.
- **Most popular subscription**: the most popular subscription type in the current view.
- **Mean usage per day in minutes**: the average daily usage in the current view.

These KPIs give us an idea of the size of the current dataset, the user's usbscription preferences and their use of streaming services.

### Plots

Using several types of charts, I explored relationships between features in the dataset:

- <u>**Map plots**</u>:
    - **Streaming platform per country**: I used a map plot to show which streaming platform is the most popular in each of the countries explored.
    - **Genre per country**: I used a map plot to show which genre is the most popular on each of the countries explored.
- <u>**Vertical barplots**</u>:
    - **Average use of Discover Weekly** and **Average song repeat** by **Genre**: I created a composite plot using two features with similar ranges. This makes it easier to compare user behaviour across favourite genres, particularly in terms of song repetition and use of automated playlists.
    - **Average minutes per day** and **Average liked songs** by **Genre**: I created a composite plot using two features with similar ranges. It helps compare average usage and the average number of liked songs across genres, which could indicate users’ interest in keeping those songs accessible.
- <u>**Dotted lineplot**</u>:
    - **Discover Weekly usage (%)** by **Age**: this plot helps explore whether there is a relationship between age and discovery through automated playlists.
    - **Average age** by **Genre**: in this plot, I wanted to explore the correlation between age and musical genre.
- <u>**Horizontal barplot**</u>:
    - **Subscription types** by **Streaming service**: this plot shows the proportion of users with a Premium subscription on each streaming platform.  
- <u>**Pieplot**</u>:
    - **Average minutes per day** by **Listening time**: this plot compares the average listening time across different periods of the day.

### Slicers

To segment and navigate the data more easily, I included the following slicers, which allow users to view different parts of the dataset in the plots:

- **Age**: 13 to 60 years old.
- **Country**: Australia, Brazil, Canada, France, Germany, India, Japan, South Corea, UK and the USA.
- **Time of the day**: Morning, Afternoon and Night.
- **Subscription type**: Free and Premium.
- **Musical genre**: Classical, Country, EDM, Hip-Hop, Jazz, Metal, Pop, R&B, Reggae and Rock.
- **Streaming platform**: Amazon Music, Apple Music, Deezer, Spotify, Tidal and YouTube.

---

### Observations

- The dataset is composed of **5000 users**.
- The most popular subscription type is **Premium**, although it varies across regions and musical genres.
- The average **daily listening time** is consistently close to 300 minutes.

### Case study: Amazon Music

Amazon Music has the lowest proportion of Premium subscribers among the streaming platforms in the dataset: 47.3% of its users have a Premium subscription. With 861 users, the sample allows us to explore several patterns:

- <u>**Subscriptions** by **Age**</u>:  
I divided the data into five age groups:
    - <u>13-19</u>: 43.3% have a Premium subscription.
    - <u>20-29</u>: 45.5% have a Premium subscription.
    - <u>30-39</u>: 51.4% have a Premium subscription.
    - <u>40-49</u>: 48.9% have a Premium subscription.
    - <u>50-60</u>: 46.1% have a Premium subscription.

**Observations**:  
The lowest proportion of Premium is among users aged *13 to 19*, which may be related to their more limited access to money. The 20–29 and 50–60 age groups may also be worth exploring further.

- <u>**Subscriptions** by **Country**</u>:  
The dataset includes ten countries:
    - <u>Brazil</u>: 54.9% have a Premium subscription.
    - <u>USA</u>: 54.8% have a Premium subscription.
    - <u>Australia</u>: 53.6% have a Premium subscription.
    - <u>UK</u>: 51.9% have a Premium subscription.
    - <u>Japan</u>: 48.2% have a Premium subscription.
    - <u>France</u>: 45.2% have a Premium subscription.
    - <u>Canada</u>: 45.1% have a Premium subscription.
    - <u>Germany</u>: 40.7% have a Premium subscription.
    - <u>South Korea</u>: 39.8% have a Premium subscription.
    - <u>India</u>: 34.6% have a Premium subscription.

**Observations**:  
*India* stands out in this distribution, with just 34.6% of users having a Premium subscription. This may be related to economic inequality in the country, which could limit some users’ ability to pay for a subscription. *Germany* and *South Korea* also have relatively low proportions of Premium subscribers, at around 40%.

- <u>**Subscriptions** by **Genre**</u>:
This dataset contains data about ten musical genres:
    - <u>EDM</u>: 52.3% have a Premium subscription.
    - <u>Classical</u>: 50.5% have a Premium subscription.
    - <u>Jazz</u>: 48.8% have a Premium subscription.
    - <u>Rock</u>: 48.8% have a Premium subscription.
    - <u>Reggae</u>: 48.3% have a Premium subscription.
    - <u>R%B</u>: 46.3% have a Premium subscription.
    - <u>Country</u>: 46% have a Premium subscription.
    - <u>Metal</u>: 45.7% have a Premium subscription.
    - <u>Hip-Hop</u>: 43.8% have a Premium subscription.
    - <u>Pop</u>: 41.3% have a Premium subscription.

**Observations**:  
*Pop* has the lowest proportion of Premium subscribers, even though it is one of the most popular genres among the general population. I would also like to highlight the genres with less than 48% Premium subscribers: *Hip-Hop, Metal, Country* and *R&B*.

- <u>**Subscriptions** by **Listening time** of the day</u>:
This dataset contemplates three periods:
    - <u>Morning</u>: 47.8% have a Premium subscription.
    - <u>Afternoon</u>: 45.5% have a Premium subscription.
    - <u>Night</u>: 48.3% have a Premium subscription.

**Observations**:  
The differences between the periods of the day are minimal, with *afternoon* listeners having the lowest proportion of Premium subscriptions.

#### Conclussions and recommendations

I identified **three areas** where the proportion of Premium subscribers is relatively **low**:

- <u>Age</u>: users aged 20–29 and 50–60.
- <u>Country</u>: Germany and South Korea.
- <u>Musical genre</u>: Pop, Hip-Hop, Metal, Country and Rithm & Blues.

My **recommendations**:

- Run marketing campaigns in Germany and South Korea, targeted at younger and older users.
- Invite well-known artists from the aforementioned genres to collaborate on marketing campaigns, with the aim of increasing interest in the app among listeners of those genres.

---

### Challenges

The main challenge in this project was organizing the data and choosing the right plots to provide actionable insights from the raw data. Once that was done, creating the dynamic tables and adding slicers was relatively straightforward.

Excel is a powerful tool, although it can be somewhat cumbersome because of its high memory consumption and susceptibility to errors.

### Skills trained

Through this project, I improved my spreadsheet skills by learning how to create, manage and filter dynamic tables and charts, and how to combine them into a clear, engaging and visually appealing dashboard.