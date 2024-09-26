import getpass
import imaplib
import pprint

# IMAP server and port for Gmail
GOOGLE_IMAP_SER = 'imap.googlemail.com'
IMAP_PORT = 993

def check_email(username, password):
    try:
        # Connect to the server
        mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SER, IMAP_PORT)
        mailbox.login(username, password)
        print("Logged in successfully.")
        
        # Select the mailbox (Inbox)
        mailbox.select('inbox')
        
        # Search for all emails
        status, messages = mailbox.search(None, 'ALL')
        
        if status != 'OK':
            print("Failed to retrieve emails.")
            return
        
        # Iterate over the email messages
        for num in messages[0].split():
            status, msg_data = mailbox.fetch(num, '(RFC822)')
            if status != 'OK':
                print(f"Failed to fetch email {num}.")
                continue
            
            print(f"\nEmail ID: {num.decode()}")
            pprint.pprint(msg_data[0][1].decode('utf-8'))
        
    except imaplib.IMAP4.error as e:
        print(f"IMAP error occurred: {e}")
    finally:
        # Ensure the connection is closed
        mailbox.logout()

if __name__ == '__main__':
    username = input('Email: ')
    password = getpass.getpass(prompt='Enter password: ')
    check_email(username, password)
