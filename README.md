# Minesweeper

Minesweeper game in Django

## Usage

```python manage.py runserver```

Go to ```localhost:8000/game/```

## TODO

- Use HTML5 canvas for board

- Base URL redirect to /game/

- Front end presentation (HTML5, CSS3)

## Notes

Moved most of logic from views to models as seems to be the Django way. Implementations of reveal function on models is super ugly so far so it is staying in views for now.

Also, I don't like addValue in models.Board. However, Implementation in models.Tile requires getting from the db for every surrounding tile which costs more than is worth the semantic appeal.

Not sure how to testing on win or lose scenarios?

