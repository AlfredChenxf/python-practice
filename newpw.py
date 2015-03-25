__author__ = 'Alfred'

db = {}


def newuser():
    global name
    while True:
        name = raw_input('Enter your name: ')
        if name in db:
            print "This name is used, please try another"
        else:
            break

    passwd = raw_input('Enter your password: ')
    db[name] = passwd


def olduser():
    name = raw_input('login: ')
    enterpwd = raw_input('password: ')

    passwd = db[name]
    if enterpwd == passwd:
        print "wellcome back", name
    else:
        print "invalid password"


def showmeu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Enter choice:"""

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'

            print "\n You picked: %s" % choice

            if choice not in 'neq':
                print "Please try again"
            else:
                chosen = True
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()

if __name__ == '__main__':
    showmeu()
