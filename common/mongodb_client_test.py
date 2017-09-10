''' use  mongodb_client defined in another module'''

import mongodb_client as client


def test_basic():
    ''' test basic mongodb client utility '''
    database = client.get_db('tap-news2')
    database.testCollection.drop()
    assert database.testCollection.count() == 0
    database.testCollection.insert({'tap-news2': 1, 'hello': 'world'})
    assert database.testCollection.count() == 1
    # database.testCollection.drop()
    # assert database.testCollection.count() == 0
    print 'test_basic passed.'

def test_replace():
    NEWS_TABLE_NAME = "news-test"
    db = client.get_db()
    db.testCollection.drop()
    db.testCollection.insert({'tap-news2': 1, 'hello': 'world'})
    assert db.testCollection.count() == 1
    db.testCollection.drop()
    assert db.testCollection.count() == 0
    # db[NEWS_TABLE_NAME].replace_one({'digest': '123'}, 'txt1', upsert=True)
    # print(db[NEWS_TABLE_NAME])
    # assert database.testCollection.count() == 0



if __name__ == '__main__':
    test_replace()
