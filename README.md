# Project 1 - Movie Trailer Website
### Udacity - Full Stack - Project 1 - Item Catalog

By Jerry Wardlow for the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### About

This project is a collection of python modules which generate an HTML document
that displays information about a list of movies and allows the user to view
the YouTube trailer of each movie. Each movie is stored as an object of the
class `Movie` as defined in `media.py`. `jerrys_movies.py` creates a new
instance of `Movie` for each movie and saves information to a local variable
named after the title of the movie. By importing and calling
`fresh_tomatoes.open_movies_page` on a list of all our movie objects, we can
generate and open an HTML page which neatly formats the stored information and
let's us view the YouTube trailer.

### Using This Project

**Prerequisites**

* Python 2.7.x
* The files contained in this repository

**Running and Testing This Project**

From a command line, change into the `p3catalog` directory of this project. (For
this example, we will assume it is in `/home/user/p1movietrailerwebsite`)

`cd /home/user/p1movietrailerwebsite`

From this directory we can run `jerrys_movies.py` and generate our HTML.

`python jerrys_movies.py`

This will generate our HTML and automatically open a browser window to display
the content.
