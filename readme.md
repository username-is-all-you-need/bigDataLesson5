首先创建环境并拉取ultralytics ,使用 git clone ... 或通过手动下载安装
       （pytorch（训练）、cuda（模型导出）   cd ultralytics(你的安装路径）      在通过pip install -e 参数实现原项目的可编辑安装
以及其他依赖（）
特别的要单独拉取labelimg来标注数据（非python8环境会出现qt依赖无法正确打开，而需要单独创建环境，本项目就是如此，在./labeling当中）

然后数据准备，使用My_cut_out.py将视频切分为单张图片，使用命令行labeimg .\images\train .\classes.txt\用指定的类别去给目标画框

模型训练，将训练集与验证集按照特定方式组织，编写yaml配置文件后使用命令行yolo task=detect mode=train model=./yolov8n.pt data=“yolo_bvn.yaml” workers=1 epochs=50 batch=16 
       或脚本此项目为（test.py中未被注释代码）训练模型 
训练完成后会在runs/""/weights/中生成best.pt，就是我们训练出来的自己的模型，使用命令行yolo detect predict model=runs/detect/train/weights/best.pt source=./BVN.mp4 show=True
验证模型

注意：划分类别txt文件与项目训练的yaml文件有模板，需要自己根据实际编写。