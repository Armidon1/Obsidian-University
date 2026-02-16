You are absolutely right that changing the labels from **0 and 1** to **-1 and 1** seems like a small detail, but it signals a massive shift in **how** the machine learns.

The fundamental reason for introducing the Perceptron (and later Support Vector Machines or SVMs) is to move away from calculating **probabilities** and focus entirely on **geometry**.

Here is the breakdown of why this change is useful, using the concepts from your sources.

### 1. Probability vs. Geometry

- **The "Normal" Way (Logistic Regression):** As you learned in Week 4, models like Logistic Regression are obsessed with **probabilities**. They output a number between 0 and 1 (using the Sigmoid function) to tell you _how likely_ it is that a point belongs to a class. They try to minimize the "distance" between predicted probabilities and reality (KL Divergence).
- **The Perceptron Way:** The Perceptron doesn't care about probabilities (e.g., "there is a 92% chance this is a cat"). It only cares about the **geometry**: "Is this point on the correct side of the wall?".
    - We use **-1 and 1** because it simplifies the math for this geometric check.
    - If the label $y$ is -1 and your prediction (the sign of the dot product) is -1, multiplying them gives a **positive** number.
    - If the label is 1 and prediction is 1, the result is **positive**.
    - Therefore, the algorithm just wants $y \cdot x^T\theta > 0$. If this condition is met, the Perceptron is happy and does nothing.

### 2. "Lazy" Learning (Error-Driven)

This is a major efficiency difference.

- **Logistic Regression:** It is constantly adjusting its parameters ($ \theta $) based on **every single point** to maximize the likelihood, even if it is already classifying the point correctly.
- **Perceptron:** It is "lazy." It looks at a point; if the point is already on the correct side of the hyperplane, the Perceptron **does not update** the model at all. It only learns from its **mistakes** (or "margin errors").
    - This makes the calculation very fast, as it stops doing work once the points are separated.

### 3. The Concept of "Margin" (Safety)

The most important reason for this new approach is to introduce the concept of the **Margin**.

In "normal" classification, a decision boundary is "good" as long as it separates the classes. But geometrically, some boundaries are safer than others.

- **Logistic Regression** doesn't explicitly measure how far a point is from the line, only the probability.
- **Perceptron/SVM** introduces the idea that we don't just want to be _correct_; we want to be **safely correct**.
    - Your sources define a **margin error** not just when you are wrong, but when you are "barely" right (too close to the line).
    - This leads to **SVMs**, which look for the "simplest" solution that separates the data with the widest possible corridor (margin) between the classes.

### Summary Table

| Feature         | "Normal" (Logistic Regression)               | Perceptron / SVM                                                               |
| :-------------- | :------------------------------------------- | :----------------------------------------------------------------------------- |
| **Output**      | A Probability (0 to 1)                       | A Side of the line (-1 or 1)                                                   |
| **Goal**        | Model the data distribution                  | Find a separating Hyperplane                                                   |
| **Updates**     | Adjusts for every point                      | Adjusts only on **errors**                                                     |
| **Why use it?** | You need to know "how certain" the model is. | You want a **geometric guarantee** (Margin) that the classification is robust. |