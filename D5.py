import file_operations
from faker import Faker
import random
import os


def main():
    fake = Faker('ru_RU')
    runic_skills = [] 
    skill = [
        'Стремительный прыжок', 
        'Электрический выстрел', 
        'Ледяной удар', 
        'Стремительный удар', 
        'Кислотный взгляд', 
        'Тайный побег', 
        'Ледяной выстрел', 
        'Огненный заряд',
    ]
    alphabet = {
        'а': 'а͠', 
        'б': 'б̋', 
        'в': 'в͒͠',
        'г': 'г͒͠', 
        'д': 'д̋', 
        'е': 'е͠',
        'ё': 'ё͒͠', 
        'ж': 'ж͒', 
        'з': 'з̋̋',
        'и': 'и', 
        'й': 'й͒͠', 
        'к': 'к̋̋',
        'л': 'л̋͠', 
        'м': 'м͒͠', 
        'н': 'н͒',
        'о': 'о̋', 
        'п': 'п̋͠', 
        'р': 'р̋͠',
        'с': 'с͒', 
        'т': 'т͒', 
        'у': 'у͒͠',
        'ф': 'ф̋̋', 
        'х': 'х͒͠', 
        'ц': 'ц̋',
        'ч': 'ч̋͠', 
        'ш': 'ш͒͠', 
        'щ': 'щ̋',
        'ъ': 'ъ̋͠', 
        'ы': 'ы̋͠', 
        'ь': 'ь̋',
        'э': 'э͒͠', 
        'ю': 'ю̋͠', 
        'я': 'я̋',
        'А': 'А͠', 
        'Б': 'Б̋', 
        'В': 'В͒͠',
        'Г': 'Г͒͠', 
        'Д': 'Д̋', 
        'Е': 'Е',
        'Ё': 'Ё͒͠', 
        'Ж': 'Ж͒', 
        'З': 'З̋̋',
        'И': 'И', 
        'Й': 'Й͒͠', 
        'К': 'К̋̋',
        'Л': 'Л̋͠', 
        'М': 'М͒͠', 
        'Н': 'Н͒',
        'О': 'О̋', 
        'П': 'П̋͠', 
        'Р': 'Р̋͠',
        'С': 'С͒', 
        'Т': 'Т͒', 
        'У': 'У͒͠',
        'Ф': 'Ф̋̋', 
        'Х': 'Х͒͠', 
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 
        'Ш': 'Ш͒͠', 
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 
        'Ы': 'Ы̋͠', 
        'Ь': 'Ь̋',
        'Э': 'Э͒͠', 
        'Ю': 'Ю̋͠', 
        'Я': 'Я̋',
        ' ': ' ',
    }

    while len(skill) != 0:
        skill_1 = skill[0]
        for letter, replacement in alphabet.items():
            skill_1 = skill_1.replace(letter, replacement)
        runic_skills.append(skill_1)
        del skill[0]

    folder = 'Dv5'
    os.makedirs(folder, mode=0o777, exist_ok=False)

    for number in range(10):
            random_skill = random.sample(runic_skills, 3)
            context = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'job': fake.job(),
                'town': fake.city(),
                'strength': random.randint(3, 18),
                'agility': random.randint(3, 18),
                'endurance': random.randint(3, 18),
                'intelligence': random.randint(3, 18),
                'luck': random.randint(3, 18),
                'skill_1': random_skill[0],
                'skill_2': random_skill[1],
                'skill_3': random_skill[2],
            }
            file_operations.render_template(
                'charsheet.svg', 
                os.path.join(
                    folder, 
                    f'result{number + 1}.svg'
                    ), 
                context,
                )
    
if __name__ == '__main__':
    main()
