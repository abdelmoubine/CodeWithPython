is_man = True
is_arab = True

if is_man and is_arab:
    print("You are an Arab Man")

elif is_man and not (is_arab):
    print("You are a man but not arab")

elif not (is_man) and (is_arab):
    print("You are an arab woman")

else:
    print("you are not an arab man")