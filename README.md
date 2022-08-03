# Dijkstra-s-Algorithm-on-a-Cost-Grid
Nodes and nonnegative edges are necessary for Dijkstra’s algorithm to build a reliable network. A standard grid can take a form of an unambiguous network. A cost grid also more accurately reflects the environments. Each board cell on a cost square grid with the dimensions max_val by max_val is assigned a value between 1 and max_cost. The line linking one vertex to the opposite end on the other side is said to be the shortest "route" if it has the lowest sum of cell values along the way. Obstacles cells are designated by inf to signify an endless journey to them in order to account for the barriers. These obstacles are produced at random, and obstacles_number indicates how many are present. Start and end locations are defined by the user and have no expenses. Note that, if max_cost = 2 then the cost grid reduces to a standard grid with uniform costs = 1.
 
Figure 1: Cost Grid

![image](https://user-images.githubusercontent.com/110555868/182700292-f5862488-c2c1-46f0-8f40-f4fc165c08f7.png)

Outcome
Standard Grid Omnidirectional Mobile Robot
If the robot can move in all directions without any constraints.

![image](https://user-images.githubusercontent.com/110555868/182700594-bafdff1b-e114-4990-824e-c1dd59363e6e.png)

 
Figure 2: Omnidirectional Mobile Robot Planned Path on a Standard Grid
Path cost: 17
Standard Grid Nondirectional Mobile Robot
If the robot can move only up, down, right, and left.

![image](https://user-images.githubusercontent.com/110555868/182700631-70bfd201-382a-4fd9-88c3-82b30785a8f2.png)

 
Figure 3: Nondirectional Mobile Robot Planned Path on a Standard Grid
Path cost: 34
Cost Grid Omnidirectional Mobile Robot

![image](https://user-images.githubusercontent.com/110555868/182700694-53da7b7e-503d-47c9-9d7f-26196f8cf414.png)

 
Figure 4: Omnidirectional Mobile Robot Planned Path on a Cost Grid
Path cost: 219
Cost Grid Nondirectional Mobile Robot

![image](https://user-images.githubusercontent.com/110555868/182700732-e76c3c59-07bd-473d-aaec-0fb15ba7baf4.png)

 
Figure 5: Nondirectional Mobile Robot Planned Path on a Cost Grid
Path cost: 442
The waypoints found by Dijkstra’s algorithm can now be employed by the trajectory generator since the results are reliable.


