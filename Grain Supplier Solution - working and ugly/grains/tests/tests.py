from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:8000/admin/')
driver.maximize_window()

class LoginPage:
#login page elements
    emailField = driver.find_element_by_css_selector('input[name="username"]')
    passwordField = driver.find_element_by_css_selector('input[name="password"]')
    loginButton = driver.find_element_by_css_selector('input[type="submit"]')

#Ensure that the field selected by default is the email field
assert driver.switch_to.active_element == LoginPage.emailField
driver.find_element_by_id('djHideToolBarButton').click()

LoginPage.emailField.send_keys("admin@admin.com")
LoginPage.passwordField.send_keys("admin")
LoginPage.loginButton.click()

class AdminPage:
#admin page elements
    logo = driver.find_element_by_css_selector('a[href="/admin/"]')

    viewSiteLink = driver.find_element_by_css_selector('a[href="/"]')
    changePasswordLink = driver.find_element_by_css_selector('a[href="/admin/password_change/"]')
    logOutLink = driver.find_element_by_css_selector('a[href="/admin/logout/"]')
    
    authenticationAndAuthorizationHeader = driver.find_element_by_css_selector('a[href="/admin/auth/"]')
    groupsLink = driver.find_element_by_css_selector('a[href="/admin/auth/group/"]')
    addGroupsLink = driver.find_element_by_css_selector('a[href="/admin/auth/group/add/"]')
    changeGroupsLink = driver.find_element_by_css_selector('a[href="/admin/auth/group/"][class="changelink"]')
    
    coreHeader = driver.find_element_by_css_selector('a[href="/admin/core/"]')
    usersLink = driver.find_element_by_css_selector('a[href="/admin/core/user/"]')
    addUsersLink = driver.find_element_by_css_selector('a[href="/admin/core/user/add/"]')
    changeUsersLink = driver.find_element_by_css_selector('a[href="/admin/core/user/"][class="changelink"]')
    
    grainsHeader = driver.find_element_by_css_selector('a[href="/admin/grains/"]')
    grainsUserProfilesLink = driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"]')
    addGrainsUserProfilesLink = driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/add/"]')
    changeGrainsUserProfulesLink = driver.find_element_by_css_selector('a[href="/admin/grains/grainsuserprofile/"][class="changelink"]')
    ordersLink = driver.find_element_by_css_selector('a[href="/admin/grains/order/"]')
    addOrdersLink = driver.find_element_by_css_selector('a[href="/admin/grains/order/add/"]')
    changeOrdersLink = driver.find_element_by_css_selector('a[href="/admin/grains/order/"][class="changelink"]')
    suppliersLink = driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"]')
    addSuppliersLink = driver.find_element_by_css_selector('a[href="/admin/grains/supplier/add/"]')
    changeSuppliersLink = driver.find_element_by_css_selector('a[href="/admin/grains/supplier/"][class="changelink"]')

    listOfElementsInOrder = [logo, viewSiteLink, changePasswordLink, logOutLink, authenticationAndAuthorizationHeader, groupsLink, addGroupsLink, changeGroupsLink, coreHeader, usersLink, addUsersLink, changeUsersLink, grainsHeader, grainsUserProfilesLink, addGrainsUserProfilesLink, changeGrainsUserProfulesLink, ordersLink, addOrdersLink, changeOrdersLink, suppliersLink, addSuppliersLink, changeSuppliersLink]
    
    def checkTabOrder():
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
    
        for i in range(len(AdminPage.listOfElementsInOrder)):
            actions.perform()
            assert driver.switch_to.active_element == AdminPage.listOfElementsInOrder[i]

AdminPage.checkTabOrder()

driver.quit()