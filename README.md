# Apple Distribution Script
This Python script simulates the process of fulfilling an order for apples with constraints. The goal is to package up to <b>1000 apples</b> while ensuring that the <b>total weight</b> does not exceed <b>300 units</b>.

### Code Summary
1. <b>Apple Class</b>:
    * The `Apple` class contains class variables `total_apples` and `total_weight`, which track the cumulative number of apples and their total weight.
    * Each apple is initialized with a random weight.
2. <b>Order Fulfillment</b>:
    * The script runs a `while` loop where new apples are added as long as the total apple count is less than 1000 and the total weight doesn’t exceed 300.
    * The weight of each new apple is checked before it is added. If adding the apple exceeds the weight limit, the loop breaks.
3. <b>Output</b>:
    * The script outputs the final count of apples packed and their total weight.

### Usage
1. Clone the repository:
    ``` sh
    git clone https://github.com/ysgorin/apple_distribution.git
    ```
2. Run the script:
    ``` sh
    python apples.py
    ```
3. Example output:
    ``` sh
    A shop owner has asked for 1000 apples, but the total weight cannot exceed 300 units.
    Fulfilling order...
    Number of Apples Packaged: 860
    Total Weight: 299.70
    ```
### Requirements
* Python 3.x

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.