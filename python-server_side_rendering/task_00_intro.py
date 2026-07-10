#!/usr/bin/python3
"""Generate invitation letters by filling a template per attendee."""
import logging

# Placeholders supported in the template, in the order they are filled.
PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def generate_invitations(template, attendees):
    """Render one invitation file per attendee from a template string.

    Args:
        template (str): Text containing "{name}", "{event_title}",
            "{event_date}" and "{event_location}" placeholders.
        attendees (list): List of dicts, one per attendee, providing
            values for the template placeholders.

    Writes one "output_<n>.txt" file per attendee (1-indexed). Missing
    placeholder values are filled in with "N/A". Logs an error and
    returns without writing anything if the inputs are invalid.
    """
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
        rendered = template
        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder) or "N/A"
            rendered = rendered.replace("{%s}" % placeholder, value)
        filename = f"output_{index}.txt"
        with open(filename, "w") as file:
            file.write(rendered)
