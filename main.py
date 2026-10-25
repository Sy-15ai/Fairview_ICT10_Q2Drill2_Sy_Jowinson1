from pyscript import document

# List of ICT Club members
club_members = [
    "John Smith",
    "Jowi Sy",
    "Maria Santos",
    "Carlos Reyes",
    "Sofia Garcia",
    "Daniel Cruz"
]


def check_member(event):

    # Get the names from the input fields
    first_name = document.querySelector("#firstName").value
    last_name = document.querySelector("#lastName").value

    # Combine the first and last name
    full_name = first_name.strip() + " " + last_name.strip()

    # Check if the name is in the club members list
    member_status = full_name in club_members

    # Store the messages
    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    # Store the final result
    result = messages[member_status]

    # Display the result
    document.querySelector("#result").innerText = result