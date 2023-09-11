import os
from datetime import datetime, timedelta
from dls_task import get_stackoverflow_questions
import requests

def logger(log_file_path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(log_file_path, 'a', encoding="utf-8") as log_file:
                log_file.write(f"Дата/время: {current_time}\n")
                log_file.write(f"Функция: {old_function.__name__}\n")
                log_file.write(f"Аргументы: {args}, {kwargs}\n")
                
            result = old_function(*args, **kwargs)
            
            with open(log_file_path, 'a', encoding="utf-8") as log_file:
                log_file.write(f"Результат: {result}\n")
                log_file.write("=" * 40 + "\n")
                
            return result
        return new_function
    return __logger

paths = ('log_1.log')
base_url = 'https://api.stackexchange.com/2.3/questions'

@logger(paths)
def get_stackoverflow_questions(base_url):
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
    return "all done"

if __name__ == '__main__':
    get_stackoverflow_questions(base_url)