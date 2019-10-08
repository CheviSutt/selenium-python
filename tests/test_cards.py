# Go to statsroyale
# open cards page
# assert Ice Spirit is displayed
# $ pip install pytest

# update project to pytest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from royale.pages.pages import Pages
from royale.services import card_service


@pytest.fixture
def royale():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')
    pages = Pages(driver)
    yield pages
    driver.quit()


# card_names = ['Ice Spirit', 'Mirror', 'Lava Hound']
api_cards = card_service.get_all_cards()


@pytest.mark.parametrize('api_card', api_cards)
def test_card_is_displayed(royale, api_card):
    # Go to statsroyale
    # open cards page
    # assert Ice Spirit is displayed
    # $ pip install pytest

    # cards_link = driver.find_element(By.CSS_SELECTOR, "a[href='/cards']")
    # cards_link.click()
    # ice_spirit = driver.find_element(By.CSS_SELECTOR, "a[href*='Ice+Spirit']")
    # assert ice_spirit.is_displayed()
    royale.cards.goto()
    card = royale.cards.get_card_by_name(api_card.name)
    assert card.is_displayed


@pytest.mark.parametrize('api_card', api_cards)
def test_ice_spirit_details_are_correct(royale, api_card):
    # Go to statsroyale
    # open cards page
    # assert Ice Spirit is displayed
    # $ pip install pytest
    # assert name, type, arena, and variety are correct

    # driver = webdriver.Chrome()
    # driver.get('https://statsroyale.com')
    # driver.find_element_by_css_selector("a[href='/
    royale.cards.goto()
    royale.cards.get_card_by_name(api_card.name).click()

    royale.card_details.wait_for_page_load()
    card = royale.card_details.get_base_card()

    assert card.name == api_card.name
    assert card.type == api_card.type
    assert card.arena == api_card.arena
    assert card.rarity == api_card.rarity


assert True
