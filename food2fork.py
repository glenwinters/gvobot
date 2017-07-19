import os
import requests
import random

FOOD2FORK_API_KEY = os.environ['FOOD2FORK_API_KEY']
FOOD2FORK_API_URL = 'http://food2fork.com/api/'

def food2fork_search(query=None, page=None):
    """food2fork search API

    Get a list of recipes based on a query. If no query is sent, you get a
    list of the most popular recipes. 30 results per page.
    """
    base_url = FOOD2FORK_API_URL + 'search?key=' + FOOD2FORK_API_KEY
    url = base_url
    if query is not None:
        url += '&q={}'.format(query)
    if page is not None:
        url += '&page={}'.format(page)
    response = requests.get(url)
    response_json = response.json()
    return response_json['recipes']

def food2fork_get(recipe_id):
    """food2fork get API

    Get a single recipe by ID.
    """
    base_url = FOOD2FORK_API_URL + 'get?key=' + FOOD2FORK_API_KEY
    url = base_url + '&rId={}'.format(recipe_id)
    response = requests.get(url)
    return response.json()

def get_random_recipe():
    # food2fork's search returns the count of recipes in the given response,
    # but it doesn't tell you how many pages there are. I manually checked
    # different pages up to around 4000, but the social_rank was low. I backed
    # up until I found the social_rank was at about 50 at page 1000. For better
    # quality random recipe, the page_max should be lowered.
    # Pick a random page
    page_max = 1000
    page = random.randint(1, 1000)

    # Make the call to food2fork.com
    results = food2fork_search(page=page)

    # Pick a random recipe in the list
    pick = random.randint(0, len(results) - 1)
    recipe = results[pick]

    # Return a message format for the bot
    message = recipe['title'] + ' ' + recipe['source_url']
    return message
