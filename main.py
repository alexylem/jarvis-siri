import time # sleep interval
import imaplib # connect to gmail
import email # parsing emails
import os # build path
import argparse # manage program arguments
import logging # logging
from subprocess import check_output # run shell commands

# Global variables
global logger

def main(username, password, interval):
    logger.debug ('Connecting to gmail imap server...')
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    logger.debug ('Authentificating %s', username)
    mail.login(username, password)
    logger.debug ('Checking what was latest note id...')
    #mail.list () # list all labels, apparently not needed
    result, tidnote = mail.select ("Notes")
    last_checked=int(tidnote[0])
    logger.debug ('It is %d', last_checked)
    logger.debug ('Checking new Notes...')
    while True:
        result, tidnote = mail.select ("Notes")
        idnote=int(tidnote[0])
        if idnote > last_checked:
            logger.debug ('New Note received (%d)', idnote)
            last_checked = idnote
            result, data = mail.fetch(idnote, "(RFC822)")
            message = email.message_from_string(data[0][1])
            payload = message.get_payload(decode=True)
            order = payload.strip ()
            logger.debug ('Order: %s', order)
            output = check_output([os.path.join (".", "jarvis.sh"), "-x", order])
            logger.debug ('Output: %s', output)
        #else:
            #logger.debug ('No new Note (last note id still %d)', idnote)
        time.sleep (interval)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Siri Notes checker for Jarvis')
    parser.add_argument('-u', '--username', help='gmail username', required=True)
    parser.add_argument('-p', '--password', help='gmail password', required=True)
    parser.add_argument('-i', '--interval', help='check interval', type=int, default=1)
    parser.add_argument('-v', '--verbose', help='debug information', action='store_true')
    
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG) # DEBUG, INFO, WARNING, ERROR, CRITICAL
    else:
        logging.basicConfig(level=logging.INFO) # DEBUG, INFO, WARNING, ERROR, CRITICAL
    logger = logging.getLogger("jarvis-siri")
    try:
        main(args.username, args.password, args.interval)
    except KeyboardInterrupt:
        print # new line
        pass
    except Exception, e:
        logger.error(str(e))
