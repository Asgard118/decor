import requests
from datetime import datetime, timedelta

def get_stackoverflow_questions():
    base_url = 'https://api.stackexchange.com/2.3/questions'
    today = datetime.utcnow()
    two_days_ago = today - timedelta(days=2)
    
    params = {
        'fromdate': int(two_days_ago.timestamp()),
        'todate': int(today.timestamp()),
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow',
        'filter': '!9Z(-wzu0T'
    }
    
    response = requests.get(base_url, params=params)
    questions = response.json()['items']
    
    for question in questions:
        print(f"Question ID: {question['question_id']}")
        print(f"Title: {question['title']}")
        print(f"Link: {question['link']}")
        print("------")
        
get_stackoverflow_questions()
