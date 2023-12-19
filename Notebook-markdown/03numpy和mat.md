# numpy和mat对象

## numpy简介
和图像运算有关

- opencv中用到的矩阵都要转换成numpy数组
- numpy是一个经过高度优化的Python数值库

## numpy基本操作

- 创建矩阵
  - 创建数组array()，
    - 一维数组， `a=np.array([2,3,4])`
    - 二维数组， `c=np.array([[1.0,2.0],[3.0,4.0]])`
  - 创建全0数组 zeros/ones 函数
    - `c=np.zeros((480,640,3),np.uint8))`,(480,640,3)表示行数（高度），列数（宽度），通道数/层数;np.uint8表示矩阵中的数据类型，
  - 创建全值数组 full(), `c=np.full((480,640,3),255,np.uint8)` ,255表示每个元素的值
  - 创建单元数组 identity/eye()  ，单元数组，斜角为1,两侧为0
- 检索与赋值[y,x]
  - [y,x]，坐标，索引从0开始，
  - [y,x,channel]，多通道，
- 获取子数组[:,:]，ROI,Region of Image,获取图像中的一部分，
  - 方式：[y1:y2,x1:x2]，
  - 整个图像：[:,:]