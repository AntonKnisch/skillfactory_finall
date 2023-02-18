import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from env import Env


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def env():
    return Env()
