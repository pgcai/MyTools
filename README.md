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

#### dirTool

- get_file(file_path, file_end)
- get_numfile(file_path, file_end)
- get_file_sub(file_path, filelist, file_end)
- get_numfile_sub(file_path, imagelist, file_end)
- new_folder(dirpath)



#### txtTool

- check_dir(file_path)
- txtRead(file_path)
- txtReadArray(file_path, tList)
- txtReadNumArray(file_path, tList)
- txt_read_2dim(file_path, tList)
- txt_read_2dim_num(file_path, tList)
- txtWrite(file_path, str)
- txtAddWrite(file_path, str)
- txtWriteArray(file_path, tList)
- txtAddWriteArray(file_path, tList)
- txtAddtxt(path1, path2)
- txt_write_2d_array(file_path, tList=[[]])



#### dateTool

- getDateYMDHMSU()
- getDateYMD()
- getDateYMDHMS()



#### exlTool

- read_csv(file_path)
- read_excel(file_path)



#### listTool

- get_iwant_col_y(alist, colname)
- get_iwant_col_x(alist, colname)
- npy_plus_npy(npypath, tofilepath)
- get_all_npy(npypath)



#### videoTool

- video2img(videoPath, savePath, timeF, file_end)
- img2video(savePath, videoPath, fps, file_end)



#### mathTool

- sigmoid(x)
- tanh(x)
- relu(x)
- prelu(x, a=0.25)
- 



- - - 更多精彩等你探索。



### A more detailed

#### dirTool_

- ``` python
    get_file(file_path, file_end=('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff'))# 获取指定文件夹下指定后缀文件/不包含子文件夹
    # (文件夹路径, 后缀名)
    
  ```

- ``` python
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
