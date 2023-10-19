yolox model convert to rknn model, including the preprocess and post-process
step 1:
	prepare your quantization dataset
	run quant_data_prepare.py script
	this will produce dataset.txt which indicate the path of your quantization dataset
step 2:
	run rknn_convert.py
	this will produce rk_model/yolox.rknn and result.jpg
The file list is state as:
quant_data: quantization dataset path
onnx_data: yolox.pt-->yolox.onnx model path
rk_model: converted rknn model path
acc_eval.txt: accuracy evaluation image path
config.yaml: rknn convert config file