# ISSUE CLOSED BELL

closing issue 總令人開心，或許可以每 close 一個 issue 就自動敲鐘(擊鼓、放音樂... 之類的)，振奮人心~ XD

## 硬體設定

* 需要準備一台主機(例如 RaspberryPI or Arduino or PC or Mac)，有speaker
* 需要有一個外部IP或domain name，並且對外開放5567 port

## 開始執行

唯一的需求是`pip install flask`。

```
python issue.py
```

## 設定Webhook

在repo setting裡面，有一個webhook的選項，新增webhook：

1. payload url 設為 `http://{host_name}:5567/github_issues`
2. content type 設為 JSON
3. trigger event 只需要選 Issues

## 設定音效

* opened issue的音效由開issue的login名稱決定
    * 例如，在`opened`資料夾內，放`ash.mp3`或`ash.m4a`或`ash.wav`都是代表`ash`的音效
    * 沒有對應檔案，則使用`default.m4a`
* closed issue的音效由assignee的login名稱決定
    * 例如，在`closed`資料夾內，放`ash.mp3`或`ash.m4a`或`ash.wav`都是代表`ash`的音效
    * 沒有對應檔案，則使用`default.m4a`
