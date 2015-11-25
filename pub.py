from settings import r
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]
    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print 'Welcome to {channel}'.format(**locals())

    while True:
        message = raw_input('Enter a message: ')

        if message.lower() == 'exit':
            break

        message = '{name} says: {message}'.format(**locals())

        r.publish(channel, message)
        for item in pubsub.listen():
            print item['data']
