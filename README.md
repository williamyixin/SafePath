# CalHacksTopographyGraphTraversal

SafePath

A novel, general purpose approach to detecting safe paths using topographic modeling and Google Cloud API.
Using Python, Google Cloud Elevation API, and Tkinter/Pillow.
(NOTE: For Tkinter/Pillow, use "pip install Pillow" to install required libraries)

We’ve all had our troubles finding SafePaths. 

“From playing golf after the sun going down, not being able to see“ - Connor Lien

“To spending countless hours at my mother’s hospital, escorting the elderly using wheelchairs, “ - William Zhang

“To getting lost in Yosemite” - Matthew Park

Throughout all of our lives, we’ve encountered difficulties wondering which way to go. Which is what inspired us to create SafePaths, a topographical map simulator that utilizes graph theory searching algorithms and pair it with elevation data from the Google Cloud API. But building such a program was no easy feat. We had to embody the definition of a full-stack development team, from using the server side keys to fetch the data, to finding the path of least resistance, and to render it in a comprehensible manner on the display.
There were many challenges along the way, from pairing the elevation and image coordinates, to finding a difficulty function for traversing a given gradient, to event handling for the user interface. But while each of these challenges posed an initial barrier (no pun intended), we persevered.

For pairing the elevation and image coordinates, we created a program to calculate the difference in longitude difference across different latitudes, and then used that to automate data fetching.

For finding a difficulty function to traverse a given gradient, we had to explore options other than those found in our physics based backgrounds. This included chemistry and biology, because it enabled us to not only find out the forces necessary to traverse across a given node, but how difficult a task would be for a typical human.

And finally, to properly implement event-handling, we used multi-threading to allow the graph traversing algorithm to not hinder the main GUI looping thread. This also created the issue of multiple threads accessing a variable at the same time. This was solved by using a boolean lock to regulate the accessing of the graph variables. 

And yet, despite having overcome multiple points of adversity, we still believe we can improve on our application in the future. Data collection was sometimes slow, especially with the limitations of Google APIKeys, and the program could use greater abstraction to apply it to solve multiple real-life problems. Through the creation of SafePaths, we not only created a program that has benefits in the consumer industry, but also tested a concept that we had been interested in for some time.

Run Commands
py gui.py assets/topography_data/topography_testing_halfdome.txt 60 30 assets/images/HalfDomeCropped.png

py gui.py assets/topography_data/topography_testing_golf.txt 60 30 assets/images/GolfCropped.png

py gui.py assets/topography_data/topography_testing_bigc.txt 60 30 assets/images/BigCCropped.png

py gui.py assets/topography_data/topography_testing_hawaii.txt 60 30 assets/images/HawaiiCropped.png
