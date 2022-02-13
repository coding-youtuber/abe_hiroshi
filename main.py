# ランダム機能を使うためにデフォルトライブラリを読み込む
import random
# ブラウザ操作のためのツール「Selenium」
from selenium import webdriver
# ChromeのDriverを使うために読み込む。最新版にupdate例:「pip install chromedriver-binary==98.0.4758.80.0」
import chromedriver_binary
# 時間計測のためにデフォルトライブラリを読み込む
import time


def open_mutiple_windows():
    # 時間計測の開始時刻
    start = time.time()

    # 開くウィンドウの数
    N = 100
    # デュアルディスプレイ両方で表示
    DUAL_DISPLAY_OFFSET_X = 1280
    # ホームページを表示する横幅
    WINDOW_SIZE_WIDTH = 1000
    # ホームページを表示する縦幅
    WINDOW_SIZE_HEIGHT = 700
    # Chromeのドライバー
    driver = webdriver.Chrome()
    # ホームページのURL
    page_url = "http://abehiroshi.la.coocan.jp/"
    # ウィンドウのサイズを設定
    driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
    # ウィンドウの位置を設定
    driver.set_window_position(DUAL_DISPLAY_OFFSET_X, 0)
    # 指定したURLのページを開く
    driver.get(page_url)
    print(f'阿部寛HP #1 表示完了 time:{format(time.time() - start, "0.2f")}秒')

    # 画面全体の横幅（デュアルディスプレイではなく一つのウィンドウ）
    width = driver.get_window_size().get("width")
    # 画面全体の縦幅
    height = driver.get_window_size().get("height")

    # 99回同じ操作を繰り返す
    for i in range(N - 1):
        # 新しいウィンドウを開く
        driver.switch_to.new_window('window')
        # ウィンドウのサイズは同じなのでコメントアウト
        # driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
        # ウィンドウの位置をランダムで決める
        driver.set_window_position(random.randint(
            0, DUAL_DISPLAY_OFFSET_X + width * 0.5), random.randint(-height / 2, height * 0.75))
    # 指定したURLのページを開く
        driver.get(page_url)
        # 進捗表示
        print(
            f'阿部寛HP #{i + 2} 表示完了 time:{format(time.time() - start, "0.2f")}秒')

    # 最後に10秒待ってウィンドウを全て閉じる
    time.sleep(10)


def main():
    open_mutiple_windows()


if __name__ == '__main__':
    main()
