# selenium cheatsheet <https://gist.github.com/huangzhichong/3284966>

# sudo pip3 install selenium
import time
from selenium.server.standalone import webdriver
from selenium.webdriver.common.keys import Keys
import csv

aList = []
with open('addy.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter = '\t', quotechar = '|')
    for row in filereader:
        aList += row

print(aList)

browser = webdriver.Chrome()

# if this throws an exception of 'geckodriver'
# you need to download the latest
# at https://github.com/mozilla/geckodriver/releases
# then in terminal:
# export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
# to add that to searchable path

# opens Firefox
browser = webdriver.chrome()
browser.get('https://grubhub.com')

# this maybe necessary so you have the variable 'browser' that you can manipulate
# after entering order to fill out rest of form...

# <input ng-model-options="{ updateOn: 'default blur', debounce: {'default': 1000, 'blur' : 0} }" name="firstName" ng-model="nuVm.userFormObject.firstName" class="s-form-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required ng-valid-pattern" required="" autofocus="" ng-disabled="nuVm.widgetDisabled" ng-class="{disabled: nuVm.widgetDisabled}" placeholder="First name" spellcheck="false" ng-pattern="/^([a-z'.,-])+$/i" type="text">

# NOTE -- the WebDriver may not wait for the page to load, you'd better using explicit and implicit waits.
time.sleep(3)

try:
    address = browser.find_element_by_class_name("addressInput-textInput")
except:
    print('Was not able to find an element with that name.')

time.sleep(3)
# adds address to site
address.send_keys(aList[0])

    # Not sure why I can't just submit
# time.sleep(2)
# address.submit()
    # this isn't working either?
# Keys.ENTER

#<button type="button" class="s-btn s-btn-primary startOrderForm-submit-btn ghs-spinner" id="ghs-startOrder-searchBtn" ghs-progress-indicator-add="" ng-class="{'disabled': $ctrl.searchInProgress, spin: $ctrl.searchInProgress}" ng-click="$ctrl.submitForm(true)"><!----><span ng-if="!$ctrl.useDiscoveryInteraction">Find food</span><!----> <!----><span class="ghs-spinner-container"><i class="ghs-spinner-rotate icon-spinner"></i></span></button>
submitButton = browser.find_element_by_class_id("ghs-startOrder-searchBtn")
submitButton.send_keys(Keys.ENTER)
