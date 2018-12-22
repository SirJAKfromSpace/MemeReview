# MemeReview
# Authors: Jawad Aziz Khan, Abir Rahman, Taufiqur Rahman

This contains code that can be used to visualize tens of thousands of images in a two-dimensional projection within which similar images are clustered together. The image analysis uses Tensorflow's Inception bindings, and the visualization layer uses a custom WebGL viewer.

When first running fresh, preprocessing is required.
The images and required thumbnails, vector and map data can be processed by running:
```
python run.py "memes/*.jpg"
```
Or a similar 3rd path argument

Image resizing utilities require ImageMagick compiled with jpg support. For Windows search for ImageMagick and download/install using the .exe

The html viewer requires a WebGL-enabled browser.
If you have a WebGL-enabled browser and a directory full of images to process, you can prepare the data for the viewer by installing the dependencies

For python 3.x, open the prompt from the project dir and run:
```
python -m http.server 5000
```
Once the web server starts, you should be able to see your results on `localhost:5000`.
Also make sure that there is a folder named exactly "output", in the root folder before starting.
