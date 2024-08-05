import requests

# Replace 'YOUR_API_KEY' with your actual OMDb API key
api_key = '8a04f01c'

# Function to build the API request URL
def build_url(movie_title, year=''):
  base_url = 'http://www.omdbapi.com/'
  params = {
      'apikey': api_key,
      't': movie_title,
      'plot': 'full',
  }
  if year:
    params['y'] = year
  return base_url + '?' + '&'.join(f'{key}={value}' for key, value in params.items())

# Function to fetch and handle API response
def fetch_movie_data(movie_title, year=''):
  url = build_url(movie_title=movie_title, year=year)
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return None

# Example usage
movie_title = 'Ice Age'
year = 2000


# Fetch and process data
data = fetch_movie_data(movie_title=movie_title)
print(data)

