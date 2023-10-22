## Evaluation of Bond-Systems Efficiency

### Introduction

This repository contains the code and resources for evaluating the efficiency of bond-systems. Bond-systems are mechanisms that require potential attackers to risk their capital when attempting to compromise an oracle that employs such a system. The experiment is designed to assess the effectiveness of bond-systems in deterring malicious actors by making attacks financially unfeasible.

### Background

The bond-system under examination is modeled after the oracle system used by Tellor. In this system:

- Elected data can be disputed by paying a fee.
- Disputed data undergoes a consensus process where participants vote on its validity.
- The fee for disputing data increases progressively, deterring repeated false disputes.
- Participants deposit a cryptocurrency as a bond to gain voting rights in the consensus process.
- Each consensus process lasts 48 hours, after which votes are tallied to determine the outcome.

Real-world parameters are used to model costs associated with participating in the consensus process. For instance, the bond price is based on the value of Tellor's TRB token, which has fluctuated between $0.88 and $146.14. The current price used for the experiment is $10.87, requiring a bond of 138 tokens.

### Experiment Details

The code models the costs associated with manipulating the consensus process. As shown in the provided table, these costs can be substantial, especially when considering the potential price inflation due to rapid token purchases. The model assumes a constant liquidity of $90,367 but increases the token price by 2% after each purchase, simulating the diminishing returns of buying large quantities of tokens in a short timeframe.

### Code Overview

The code in `model.ipynb` is structured as follows:

- **testcalc**: This function calculates the total cost based on an initial token price and a required token amount. It simulates the process of purchasing tokens, considering the available liquidity and the increasing token price.

- **calc**: A helper function that computes the costs for a range of token prices and amounts.

- **graph**: Generates a 3D plot visualizing the relationship between token price, token amount, and the total cost.

- **arraytesting**: A utility function for testing array operations.

- **averagepricegraph**: Plots the average token price against the amount of tokens purchased. This visualization helps in understanding how the average price per token changes as more tokens are purchased.

### Results and Implications

The results indicate that bond-systems can be an effective deterrent against malicious attacks. By requiring attackers to invest significant capital, many potential threats may be priced out of attempting an attack. Furthermore, even well-funded attackers might be dissuaded by the financial risks involved. The experiment also underscores the importance of setting a minimum bond value and ensuring active participation from honest actors.
