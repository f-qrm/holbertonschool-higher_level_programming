import logging

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Must be a string")
        return
    if not isinstance(attendees, list):
        logging.error("Must be a list of dictionaries")
        return
    for i in attendees:
        if not isinstance(i, dict):
            logging.error("N/A")
            return
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, 1):
        cpTemplate = template
        cpTemplate = cpTemplate.replace("{name}", attendee.get("name") or "N/A")
        cpTemplate = cpTemplate.replace("{event_title}", attendee.get("event_title") or "N/A")
        cpTemplate = cpTemplate.replace("{event_date}", attendee.get("event_date") or "N/A")
        cpTemplate = cpTemplate.replace("{event_location}", attendee.get("event_location") or "N/A")
        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(cpTemplate)
