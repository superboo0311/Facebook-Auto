from selenium import webdriver
import time
import random
import sentencegen as gen

def commentspam(num,timedelta,postURL,cmt):
    #your credentials here
    userId = "itunesvnpaid@gmail.com"
    password = "mrdat123a"

    #need chromedriver for your current chrome version
    browser = webdriver.Chrome("/Users/boo/Downloads/chromedriver")
    
    fbURL = "https://m.facebook.com"
    browser.get(fbURL)
    time.sleep(8)

    #fill credentials and log in
    userIdField = browser.find_element_by_id("m_login_email")
    passwordField = browser.find_element_by_id("m_login_password")   
    loginButton = browser.find_elements_by_tag_name("button")[0]
    userIdField.send_keys(userId)
    passwordField.send_keys(password)
    loginButton.click()
    

    #wait for two factor auth
    time.sleep(5)
    notNowButton = browser.find_element_by_tag_name("a")
    notNowButton.click()
    #should be able to get into post now
    for i in postURL:
        browser.get(i)
        time.sleep(10)
        # comment x many times
        for j in cmt:
            time.sleep(timedelta)
            commentBox = browser.find_element_by_id("composerInput")
            try:
                commentBox.send_keys(j)
            except:
                #try 10 times max with 1 second delay if comment box is not available. 
                for i in range(0,10):
                    try:
                        time.sleep(1)
                        commentBox.send_keys(j)
                        break
                    except:
                        pass
            #leave this delay fixed. Usually takes 2-3 seconds for the comment to get posted
            time.sleep(10)
            try:
                sendButton = browser.find_elements_by_tag_name("button")[0]
                sendButton.click()
            except:
                #try 10 times max with 1 second delay if comment box is not available. 
                for i in range (0,10):
                    try:
                        time.sleep(1)
                        sendButton = browser.find_elements_by_tag_name("button")[0]
                        sendButton.click()
                        break
                    except:
                        pass
            
        
# list of post need to comment
postUrl=["https://m.facebook.com/groups/1344873668901428/permalink/5170024369719653/",
         "https://m.facebook.com/groups/330966831016688/permalink/1157555105024519/",
         "https://m.facebook.com/groups/vieclamquanbinhtan/permalink/5146164988765265/",
         "https://m.facebook.com/groups/danbinhchanhnew/permalink/5067636606646783/",
        "https://m.facebook.com/groups/377156329334346/permalink/1611130729270227/",
        "https://m.facebook.com/groups/pgpbkhuvucmienbac/permalink/425006882503944/",
        "https://m.facebook.com/groups/101725677141334/permalink/982419969071896/",
        "https://m.facebook.com/groups/406678599486879/permalink/2337853006369419/",
        "https://m.facebook.com/groups/timvieclamtaihcmsaigon2/permalink/3147531062169326/",
        "https://m.facebook.com/groups/275568093015527/permalink/1154702545102073/",
        "https://m.facebook.com/groups/280503298758830/permalink/2311721458970327/"]

cmt = ["up"]
# call method ( how many repeate comment, how long of the delay comment, list of post )
commentspam(1,8,postUrl,cmt)

print("finish")
