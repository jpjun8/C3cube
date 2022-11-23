### 1. The kernel used for a convolution operation
- lays partially outside of the image when the center is within k pixels of any edge, when the kernel has $2 * k + 1$ rows or columns and no padding was used
- ~~is an array whose values keep constant while training a NN convolutional layer~~
- ~~is slid through the pixels in the input image by taking always strides of the same length of the kernle so that there is no overlap between~~
- can be learned in a NN convolutional layer
- ~~is an array that has to be of the same size than the input image~~
- is an array that encodes a pattern to be identified in the input image

### 2. When convolutions are taken in strides of length $s > 1$
- ~~the size of the output in each dimension is about the size of the input in each diemnsion multiplied by $s$~~
- ~~$s$ is always the same as the number of pixels in the convolutional kernel~~
- $s$ is the number of steps taken in each dimension to move the conolutional kernel to compute the next convolution value
- the size of the output in each dimension is about the size of the input in each dimension divided by $s$

### 3. A feature map with $x_f \times y_f$ pixels and $L$ layers taken from images with $x_i \times y_i$ pixels and D channels
- Holds the response to a collection of $L$ patterns, or features, in the image and is computed through convolution
- can be computed using $L$ kernels represented as tensros of size $k_i \times k_j \times D$
- ~~has always the same number of layers as the number of channels in the input~~
- encodes pattern activation in locations in the iamge
- ~~Holds the response to a collection of $D$ patterns, or features, in the image and is computed through convolution~~

### 4. A convolutional layer
- outputs a feature map that encodes in each slice the activation patterns encoded in the kernels whose parameters are learned
- ~~has to be connected to a pooling layer always~~
- ~~is trained to optimize the number of kernels to use~~
- implements the convolution operation through units whose weights are kernel values
- can be setup with parameters that include the number of kernesl, the number of channles, the stride length and the padding strategy used
- shares the kernel weights among the convolutional units associated to the same slice on the output feature map
- is trained to learn kernel weights and biases for its units
- ~~shares no kernel weights among the convolutional units associated to the same slice on the output feature~~

### 5. Convolution
- results in a large positive value when the pixels in the image match the corresponding pixels in the kernel
- ~~operates on an input image which is a 2D array and a kernel which is a 3D array~~
- operates using an input image and a kernel which are both arrays with the same number of dimensions
- is a commutative operation
- ~~is valid for every pixel in an input image regardless of the size of the kernel used~~
- ~~is not commutative~~
- can be computed for RGB images through a 3D version where each of the color intensities is encoded as a channel

### 5-1. Convolution
- can only be computed for images in levels of grey
- ~~cannot be computed as a dot product~~
- **for a given output $u, v$ computes a weighted sum of the pixel values in an image that overlap a kernel centered at $u, v$ that holds the weights**
- ~~is a non-linear operation~~
- **is a linear operation**
- is invalid for some pixels in an input image for when the kernel has more than one row or more than one column

### 6. Padding
- ~~shrinks the output image to ignore pixels where the convolution is invalid~~
- ~~summarizes the pixels that align with the kernels by computing their maximum or their average~~
- allows to compute the convolution for every pixel in an input image
- expands the input image by $k$ pixels on each of the four sides for the computation of the convolution for kernels with $2k + 1$ rows and columns

### 7. Image classification through Deep Neural Networks
- may involve a flattening fully connected layer close to the output
- is achieved by identification of patterns at increasing levels of complexity that account for larger patches in the input
- ~~can get the final classification by connecting a softmax output to each pixel in its output feature map~~
- ~~require to use ReLU functions in their non-linear units~~
- ~~can get the final classification directly at the output of a Convolutional Layer without any flattening layer~~
- can be achieved through a stack that includes convolutional, ReLU, fully-connected, and softmax layers