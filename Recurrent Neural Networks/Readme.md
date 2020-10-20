# Introduction 
A typical feed-forward neural network maps inputs to outputs with no consideration of previous computations or where the current input fits in relation to others. The network applies the same function to each input regardless of sequence. This is fine for many applications, but often the context of an input has some relevance to the target output. One way to address this problem is to use a recurrent neural network (RNN). An RNN is a network with ‘memory.’ The network maintains information about previous inputs allowing its current output to be generated with consideration about the past.
# Working 
An RNN cell takes an input vector at some time 𝑥(𝑡) and maps it to an output vector 𝑦̂(𝑡) while also considering something called the network hidden state ℎ(𝑡) which depends on the previous inputs to the network. At every time step the network computes the output vector while also computing the hidden state as a function of the input and previous hidden state, passing the computed hidden state as an input to the next RNN cell.
These RNN cells can be strung together to form multiple layers of cells and mixed with other NN structures such as feed-forward layers to form the final model.

# Code(PyTorch)
    class RNNCell(nn.Module):
      def __init__(self, inputSize, hiddenSize, outputSize):
        super(RNNCell, self).__init__()
        self.Wx = torch.randn(hiddenSize, inputSize) # input weights
        self.Wh = torch.randn(hiddenSize, hiddenSize) # hidden weights
        self.Wy = torch.randn(outputSize,recurhiddenSizerentSize) # output weights
        self.h = torch.zeros(hiddenSize,1) # initial hidden state
        self.bh = torch.zeros(hiddenSize,1) # hidden state bias
        self.by = torch.zeros(outputSize,1) # output bias
      def forward(self, x):
        self.h = torch.tanh(self.bh + torch.matmul(self.Wx, x) + torch.matmul(self.Wh,self.h))
        output = nn.Softmax(self.by + torch.matmul(self.Wy,self.h))
        return output, self.h
# Advantages
1. An RNN remembers each and every information through time. It is useful in time series prediction only because of the feature to remember previous inputs as well. This is called Long Short Term Memory.
2. Recurrent neural network are even used with convolutional layers to extend the effective pixel neighborhood.
# Disadvantages 
1. Gradient vanishing and exploding problems.
2. Training an RNN is a very difficult task. 
# References 
1. https://medium.com/dair-ai/building-rnns-is-fun-with-pytorch-and-google-colab-3903ea9a3a79
2. https://medium.com/analytics-vidhya/understanding-rnn-implementation-in-pytorch-eefdfdb4afdb
