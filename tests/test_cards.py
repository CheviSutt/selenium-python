# Go to statsroyale
# open cards page
# assert Ice Spirit is displayed
# $ pip install pytest

# update project to pytest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.pages import Pages


@pytest.fixture
def royale():
    drvr = webdriver.Chrome()
    drvr.get('https://statsroyale.com')
    pages = Pages(drvr)
    yield pages
    drvr.quit()


card_names = ['Ice Spirit', 'Mirror', 'Lava Hound']


@pytest.mark.parametrize('card_name', card_names)
def test_card_is_displayed(royale, card_name):
    # Go to statsroyale
    # open cards page
    # assert Ice Spirit is displayed
    # $ pip install pytest

    # cards_link = driver.find_element(By.CSS_SELECTOR, "a[href='/cards']")
    # cards_link.click()
    # ice_spirit = driver.find_element(By.CSS_SELECTOR, "a[href*='Ice+Spirit']")
    # assert ice_spirit.is_displayed()
    royale.cards.goto()
    card = royale.cards.get_card_by_name(card_name)
    assert card.is_displayed


def test_ice_spirit_details_are_correct(driver):
    # Go to statsroyale
    # open cards page
    # assert Ice Spirit is displayed
    # $ pip install pytest
    # assert name, type, arena, and variety are correct

    # driver = webdriver.Chrome()
    # driver.get('https://statsroyale.com')
    # driver.find_element_by_css_selector("a[href='/
    cards_link = driver.find_element(By.CSS_SELECTOR, "a[href='/cards']")
    cards_link.click()

    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    card_deets = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(', ')
    card_type = card_deets[0]
    card_arena = card_deets[1]
    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='card__count']")

    assert card_name == 'Ice Spirit'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'
    assert card_rarity == 'Common'


assert True
