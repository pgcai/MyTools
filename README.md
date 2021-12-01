## PyTools-**包罗万象的python工具包。🔧**

```
 _________  ________  ________  ___       ________  ___    ___ 
|\___   ___\\   __  \|\   __  \|\  \     |\   __  \|\  \  /  /|
\|___ \  \_\ \  \|\  \ \  \|\  \ \  \    \ \  \|\  \ \  \/  / /
     \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \   ____\ \    / / 
      \ \  \ \ \  \\\  \ \  \\\  \ \  \____\ \  \___|\/  /  /  
       \ \__\ \ \_______\ \_______\ \_______\ \__\ __/  / /  
        \|__|  \|_______|\|_______|\|_______|\|__||\___/ /   
                                                  \|___|/    
```

### API参考手册

#### dirTool🗂️

```python
1. get_file(file_path, file_end=('.png', '.jpg', '.jpeg'))      获取指定文件夹下指定后缀文件/不包含子文件夹
2. get_numfile(file_path, file_end=('.png', '.jpg', '.jpeg'))   获取指定文件夹下指定后缀文件/不包含子文件夹//文件名需要为number/排序
3. get_file_sub(file_path, filelist=[], file_end=('.png', '.jpg'))      获取指定文件夹下指定后缀文件/包含子目录
4. get_numfile_sub(file_path, filelist=[], file_end=('.png', '.jpg'))   获取指定文件夹下指定后缀文件/包含子目录/文件名需要为number/排序
5. new_folder(dirpath)  根据当前时间新建文件夹
```



#### txtTool📄

```python
1. check_dir(file_path)     检查文件地址的合法性,不存在文件夹则新建
2. txtRead(file_path)       打开txt文件并返回全部内容
3. txtReadArray(file_path)  以列表形式返回txt中的内容 去掉回车‘\n’
4. txtReadNumArray(file_path, tList=[])     以列表形式返回txt中的内容 去掉回车‘\n’ 并将他们都转化为float类型
5. txt_read_2dim(file_path, tList=[])       以列表形式返回txt中的内容(有字符串)/并去掉回车‘\n’/每一行有多个属性
6. txt_read_2dim_num(file_path, tList=[])   以列表形式返回txt中的内容(纯数字，提前转换为浮点型)/并去掉回车‘\n’/每一行有多个属性
7. txtWrite(file_path, str) 对txt文件写入字符串 str
8. txtAddWrite(file_path, str)          对txt文件!!增添写入字符串 str
9. txtWriteArray(file_path, tList=[])   “新建”txt文件写入一个数组 "一个元素一行"
10. txtAddWriteArray(file_path, tList=[])   “对原有”txt文件写入一个数组 "一个元素一行"
11. txtAddtxt(path1, path2)     两个txt文件 拼接
12. txt_write_2d_array(file_path, tList=[[]])   “新建”txt文件写入一个2-dim列表/"多个属性一行"
```



#### dateTool⏰

```python
1. getDateYMDHMSU()     返回年月日|时分秒|毫秒
2. getDateYMD()         返回年月日
3. getDateYMDHMS()      返回年月日|时分秒
```



#### exlTool📊

```python
1. read_csv(file_path)  读取csv文件返回列表  
2. read_exl(file_path)  读取excel文件返回列表
3. write2exl(names, wlist, file_path)   将列表写入到excel
```



#### listTool🏁

```python
1. get_iwant_col_y(alist=[["!!!原列表为空"]], colname=[0])  返回你想要的列/一列一个列表
2. get_iwant_col_x(alist=[["!!!原列表为空"]], colname=[0])  返回你想要的列/一行一个列表
3. npy_plus_npy(npypath = [], tofilepath = '')  多个npy合并为一个npy文件/输入文件地址/纵向合并 (!文件太大会存不了)
4. get_all_npy(npypath = [])    根据路径读取多个npy文件,返回他们纵向合并的列表
```



#### videoTool📽️

```python
1. video2img(videoPath, savePath, timeF = 1, file_end='.jpg')   将视频分帧到指定文件夹
2. img2video(savePath, videoPath, fps = 30, file_end=('.jpg'))  将指定文件夹图片合成为视频
```



#### mathTool📐

```python
1. sigmoid(x)   sigmoid
2. tanh(x)      tanh
3. relu(x)      relu
4. prelu(x, a=0.25)     prelu
5. mean(nlist)  求数组均值
6. var(nlist)   求数组方差
7. std(nlist)   求数组标准差
7. normalization(nlist)     归一化
8. standardization(nlist)   标准化
9. sta_mean_std(nlist, mean, std)   指定 均值 标准差 标准化
10. euclidean_distance(a, b)        计算两向量的欧氏距离
11. vectorial_resultant(a, b)       计算ab两向量合向量
12. vector_angle(a, b)  计算点a指向点b的矢量 且各维度平方和为1
13. linear_equation_in_2unknowns(a, b, c)   解二元一次方程
14. arctan(theta)   输入正切值，返回角度值
15. arcsin(theta)   输入正弦值，返回角度值
16. arccos(theta)   输入余弦值，返回角度值
17. arc_sin_cos(sin_theta, cos_theta)   同时输入sin 与 cos 计算角度值
18. theta_angle(sin_theta, cos_theta, angle)    输入正弦余弦值，返回旋转angle角度后的正弦余弦值
19. vector_3d_angle(v1, v2)     求两个3-dim向量的夹角
```



#### imgTool🖼️

```python
1. get_img(getpath, gray=False, scale_percent=100) 根据路径返回img/灰度选择/缩放
2. save_img(savepath, img)      保存图片
3. plot_line_chart(y1, y2, y3)  画折线图 暂不完善 
4. cut_pic(img,pattern=0, up = 0, down = 0, left = 0, right = 0)    切割图片/比例切割/像素切割
5. plot_3d_line(x, z, y, over, x_max, y_max, z_max)     三维空间画线
6. plot_3d_dot(location, over, x_max, y_max, z_max)     三维空间中画点
```



#### spiderTool🕸️

```python
1. get_headers(url, use='pc')	随机生成设备头
```



### A more detailed

#### dirTool_

- ```python
    get_file(file_path, file_end=('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))# 获取指定文件夹下指定后缀文件/不包含子文件夹
    # (文件夹路径, 后缀名)
    
  ```
- ```python
  get_numfile(file_path, file_end=('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))
  # 获取指定文件夹下指定后缀文件/不包含子文件夹/数字文件排序
  # (文件夹路径, 后缀名)
  ```
- ```python
  get_file_sub(file_path, filelist=[], file_end=('.png', '.jpg'))
  # 获取指定文件夹下指定后缀文件/包含子目录
  ```
- ```python
  get_numfile_sub(file_path, imagelist=[], file_end=('.png', '.jpg'))
  # 获取指定文件夹下指定后缀文件/包含子目录/文件名为number排序
  ```
- ```python
  new_folder(dirpath)
  # 根据当前时间(年月日时分秒)新建文件夹
  ```



- - - 更多具体等闲了再写，你可以先去utils下的代码里看看
    - (For more details, you can go to the utils code first.)

