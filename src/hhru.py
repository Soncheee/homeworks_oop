from abc import ABC, abstractmethod
import requests
import json
from typing import List



class HH_API_ABC(ABC):
    @abstractmethod
    def __connect(self):
        pass

    def load_vacancies(self, keyword):
        pass

class HH_API(HH_API_ABC):
    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

class Vacancies:
    def __init__(self, name: str, url: str, payment: float, description: str):
        self.name = name
        self.url = url
        # self.payment = payment if payment is not None else 0
        if payment is not None:
            self.payment = payment
        else:
            self.payment = 0

        self.description = description


    def __lt__(self, other):
        return self.payment < other.payment
    def __gt__(self, other):
        return self.payment > other.payment
    def __eq__(self, other):
            return self.payment == other.payment

class FileManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancies):
        pass

    @abstractmethod
    def get_vacancy(self) -> List[Vacancies]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancies):
        pass

class JsonFile:
    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancies):
        try:
            with open(self.filename, 'r') as file:
                try:
                    vacancies = json.load(file)
                except json.JSONDecodeError:
                    vacancies = []
        except FileNotFoundError:
            vacancies = []

        vacancies.append({
            'name': vacancy.name,
            'url': vacancy.url,
            'payment': vacancy.payment,
            'description': vacancy.description
        })

        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, indent=4)

    def get_vacancy(self) -> List[Vacancies]:
        try:
            with open(self.filename, 'r') as file:
                vacancies_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies_data = []

        vacancies = []
        for data in vacancies_data:
            vacancies.append(Vacancies(
                data['name'],
                data['url'],
                data['payment'],
                data['description']
            ))
        return vacancies

    def delete_vacancy(self, vacancy: Vacancies):
        try:
            with open(self.filename, 'r') as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        vacancies = [v for v in vacancies if not (v['name'] == vacancy.name and v['url'] == vacancy.url)]

        with open(self.filename, 'w') as file:
            json.dump(vacancies, file, indent=4)
class HHAPI:
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def load_vacancies(self, keyword: str):
        self.params['text'] = keyword
        vacancies = []
        while self.params.get('page') != 20:  # Ограничиваем количество страниц
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()  # Проверяем, что запрос выполнен успешно
            vacancies.extend(response.json()['items'])
            self.params['page'] += 1
        return vacancies

def user_interaction():
    hh_api = HHAPI()
    file_worker = JsonFile('vacancies.json')

    keyword = input("Введите поисковый запрос для вакансий: ")
    vacancies_data = hh_api.load_vacancies(keyword)

    vacancies = []
    for data in vacancies_data:
        salary = data['salary']
        salary_value = salary['from'] if salary and salary['from'] else 0
        vacancies.append(Vacancies(
            data['name'],
            data['alternate_url'],
            salary_value,
            data['snippet']['requirement']
        ))

    for vacancy in vacancies:
        file_worker.add_vacancy(vacancy)

    n = int(input("Введите количество топ вакансий по зарплате: "))
    top_vacancies = sorted(vacancies, key=lambda x: x.payment, reverse=True)[:n]
    for vacancy in top_vacancies:
        print(f"Title: {vacancy.name}, Salary: {vacancy.payment}, URL: {vacancy.url}")

    keyword_in_description = input("Введите ключевое слово для поиска в описании: ")
    vacancies_with_keyword = [
        v for v in vacancies
        if v.description is not None and keyword_in_description in v.description
    ]
    for vacancy in vacancies_with_keyword:
        print(f"Title: {vacancy.name}, Description: {vacancy.description}, URL: {vacancy.url}")

if __name__ == "__main__":
    user_interaction()
