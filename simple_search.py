def reflex_vacuum_agent(location , status):
  if status == "Dirty":
    return "Suck"
  elif location == "A":
    return "Right"
  elif location == "B":
    return "Left"
    
    
    location = "A"
status = "Dirty"


action =reflex_vacuum_agent(location , status)
print(f"Location : {location}, Status : {status} , Action : {action} ")

def reflex_vacuum_agent(location , status):
  if status == "Dirty":
    return "Suck"
  elif location == "A":
    return "Right"
  elif location == "B":
    return "Left"
    
    location = "A"
status = "Dirty"
locations = ["A", "B"]
