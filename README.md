# Martial Arts Academy

Martial Arts Academy is a Django web application for exploring martial arts, their training curriculum, and upcoming martial arts events.

## Features

- Browse martial arts
- View detailed information about each martial art
- Create, edit, and delete martial arts
- Browse and view curriculum items
- Create curriculum items and assign them to a martial art
- Browse martial arts events
- Filter events by event type
- View detailed information about events
- Create, edit, and delete events
- Assign multiple martial arts to an event
- Custom form validation
- User-friendly form labels, placeholders, help text, and error messages
- Disabled form field on martial art editing
- Delete confirmation pages
- Custom Django template filter
- Custom 404 page
- Template inheritance with a shared base template
- Reusable header and footer partial templates
- Global navigation
- Static images and CSS styling
- Responsive martial art cards on the home page

## Applications

The project contains three Django applications:

- `martial_arts` - manages martial arts
- `curriculum` - manages training curriculum items
- `events` - manages seminars, competitions, and galas

## Models

### MartialArt

Stores information about a martial art.

Main fields:

- Name
- Description

The martial art name must be unique.

### CurriculumItem

Stores training curriculum items.

Main fields:

- Name
- Description
- Level
- Martial Art

Each curriculum item belongs to one martial art through a `ForeignKey` relationship.

Available levels are:

- Beginner
- Intermediate
- Advanced

### Event

Stores information about martial arts events.

Main fields:

- Title
- Event Type
- Description
- Date
- Location
- Special Guest
- Martial Arts

An event can contain multiple martial arts through a `ManyToManyField` relationship.

Available event types are:

- Seminar
- Competition
- Gala

## Relationships

The main database relationships are:

```text
MartialArt 1 ----> many CurriculumItem

MartialArt many <----> many Event
```

## Forms and Validation

The project uses Django `ModelForm` forms for creating and editing data.

Examples of implemented validation and form customization include:

- Martial art names cannot contain numbers
- Martial art names must be unique
- Event dates cannot be in the past
- At least one martial art must be selected for an event
- The martial art name is disabled when editing an existing martial art
- Custom labels
- Help text
- Placeholders
- Custom error messages

## Database

The project uses SQLite.

The SQLite database file is not included in the repository.

A new database can be created automatically by running the Django migrations.

No pre-populated data, fixtures, or custom initialization scripts are required.

All necessary objects can be created directly through the website.

## Installation

1. Clone or download the repository.

2. Create and activate a Python virtual environment.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply the migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the application in a browser:

```text
http://127.0.0.1:8000/
```

## Using the Application

The application can start with an empty database.

All required project objects can be created directly through the website without using the Django admin panel or modifying the database manually.

A recommended order for creating data is:

1. Create one or more Martial Arts.
2. Create Curriculum Items and assign them to a Martial Art.
3. Create Events and select the participating Martial Arts.

## Main Navigation

The main navigation provides access to:

- Home
- Martial Arts
- Curriculum
- Events

The navigation and footer are implemented as reusable template partials and included in the shared base template.

## Martial Arts

The Martial Arts section supports full CRUD functionality:

- Create
- List
- Detail
- Edit
- Delete

The application contains static images for:

- Wing Tsun
- Karate
- Tai Chi

A custom Django template filter selects the appropriate image based on the martial art name.

If another martial art is created, a default image is used.

## Curriculum

The Curriculum section supports:

- Create
- List
- Detail

Each curriculum item is connected to a martial art and has a training level.

## Events

The Events section supports full CRUD functionality:

- Create
- List
- Detail
- Edit
- Delete

Events can be filtered by event type:

- Seminar
- Competition
- Gala

Events are displayed in date order.

Each event can be connected to one or more martial arts.

## Templates

The project uses Django template inheritance through:

```text
templates/base.html
```

Reusable partial templates are stored in:

```text
templates/common/
```

and include:

```text
header.html
footer.html
```

They are included in the base template using Django's `{% include %}` template tag.

## Custom 404 Page

The project contains a custom:

```text
templates/404.html
```

page for invalid URLs.

The custom page uses the same base template, navigation, styling, and footer as the rest of the application.

## Example Data

The following data can be used to test the application.

### Martial Arts

#### Wing Tsun

```text
Name: Wing Tsun
Description: A Chinese martial art focused on close-range combat, efficiency, structure, and sensitivity.
```

#### Karate

```text
Name: Karate
Description: A martial art focused on striking techniques, discipline, forms, and controlled movement.
```

#### Tai Chi

```text
Name: Tai Chi
Description: A Chinese martial art focused on controlled movement, balance, structure, and relaxation.
```

### Curriculum Items

#### Wing Tsun

```text
Siu Nim Tao - Beginner
Chum Kiu - Intermediate
Biu Tze - Advanced
```

#### Karate

```text
Heian Shodan - Beginner
Tekki Shodan - Intermediate
Bassai Dai - Advanced
```

#### Tai Chi

```text
8 Form - Beginner
24 Form - Intermediate
42 Form - Advanced
```

### Events

Example events include:

```text
Chi Sao Seminar
Type: Seminar
Special Guest: Samuel Kwok
Martial Art: Wing Tsun
```

```text
Martial Arts Gala
Type: Gala
Martial Arts: Wing Tsun, Karate, Tai Chi
```

```text
Martial Arts Tournament
Type: Competition
Martial Arts: Wing Tsun, Karate, Tai Chi
```

## Project Structure

The main project structure is:

```text
martial_arts_academy/
│
├── curriculum/
├── events/
├── martial_arts/
├── martial_arts_academy/
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── common/
│   │   ├── footer.html
│   │   └── header.html
│   ├── curriculum/
│   ├── events/
│   ├── martial_arts/
│   ├── 404.html
│   ├── base.html
│   └── home.html
│
├── manage.py
├── requirements.txt
└── README.md
```