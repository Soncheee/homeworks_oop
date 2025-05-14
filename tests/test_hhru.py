import pytest
import json
from unittest.mock import patch, MagicMock
from src.hhru import Vacancies, JsonFile, HHAPI

@pytest.fixture
def vacancy1():
    return Vacancies("Developer", "http://example.com/1", 100000, "Python developer")

@pytest.fixture
def vacancy2():
    return Vacancies("Designer", "http://example.com/2", 90000, "UI/UX designer")

@pytest.fixture
def file_worker(tmp_path):
    file_path = tmp_path / "test_vacancies.json"
    return JsonFile(str(file_path))

def test_vacancy_initialization(vacancy1):
    assert vacancy1.name == "Developer"
    assert vacancy1.url == "http://example.com/1"
    assert vacancy1.payment == 100000
    assert vacancy1.description == "Python developer"

def test_vacancy_comparison(vacancy1, vacancy2):
    assert vacancy1 > vacancy2
    assert not (vacancy1 < vacancy2)
    assert not (vacancy1 == vacancy2)

def test_add_vacancy(file_worker, vacancy1):
    file_worker.add_vacancy(vacancy1)
    with open(file_worker.filename, 'r') as file:
        vacancies = json.load(file)
        assert len(vacancies) == 1
        assert vacancies[0]['name'] == "Developer"

def test_get_vacancy(file_worker, vacancy1):
    file_worker.add_vacancy(vacancy1)
    vacancies = file_worker.get_vacancy()
    assert len(vacancies) == 1
    assert vacancies[0].name == "Developer"

def test_delete_vacancy(file_worker, vacancy1):
    file_worker.add_vacancy(vacancy1)
    file_worker.delete_vacancy(vacancy1)
    with open(file_worker.filename, 'r') as file:
        vacancies = json.load(file)
        assert len(vacancies) == 0

@patch('requests.get')
def test_load_vacancies(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {'items': [{'name': 'Developer', 'alternate_url': 'http://example.com/1', 'salary': {'from': 100000}, 'snippet': {'requirement': 'Python developer'}}]}
    mock_get.return_value = mock_response

    hh_api = HHAPI()
    vacancies = hh_api.load_vacancies("Python developer")

    assert len(vacancies) == 20
    assert vacancies[0]['name'] == 'Developer'
