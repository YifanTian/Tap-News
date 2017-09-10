''' use  cloudAMQP_client defined in another module, test cloudAMQP_client module'''

from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://zzlvmljf:7IM0kcsTGo1Pbr1kYY79TiDTuM6i7lpM@donkey.rmq.cloudamqp.com/zzlvmljf"
TEST_QUEUE_NAME = "fullstack1"


def test_basic():
    ''' test cloudAMQP_client basic utility '''
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sent_message = {"test": "test"}
    client.sendMessage(sent_message)
    received_message = client.getMessage()

    assert sent_message == received_message
    print "test_basic passed"


if __name__ == "__main__":
    test_basic()
