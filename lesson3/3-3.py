is_logged_in = True
is_admin = False

if is_logged_in:
    print ("The user is logged in.")
    if is_admin:
        print ("Show admin dashboard.")
    else:
        print ("Show regular user dashboard.")
else:
    print ("Redirect to login page.")
