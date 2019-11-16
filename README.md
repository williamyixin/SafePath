# SafePath


SafePath is a novel, general purpose approach to detecting safe paths using topographic modeling and Google Cloud API.
Using Python, Google Cloud Elevation API, and Tkinter/Pillow.
(NOTE: For Tkinter/Pillow, use "pip install Pillow" to install required libraries)

We’ve all had our troubles finding SafePaths. 

“From playing golf after the sun going down, not being able to see“ - Connor Lien

“To spending countless hours at my mother’s hospital, escorting the elderly using wheelchairs, “ - William Zhang

“To getting lost in Yosemite” - Matthew Park

Throughout all of our lives, we’ve encountered difficulties wondering which way to go. Which is what inspired us to create SafePath, a topographical map simulator that utilizes graph theory searching algorithms and pairs it with elevation data from the Google Cloud API.  

We had at first decided to utilize our knowledge of graph theory and graph traversal to build a topographical map simulator that detected the most efficient possible path across some random, self generated terrain. Upon completing that in a relatively short amount of time, we had decided to attempt to manually find elevation data through researching geological databases. However, extrapolating that data proved to be difficult. The United States Geological Survey’s various tools were buggy and difficult to work with. It was virtually impossible to extract large data sets without having to manually download the data from the site and read from the provided Excel sheet. 

It was then we discovered the Google Elevation API, which allowed us to gather the elevation of any coordinate point on the Earth by simply sending a request with a coordinate. Using this, we were able to gather thousands of data points, and users could use our data with any point on the Earth instead of having to use our randomly generated topography. 

We had already determined that we would use pathfinding algorithms such as Bellman-Ford’s algorithm and Dijkstra’s algorithm to determine the fastest path; but all that was left was to decide the “weight” of each edge, or how hard it would be to traverse from one edge to another. To determine this weight, I plotted caloric loss versus the gradient of a slope, as caloric loss is the physical measure of how much energy it takes to travel from point A to B. Furthermore, we amplified our “risk factor” when going on steep slopes downwards, as it is often just as dangerous to go up a 60 degree slope as it is to go down a 60 degree slope. Using the equations we got from analyzing these factors, we could then determine the weight of these edges and easily determine the safest and most efficient path to travel given two arbitrary points anywhere on earth. After syncing the coordinate points with google maps images, we had our working product.

And yet, despite having overcome multiple points of adversity, we still believe we can improve on our application in the future. Data collection was sometimes slow, especially with the limitations of Google APIKeys. The program could use greater abstraction to apply it to solve multiple real-life problems. Through the creation of SafePaths, we not only created a program that has benefits in the consumer industry, but also tested a concept that we had been interested in for some time.

Run Commands
py gui.py assets/topography_data/topography_testing_halfdome.txt 60 30 assets/images/HalfDomeCropped.png

py gui.py assets/topography_data/topography_testing_golf.txt 60 30 assets/images/GolfCropped.png

py gui.py assets/topography_data/topography_testing_bigc.txt 60 30 assets/images/BigCCropped.png

py gui.py assets/topography_data/topography_testing_hawaii.txt 60 30 assets/images/HawaiiCropped.png
