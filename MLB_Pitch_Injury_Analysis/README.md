# MLB Pitch & Injury Analysis

## Data sources
- [Injury Data](https://www.prosportstransactions.com/baseball/Search/SearchResults.php?Player=&Team=&BeginDate=1999-03-01&EndDate=2017-11-01&DLChkBx=yes&submit=Search&start=%22) scraped via injury_data_scrape.ipynb
- [Pitch data](https://baseballsavant.mlb.com/statcast_search?hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&hfStadium=&hfBBL=&hfNewZones=&hfPull=&hfC=&hfSea=2024%7C&hfSit=&player_type=pitcher&hfOuts=&hfOpponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfMo=&hfTeam=&home_road=&hfRO=&position=&hfInfield=&hfOutfield=&hfInn=&hfBBT=&hfFlag=&metric_1=&group_by=name&min_pitches=0&min_results=0&min_pas=0&sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc#results)


## Deployment

### Local Deployment

#### Docker deployment (recommended)
~~~bash

~~~

#### Dev deployment
~~~bash 
# install reqs
pip install -r requirements.txt

# launch app
streamlit run app.py --server.port 8000
~~~

## Acknowledgement of Limitations
- Injury report data is skewed since teams use it to remove players around strategically, not just for injuries  
- Covid-19 impacted the injury report statistics
- Previous injuries will also impact future injuries