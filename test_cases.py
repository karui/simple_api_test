basic_test_case = {
        'text': 'hh',
        'pass_condition': 'code_200'
    }

positive_test_cases = [
    {
        'name': 'Простой поиск',
        'text': 'школа программистов',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск словосочетаний',
        'text': '"работа в команде"',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск конкретной формы слова',
        'text': '!сумасшедшие',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск по части слова',
        'text': 'прокраст*',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск с учётом синонимов',
        'text': 'опсос',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск одного из слов',
        'text': 'направо or налево',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск одного из словосочетаний',
        'text': '"интересная работа" or "белая зарплата"',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск всех слов',
        'text': 'быстро and качественно and недорого',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск с исключеним слова',
        'text': 'опыт not работы',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск с объединением условий',
        'text': '(дорого or дёшево) and (качественно or халтурно)',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск по сложному запросу',
        'text': '("классная команда" and карьерный рост) or (сложные проекты) not "дресс код"',
        'pass_condition': 'found'
    },
    {
        'name': 'Поиск по полям',
        'text': 'NAME:программист and COMPANY_NAME:завод',
        'pass_condition': 'found'
    },
    
    ]

negative_test_cases = [
    {
        'name': 'Пустая строка',
        'text': '',
        'pass_condition': 'code_200'
    },
    {
        'name': 'Бессмысленный набор букв',
        'text': 'преведмедвед',
        'pass_condition': 'code_200'
    },
    {
        'name': 'Спецсимволы',
        'text': '"~`!@#$%^&*(){}[]\\\\',
        'pass_condition': 'code_200'
    },
    {
        'name': 'Разные ascii символы',
        'text': '☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶',
        'pass_condition': 'code_200'
    },
    {
        'name': 'Большая строка',
        'text': 'abc'*1000,
        'pass_condition': 'code_200'
    },
    {
        'name': 'Очень большая строка',
        'text': 'abc'*20000,
        'pass_condition': 'code_200'
    },
    ]