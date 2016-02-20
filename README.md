# webing-crawlers

## drawWordCloud.py

> 키워드로 검색되는 뉴스들의 본문요약을 분석해서 형태소(언어 표현의 최소 단위)들을 추출하고  빈도수를 기반으로 
wordCloud 형태로 출력해주는 스크립트

###Requirements
 
    The installation steps assume that you have the following things installed:
- Python 2.7
- pip and setuptools Python packages. Nowadays pip requires and installs setuptools if not installed. Python 2.7.9 and later include pip by default, so you may have it already.
- lxml. Most Linux distributions ships prepackaged versions of lxml. Otherwise refer to http://lxml.de/installation.html
- OpenSSL. This comes preinstalled in all operating systems, except Windows where the Python installer ships it bundled.

=====
    $ pip install JPype1  # dependencies for konlpy 
    $ pip install konlpy  # a Python package for natural language processing (NLP) of the Korean language. 
    $ brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
    $ brew tap samueljohn/python
    $ brew install pygame
    

###Installation & run

    $ git clone https://github.com/we-bing/webing-crawlers.git 
    $ cd webing-crawlers
    # python drawWordCloud.py {"query for keywords"} {the number of keywords}


####Examples

    $ python drawWordCloud.py "오바마 대통령" 10
    $ cat wordcloud.csv
    
####Reference

  [Lucy Park's wordCloud](https://www.lucypark.kr/)
    
---------
