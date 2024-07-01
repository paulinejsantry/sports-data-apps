# NFL 2023 Analysis (WIP)
This App is an exploratory analysis of the 2023 NFL Season. Specifically, we will focus on the New England Patriots.

## Data sources

### Column Descriptions
[Source](https://www.nflfastr.com/articles/field_descriptions.html)

## Deployment

### Local Deployment

#### Docker deployment (recommended)
~~~bash
docker build -t pats_app .
docker run -it pats_app
~~~

#### Dev deployment
~~~bash 
# install reqs
pip install -r requirements.txt

# launch app
streamlit run app.py --server.port 8000
~~~

## Acknowledgement of Limitations