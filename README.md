# django-filter-package #

## 專案介紹 ##

本專案在Python的Django網站框架中，利用django-filter套件，來開發多條件的查詢功能，可以搭配[[Django教學18]善用Django Filter來快速建構多條件的查詢功能](https://www.learncodewithmike.com/2020/05/django-filter.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /movies (例：http://127.0.0.1:8000/movies/) 後，即可看到查詢的畫面。

![Alt text](https://1.bp.blogspot.com/-vp4cQDbqEc4/XspqRxaZbvI/AAAAAAAACbo/3jUQist6KVYD5zgnrZ6i-a2Ggz5mZSNCwCK4BGAsYHg/django_filter.PNG "Optional title")
