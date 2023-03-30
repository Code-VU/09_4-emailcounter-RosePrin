def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    emails = {}

    for line in handle:
        if line.startswith('From '):
            line_words = line.split()
            email_address = line_words[1]
            
            if email_address not in emails:
                emails[email_address] = 1
            else:
                emails[email_address] += 1

    max_key = max(emails, key=emails.get)
    print(max_key, emails[max_key])
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
