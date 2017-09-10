import news_api_client as client 

def test_basic():
    ''' '''
    news = client.get_news_from_source()
    print news
    assert len(news) > 0
    news = client.get_news_from_source(sources=['cnn'], sortBy='top')
    assert len(news) > 0
    print 'test_basic passed'

if __name__ == '__main__':
    test_basic()