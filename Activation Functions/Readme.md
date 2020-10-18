# Activation Function

Activation functions helps to determine the output of a neural network. These type of functions are attached to each neuron in the network, and determines whether it should be activated or not, based on whether each neuron’s input is relevant for the model’s prediction. 

> Activation function also helps to normalize the output of each neuron to a range between 1 and 0 or between -1 and 1.



![alt text](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/1.jpg?raw=true)

In a neural network, inputs are fed into the neurons in the input layer. Each neuron has a weight, and multiplying the input number with the weight gives the output of the neuron, which is transferred to the next layer.

The activation function is a mathematical “gate” in between the input feeding the current neuron and its output going to the next layer. It can be as simple as a step function that turns the neuron output on and off, depending on a rule or threshold.


> Neural networks use non-linear activation functions, which can help the network learn complex data, compute and learn almost any function representing a question, and provide accurate predictions.

## Commonly used activation functions

### **1.   Sigmod function**



The function formula and chart are as follows

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/sig.svg)

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/2.png)

The Sigmoid function is the most frequently used activation function in the beginning of deep learning. It is a smoothing function that is easy to derive.

In the sigmoid function, we can see that its output is in the open interval (0,1). We can think of probability, but in the strict sense, don't treat it as probability. The sigmoid function was once more popular. It can be thought of as the firing rate of a neuron. In the middle where the slope is relatively large, it is the sensitive area of the neuron. On the sides where the slope is very gentle, it is the neuron's inhibitory area.

The function itself has certain defects.

1) When the input is slightly away from the coordinate origin, the gradient of the function becomes very small, almost zero. In the process of neural network backpropagation, we all use the chain rule of differential to calculate the differential of each weight w. When the backpropagation passes through the sigmod function, the differential on this chain is very small. Moreover, it may pass through many sigmod functions, which will eventually cause the weight w to have little effect on the loss function, which is not conducive to the optimization of the weight. This The problem is called gradient saturation or gradient dispersion.

2) The function output is not centered on 0, which will reduce the efficiency of weight update.

3) The sigmod function performs exponential operations, which is slower for computers.


Advantages of Sigmoid Function : -

1. Smooth gradient, preventing “jumps” in output values.
2. Output values bound between 0 and 1, normalizing the output of each neuron.
3. Clear predictions, i.e very close to 1 or 0.


Sigmoid has three major disadvantages:
* Prone to gradient vanishing
* Function output is not zero-centered
* Power operations are relatively time consuming


### **2.  tanh function**

The tanh function formula and curve are as follows

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/tan.svg)
![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/3.png)

Tanh is a hyperbolic tangent function. The curves of tanh function and sigmod function are relatively similar. Let ’s compare them. First of all, when the input is large or small, the output is almost smooth and the gradient is small, which is not conducive to weight update. The difference is the output interval. 

The output interval of tanh is 1), and the whole function is 0-centric, which is better than sigmod.

In general binary classification problems, the tanh function is used for the hidden layer and the sigmod function is used for the output layer. However, these are not static, and the specific activation function to be used must be analyzed according to the specific problem, or it depends on debugging.

### **3.  ReLU function**

ReLU function formula and curve are as follows

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/relu.png)
![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/relu.svg)

The ReLU function is actually a function that takes the maximum value. Note that this is not fully interval-derivable, but we can take sub-gradient, as shown in the figure above. Although ReLU is simple, it is an important achievement in recent years.

The ReLU (Rectified Linear Unit) function is an activation function that is currently more popular. Compared with the sigmod function and the tanh function, it has the following advantages:

1) When the input is positive, there is no gradient saturation problem.

2) The calculation speed is much faster. The ReLU function has only a linear relationship. Whether it is forward or backward, it is much faster than sigmod and tanh. (Sigmod and tanh need to calculate the exponent, which will be slower.)

Ofcourse, there are disadvantages:

1) When the input is negative, ReLU is completely inactive, which means that once a negative number is entered, ReLU will die. In this way, in the forward propagation process, it is not a problem. Some areas are sensitive and some are insensitive. But in the backpropagation process, if you enter a negative number, the gradient will be completely zero, which has the same problem as the sigmod function and tanh function.

2) We find that the output of the ReLU function is either 0 or a positive number, which means that the ReLU function is not a 0-centric function.

### 4. Leaky ReLU function

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/lrelu.png)
![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/lrelu.svg)

In order to solve the Dead ReLU Problem, people proposed to set the first half of ReLU 0.01x instead of 0. Another intuitive idea is a parameter-based method, Parametric ReLU : f(x)= max(alpha x,x), which alpha can be learned from back propagation. In theory, Leaky ReLU has all the advantages of ReLU, plus there will be no problems with Dead ReLU, but in actual operation, it has not been fully proved that Leaky ReLU is always better than ReLU.

### 5. ELU (Exponential Linear Units) function

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/elu.jpg)
![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/elu.svg)

ELU is also proposed to solve the problems of ReLU. Obviously, ELU has all the advantages of ReLU, and:

* No Dead ReLU issues
* The mean of the output is close to 0, zero-centered

One small problem is that it is slightly more computationally intensive. Similar to Leaky ReLU, although theoretically better than ReLU, there is currently no good evidence in practice that ELU is always better than ReLU.

### 6.  Softmax

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/soft.png)


for an arbitrary real vector of length K, Softmax can compress it into a real vector of length K with a value in the range (0, 1), and the sum of the elements in the vector is 1. 

It also has many applications in Multiclass Classification and neural networks. Softmax is different from the normal max function: the max function only outputs the largest value, and Softmax ensures that smaller values have a smaller probability and will not be discarded directly. It is a "max" that is "soft".

The denominator of the Softmax function combines all factors of the original output value, which means that the different probabilities obtained by the Softmax function are related to each other.
In the case of binary classification, for Sigmoid, there are:

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/soft1.png)

For Softmax with K = 2, there are:

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/soft2.png)


Among them: It

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/soft4.png)


    


### 7.  PRelu (Parametric ReLU)

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/Capture.PNG)

PReLU is also an improved version of ReLU. In the negative region, PReLU has a small slope, which can also avoid the problem of ReLU death. Compared to ELU, PReLU is a linear operation in the negative region. Although the slope is small, it does not tend to 0, which is a certain advantage.



We look at the formula of PReLU. The parameter α is generally a number between 0 and 1, and it is generally relatively small, such as a few zeros. When α = 0.01, we call PReLU as Leaky Relu , it is regarded as a special case PReLU it.

Above, yᵢ is any input on the ith channel and aᵢ is the negative slope which is a learnable parameter.
* if aᵢ=0, f becomes ReLU
* if aᵢ>0, f becomes leaky ReLU
* if aᵢ is a learnable parameter, f becomes PReLU

### 8. Swish (A Self-Gated) Function

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/swish.png)

The formula is: **y = x * sigmoid (x)**

Swish's design was inspired by the use of sigmoid functions for gating in LSTMs and highway networks. We use the same value for gating to simplify the gating mechanism, which is called **self-gating**. 

The advantage of self-gating is that it only requires a simple scalar input, while normal gating requires multiple scalar inputs. This feature enables self-gated activation functions such as Swish to easily replace activation functions that take a single scalar as input (such as ReLU) without changing the hidden capacity or number of parameters.

1) Unboundedness (unboundedness) is helpful to prevent gradient from gradually approaching 0 during slow training, causing saturation. At the same time, being bounded has advantages, because bounded active functions can have strong reguairzation, and larger negative inputs will be resolved.

2) At the same time, smoothness also plays an important role in optimization and generalization.



### 9.  Maxout

The Maxout activation function is defined as follows

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/max.jpeg)

One relatively popular choice is the Maxout neuron (introduced recently by Goodfellow et al.) that generalizes the ReLU and its leaky version. Notice that both ReLU and Leaky ReLU are a special case of this form (for example, for ReLU we have w1,b1 =0).The Maxout neuron therefore enjoys all the benefits of a ReLU unit (linear regime of operation, no saturation) and does not have its drawbacks

The Maxout activation is a generalization of the ReLU and the leaky ReLU functions. It is a learnable activation function.

Maxout can be seen as adding a layer of activation function to the deep learning network, which contains a parameter k. Compared with ReLU, sigmoid, etc., this layer is special in that it adds k neurons and then outputs the largest activation value. value.


### 10.  Softplus

![alt](https://github.com/bhanuteja2001/ML_Knowledge/blob/master/Activation%20Functions/softplus.png)

The softplus function is similar to the ReLU function, but it is relatively smooth.It is unilateral suppression like ReLU.It has a wide acceptance range (0, + inf).

Softplus function: **f(x) = ln(1+exp x)**



## **------------------------------------------------------NOTE--------------------------------------------------------------**

## **Generally speaking, these activation functions have their own advantages and disadvantages. There is no statement that indicates which ones are not working, and which activation functions are good. All the good and bad must be obtained by experiments.**

### Reference : Ineuron Material
