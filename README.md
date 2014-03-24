# Minesweeper

Minesweeper game in Django

## Usage

```python manage.py runserver```

Go to ```localhost:8000/game/```

## TODO

- View Testing (HTTP, game update tests)

- Use HTML5 canvas for board

- Base URL redirect to /game/

- Front end presentation (HTML5, CSS3)

## Notes

Moved most of logic from views to models as seems to be the Django way. Implementations of reveal function on models is super ugly so far