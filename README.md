Data Structures & Algorithms 2: Task 1

A.  Identify a named self-adjusting algorithm (e.g., nearest neighbor algorithm, greedy algorithm) that could be used to create your program to deliver the packages.

    I’m going to use the nearest neighbors algorithm with a time complexity of O(n).

B.  Identify a self-adjusting data structure, such as a hash table, that could be used with the algorithm identified in part A to store the package data.
1.  Explain how your data structure accounts for the relationship between the data components you are storing.


    I will be using a hash table to store package data. This will allow me to store key value pairs for many things, whether it be truck to package, or package to destination.


C.  Write an overview of your program in which you do the following:
1.  Explain the algorithm’s logic using pseudocode.
Note: You may refer to the attached “Sample Core Algorithm Overview” to complete part C1.


    initialize Graph
    initialize Packages
    initialize Trucks

        While user input is begin
	        Deliver packages
	        Update locations and times

            Print package query yes or no
            While package query is yes
                User input variable which to query package
                Print query result


2.  Describe the programming environment you will use to create the Python application, including both the software and hardware you will use.


    I’m using PyCharm Community Edition 17.0.10+8-b1207.12 aarch64 on MacOS, on an M1 Macbook Pro.


3.  Evaluate the space-time complexity of each major segment of the program and the entire program using big-O notation.


    Done within code


4.  Explain the capability of your solution to scale and adapt to a growing number of packages.


	This solution scales well to a growing number of packages, being that the user only needs to manually load each truck to the number of packages necessary, and the program will do the rest of the work, and will calculate the route from there.


5.  Discuss why the software design would be efficient and easy to maintain.


    This software design is very efficient and easily maintained, due to the way that each intricate component of the program is its own page of code, each being called in the main function as necessary. The data is held in its own folder, easily replaced with a new day’s packages for automatically adapted routing.


6.  Describe both the strengths and weaknesses of the self-adjusting data structure (e.g., the hash table).


    Using a hashtable presents advantages such as fast lookup, offering constant-time retrieval of city information, and efficient memory usage through key-value pairs. This flexibility in implementation allows for tailored hashing functions and collision resolution strategies. However, hash collisions can degrade performance, requiring additional handling steps, potentially leading to inaccuracies or slower lookup times. Moreover, hashtables may consume more memory and incur hashing overhead, especially in large TSP instances, impacting overall performance. Additionally, the deterministic nature of hashtables may conflict with the randomized search techniques often employed in TSP algorithms. Therefore, while hashtables offer advantages in speed and memory efficiency, their use in TSP solutions requires careful consideration of these drawbacks and their implications on algorithm performance.


7.  Justify the choice of a key for efficient delivery management from the following components:


    Package ID is definitely my choice for a key in an efficient delivery management system.


D.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.


    Of course.


E.  Demonstrate professional communication in the content and presentation of your submission.

    Always!




TASK 2 --------

C.

1.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.

        ![C1.9am.png](data%2FScreenshots%2FC1.9am.png)


2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.

        ![C2.12pm.png](data%2FScreenshots%2FC2.12pm.png)


3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.

        ![C3.12.30pm.png](data%2FScreenshots%2FC3.12.30pm.png)

E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.
   
    ![e. total mileage by all trucks.png](data%2FScreenshots%2Fe.%20total%20mileage%20by%20all%20trucks.png)


F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:

1.  Describe two or more strengths of the algorithm used in the solution.

        The algorithm is very scalable, and can take in more or less packages. It is also lightweight and optimizes a path quickly

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.

        The algorithm indeed meets all requirements of the scenario.

3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.

        Dijkstra algorithm, A* search algorithm

a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.

    The Dijkstra and A* search algorithms both traverse the graph to find the shortest 
    distance between two vertices. The solution I used just uses the given distances 
    between all the vertices without any optimizations.

G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.

    If I did this again, I would find a way to load the trucks automatically. Here, I load them manually because it is easier, but to have
    them load manually would increase scalability and functionality. 

H.  Verify that the data structure used in the solution meets all requirements in the scenario.

    The hash table has an insert function and a lookup function, and they work correctly and without error.

1.  Identify two other data structures that could meet the same requirements in the scenario.


    Priority queue, linked list

a.  Describe how each data structure identified in H1 is different from the data structure used in the solution.

    A priority queue might help deliver the packages by putting a priority on the first packages needed to be delivered.
    A linked list could assign the packages in a non-priority order and deliver the packages until the list is emptied.