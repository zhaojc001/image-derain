test（python3.6 windows和linux均支持）

python3 run_derain.py --weights_path model/model_medium/derain_gan_2019-03-08-15-09-01.ckpt-200000 --image_path input/14.jpg

--output_path  result.png

参数说明
--weights_path ：权重文件路径，本例存放了三种场景的权重文件，根据实际情况选择使用，详见下面的文件说明。
--image_path： 待测试图像路径。
--output_path :结果输出路径
文件说明
model文件夹下有三个文件夹，model_medium ， model_lens， model_heavy ，依次为场景中雨，镜头雨滴，场景大雨模型存放位置。




