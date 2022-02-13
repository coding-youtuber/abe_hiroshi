from selenium import webdriver

import chromedriver_binary

import time


def open_mutiple_tabs():
    """
    別ウィンドウではなくChromeの新規タブを開く場合
    """
    driver = webdriver.Chrome()
    page_url = "http://abehiroshi.la.coocan.jp/"
    driver.get(page_url)
    for i in range(100):
        driver.execute_script(f"window.open('{page_url}');")
        print(f"tab No.{i + 1}が開きました")

    print("すべてのブラウザが開きました")
    time.sleep(10)


def main():
    open_mutiple_tabs()


if __name__ == '__main__':
    main()
