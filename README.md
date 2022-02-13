# 【検証】阿部寛のホームページ100個開くのに何秒かかるのか

![capture](https://user-images.githubusercontent.com/58985013/153735752-31a89e5c-3c45-4bfd-b03a-a04cbc3e1379.jpg)


# YouTube検証動画
https://youtu.be/u2_CthE8PSI


# 環境

```
selenium==4.1.0
```


# Selenium Chrome version

```bash
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 86
Current browser version is 98.0.4758.80 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```

↑こちらのエラーが出た場合、ChromeDriverのChromeのversionと通常のブラウジングで使用しているChromeのversionがあっていません。だからChromeDriverのversionをあげる必要があります。


## ChromeDriverをインストールする

[https://pypi.org/project/chromedriver-binary/#history](https://pypi.org/project/chromedriver-binary/#history)

```bash
pip install chromedriver-binary==98.0.4758.80.0
```

↑versionは適宜置き換えてください。

## 注意

```python
import chromedriver_binary
```

Pythonのコードでchromedriver_binaryをimportする必要があります。importしないとChromeDriverをupdateしても反映されません。


[(Mac)PythonのSeleniumで「chromedriveのpathの場所が見つからない」時の対応 - Qiita](https://qiita.com/ti104110/items/c64f493eb6214b36add1)

# windowまわりの処理

* windowのサイズを変更
* windowの位置を変更

この辺りの処理はこちらの記事を参考にしてください。


[https://www.selenium.dev/documentation/webdriver/browser/windows/](https://www.selenium.dev/documentation/webdriver/browser/windows/)
