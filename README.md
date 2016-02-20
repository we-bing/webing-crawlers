# webing-crawlers

## drawWordCloud.py

> 키워드로 검색되는 뉴스들의 본문요약을 분석해서 형태소(언어 표현의 최소 단위)들을 추출하고  빈도수를 기반으로 
wordCloud 형태로 출력해주는 스크립트

###Requirements

    $ pip install JPype1  # dependencies for konlpy 
    $ pip install konlpy  # a Python package for natural language processing (NLP) of the Korean language. 
    $ brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
    $ brew tap samueljohn/python
    $ brew install pygame
    

###Installation & run

    $ git clone git@github.com:we-bing/webing-crawlers.git 
    $ cd webing-crawlers
    # python drawWordCloud.py {"query for keywords"} {the number of keywords}


####Examples

    $ python drawWordCloud.py "오바마 대통령" 10
    $ cat wordcloud.csv
    
####Reference

  [Lucy Park's wordCloud](https://www.lucypark.kr/)
    
---------