## Workshop Data Directory
This directory  contains the core CSV data files used to power the workshop website.
These files manage dynamic content such as the schedule, current instructors and staff, historical faculty/TAs, and course participants.

### event-schedule.csv

Stores the complete day-by-day timetable of events, lectures, labs, and social gatherings for the workshop.

This file has the following elements:
- date: The calendar date of the event (e.g., 5/17/2026).
- start_time: The start time in 24-hour format (e.g., 18:00).
- end_time: The end time in 24-hour format (e.g., 21:00).
- room: The physical location or venue where the event takes place (e.g., MBL Club (100 Water St.)).
- item_id: A unique machine-readable slug/identifier for the event item (e.g., opening-reception).
- category: The type of session. Common values include lecture, lab, or other.
- title: The display title of the session or event.
- presenter: The name of the instructor or speaker leading the session (leave blank if not applicable). These generally should match the `ID` element of a faculty found in the `faculty-registry.csv` 
- material_location: Path or URL to slides, code repositories, or auxiliary files associated with the session (leave blank if none).

Ensure all times use 24-hour formatting (HH:MM).
Use clear, concise titles and lowercase slug identifiers for item_id. 
Leave presenter and material_location empty (NaN or blank) if the event is a break, reception, or unstructured block.

### faculty-registry.csv

Maintains the registry of current workshop personnel (directors, faculty, lead TAs, TAs, and course assistants), powering both the people listing page and individual instructor profile routing.

This fil has the following elements:
- name: Full name of the faculty member or staff (e.g., Peter Beerli).
- ID: A URL-friendly slug matching their individual profile page or filename (e.g., peter-beerli).
- role: Their organizational role. Accepted values are handled dynamically by the site layout and include director, co-director, faculty, lead TA, ta, and CA.
- email: Professional contact email address (optional/can be left blank).

Be sure to provide a unique URL-safe slug in the ID column corresponding to their profile page, typically this is the slugged version of first name last name.
Assign exact role categories (director, co-director, faculty, lead TA, ta, CA) so that the template logic correctly groups and labels them on the website.

### former-faculty.csv
Archives historical workshop instructors, teaching assistants, and course assistants from past years.

This file contains the following columns:
- Name: Full name of the former personnel.
- Role: Their historical role in the workshop (e.g., Faculty, lead TA, TA, CA).
- Institution: Their affiliated institution at the time or historically.
- URL: An external personal or lab website link (optional). If provided, their name renders as a hyperlink; if left blank, their name appears as plain text.


### participants.csv

Lists all registered attendees and participants participating in the current workshop session.

- Name: Full name of the participant.
- Institution: Their current academic or professional institution.