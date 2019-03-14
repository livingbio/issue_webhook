# ISSUE CLOSED BELL

closing issue 總令人開心，或許可以每 close 一個 issue 就自動敲鐘(擊鼓、放音樂... 之類的)，振奮人心~ XD

## 硬體設定

* 需要準備一台主機
    * **實務**: 目前用的是 Raspberry Pi 3B
* 需要準備喇叭
* 需要有一個外部IP或domain name，並且對外開放5567 port
    * **實務**: `autossh -f -N -C -R "*:5567:localhost:5567" -p 325 admin@banyh.synology.me`

## 開始執行

執行前需要`pip install flask`安裝。然後用`python issue.py`執行。

**實務**: 已經設定好開機時自動執行 `/home/pi/update_webhook.sh`。

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
* **實務**: 已經設定好開機時自動執行 `/home/pi/update_webhook.sh`，裡面會自動 pull master。
    * 因此只要在github上新增音效，然後電源拔插重開機，就會更新上去。
