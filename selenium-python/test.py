#  Copyright 2025 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# The chrome and chromedriver installation can take some time.
# Give 5 minutes to install everything.
TIMEOUT = 5 * 60 * 1000


@pytest.fixture(scope="module")
def driver():
    # By default, the test uses the latest stable Chrome version.
    # Replace the "stable" with the specific browser version if needed,
    # e.g. 'canary', '115' or '144.0.7534.0' for example.
    browser_version = "stable"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.browser_version = browser_version

    service = Service(service_args=["--log-path=chromedriver.log", "--verbose"])

    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()


@pytest.mark.timeout(TIMEOUT)
def test_should_be_able_to_navigate_to_google_com(driver):
    """This test is intended to verify the setup is correct."""
    driver.get("https://www.google.com")
    logging.info(driver.title)
    assert driver.title == "Google"


@pytest.mark.timeout(TIMEOUT)
def test_issue_reproduction(driver):
    """Add test reproducing the issue here."""
    driver.get("https://wpt.live/webdriver/tests/support/html/test_actions_scroll.html")
    target = driver.find.css("#scrollable", all=False)
    driver.actions.sequence("wheel", "wheel_id").scroll(0, 0, 5, 10, origin=target).perform()




# def test_scroll_scrollable_overflow(session, test_actions_scroll_page, wheel_chain):
#     target = session.find.css("#scrollable", all=False)

#     wheel_chain.scroll(0, 0, 5, 10, origin=target).perform()

#     events = get_events(session)
#     assert len(events) == 1
#     assert events[0]["type"] == "wheel"
#     assert events[0]["deltaX"] == 5
#     assert events[0]["deltaY"] == 10
#     assert events[0]["deltaZ"] == 0
#     assert events[0]["target"] == "scrollable-content"


# @pytest.fixture
# def test_actions_scroll_page(session, url):
#     session.url = url("/webdriver/tests/support/html/test_actions_scroll.html")

# @pytest.fixture
# def wheel_chain(session):
#     return session.actions.sequence("wheel", "wheel_id")


# def test_scroll_events_for_overflow(session, test_actions_scroll_page, wheel_chain):
#     target = session.find.css("#scrollable", all=False)

#     wheel_chain.scroll(0, 0, 5, 10, origin=target).perform()

