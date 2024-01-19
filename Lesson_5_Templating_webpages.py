"""Fills in an HTML template with user data to construct a custom webpage."""

import webpage

# Collect user profile data.
first_name = input("What's your first name? ")
email = input("What's your email? ")
location = input ("Where are you located? ")

# Construct a personalized page header for the logged in user.
header_title = "<h1>Guest's profile</h1>"
header_subtitle = "<h2>Hello, " + first_name + "!</h2>"
header_content = "<p>Have a nice day in " + location + " today</p>"
page_header = header_title + header_subtitle + header_content

# Construct the main profile page content.
section_title = "<h2>About guest:"+email+"!</h2>"
section_text = first_name + "<p>this is a cool bio.</p>"
section_footer = "<p>Notifications: 4</p>"
button = "<button>Like</button>"
page_content = section_title + section_text + button + section_footer

# The final HTML body combines all the elements, in order.
webpage.render(page_header + page_content)
