#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import json
from test_cases import *

def api_request(text):
    response = requests.get('https://api.hh.ru/vacancies?text='+text)
    status_code = response.status_code
    
    result = {
        'code': status_code,
        'found': None,
        'items': None
        }
    
    if status_code == 200:
        data = json.loads(response.text)
        result['found'] = data['found']
        result['items'] = data['items']
    
    return result
    
def api_test(test_case):
    api_response = api_request(test_case['text'])
    
    if api_response['code'] == 200:
        if test_case['pass_condition'] == 'code_200':
            return True
        
        if test_case['pass_condition'] == 'found':
            return True if api_response['found']>0 else False


if api_test(basic_test_case):
    print('API работает. Тестируем.')
else:
    print('API сломан. Расходимся.')
    quit()

print()
print('Позитивные тесты:')
    
for test_case in positive_test_cases:
    print(f" {test_case['name']: <50}", end=' ')
    test_result = 'passed' if api_test(test_case) else 'failed'
    print(test_result)

print()
print('Негативные тесты:')
    
for test_case in negative_test_cases:
    print(f" {test_case['name']: <50}", end=' ')
    test_result = 'passed' if api_test(test_case) else 'failed'
    print(test_result)    
    

