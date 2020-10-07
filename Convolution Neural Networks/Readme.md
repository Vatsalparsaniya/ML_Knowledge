# CNN Introduction

A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.

## Where can we use CNNs ? 
CNNs can be used for image classification purposes.

## Working 
1. The image is resized to an optimal size and is fed as input to the convolutional layer.<br>
2. There exists a filter or neuron or kernel which lays over some of the pixels of the input image depending on the dimensions of the Kernel size.<br>
3. The Kernel actually slides over the input image, thus it is multiplying the values in the filter with the original pixel values of the image (aka computing element-wise multiplications).
4. Pooling layer is used which generally decreases the dimensions of the images but not the image channels.<br>
5. Finally, an activation function generally ReLU is applied on it.<br>

## Advantages and Disadvantages
### Advantages
Some of the advantages of a CNN over an MLP for images are that they are more location invariant due to the convolution meaning only a small portion of the image is paid attention to at a time and max pooling also helps with this. Also, CNN’s mean that you don’t need a ridiculous number of neurons which would take forever to train. Also, they are based off how the human brain’s image processing works and copying nature is normally good.

### Disadvantages
CNN do not encode the position and orientation of object. Lack of ability to be spatially invariant to the input data. A ConvNet requires a large Dataset to process and train the neural network. If the CNN has several layers then the training process takes a lot of time if the computer doesn’t consist of a good GPU.

## Reference 
1. https://machinelearningmastery.com/convolutional-layers-for-deep-learning-neural-networks/ <br>
2. https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/
