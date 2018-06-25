from selenium import webdriver
import time
import pickle
import csv


def main():
    """
    Get tweets by scrolling down a Twitter search page
    :return:
    """
    # Open search page in a browser
    browser = webdriver.Safari()
    url = 'https://twitter.com/search?src=typd&q=mad%20near%3A%22Massachusetts%2C%20USA%22%20within%3A15mi'
    browser.get(url)
    browser.maximize_window()

    # Dismiss login element
    page_body = browser.find_element_by_class_name('container')
    page_body.click()

    win_size = browser.get_window_size()

    # Scroll down page
    for i in range(2):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_win_size = browser.get_window_size()

    # Get tweets
    tweets = browser.find_elements_by_class_name('tweet-text')
    tweet_texts = [t.text for t in tweets]

    outfile = open('tweets.csv', 'w')
    outwriter = csv.writer(outfile)
    outwriter.writerows(tweet_texts)
    outfile.close()

    for t in tweet_texts:
        print(t, '\n')

    #save_file = open('tweets.pickle', 'wb')
    #pickle.dumps(tweet_texts, save_file)
    #save_file.close()

    browser.close()


if __name__ == '__main__':
    main()
    exit()