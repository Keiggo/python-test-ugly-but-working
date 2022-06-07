from ast import Assert
from email.headerregistry import ContentTransferEncodingHeader
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# class BasePage(object):
#     def __init__(self, driver):
#         self.driver = driver

class LoginPage:
    #login page elements
    def __init__(self, driver):
        self.driver = driver
        self.emailField = driver.find_element_by_css_selector('input[name="username"]')
        passwordField = driver.find_element_by_css_selector('input[name="password"]')
        loginButton = driver.find_element_by_css_selector('input[type="submit"]')

    #login page methods
    def getUsernameField(self):
        return self.emailField

    def enterUsername(self, username):
        return self.emailField.send_keys(username)

# class adminPage:
#     #admin page elements
#     logo = driver.find_element_by_css_selector('a[href="/admin/"]')
#     viewSiteLink = driver.find_element_by_link_text('View site')
#     changePasswordLink = driver.find_element_by_link_text('Change password')
#     logOutLink = driver.find_element_by_link_text('Log out')
#     authenticationAndAuthorizationHeader = driver.find_element_by_link_text('Authentication and Authorization')
#     groupsLink = driver.find_element_by_link_text('Groups')
#     addGroupsLink = driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/add/"]')
#     changeGroupsLink = driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"]')
#     coreHeader = driver.find_element_by_link_text('Grains')
#     usersLink = driver.find_element_by_link_text('Users')
#     addUsersLink = driver.find_element_by_css_selector('a[href="/admin/core/user/add/"]')
#     # changeUsersLink
#     # grainsHeader
#     # grainsUserProfilesLink
#     # addGrainsUserProfilesLink
#     # changeGrainsUserProfulesLink
#     # ordersLink
#     # addOrdersLink
#     # changeOrdersLink
#     # suppliersLink
#     # addSuppliersLink
#     # changeSuppliersLink 