import click
import json
import numpy as np


import tensorflow as tf
from tensorflow import keras
from keras import backend as k
from keras.utils import plot_model
from keras.applications.mobilenet_v2 import MobileNetV2


from tensorflow.python.profiler.model_analyzer import profile
from tensorflow.python.profiler.option_builder import ProfileOptionBuilder




@click.group()
def cli():
    """A command line tool for modifying pcaps"""
    pass



@cli.command('flop')
@click.argument('model_arch_file', type=str)
def calculate_flops(model_arch_file):
    """
    Calculate FLOPs for a given TensorFlow model.
    :param model: A compiled TensorFlow/Keras model.
    :return: Total FLOPs of the model.
    """
    # Create a session for profiling
    with open(model_arch_file) as f:
        model_arch = json.load(f)
    model = tf.keras.models.model_from_json(model_arch)
    # model = tf.keras.applications.MobileNetV2(weights=None, input_shape=(224, 224, 3))
    # # Plot model architecture
    # plot_model(model, 
    #         to_file='model_architecture.png',
    #         show_shapes=True,
    #         show_layer_names=True,
    #         rankdir='TB')
    # print("Model architecture plot saved as 'model_architecture.png'")
    # print(model.summary())
    
    # Handle multiple inputs
    input_specs = []
    for input_tensor in model.inputs:
        print(input_tensor.shape)
        input_specs.append(
            tf.TensorSpec([1] + list(input_tensor.shape[1:]), input_tensor.dtype)
        )
    
    print(input_specs)

    concrete_func = tf.function(lambda inputs: model(inputs))
    print(concrete_func, 1111)
    concrete_func = concrete_func.get_concrete_function(input_specs)
    print(concrete_func, 2222  )
    # Get graph definition
    graph = tf.compat.v1.get_default_graph()
    run_meta = tf.compat.v1.RunMetadata()
    opts = ProfileOptionBuilder.float_operation()
    flops = profile(graph, run_meta=run_meta, options=opts)
    
    print(f"Total FLOPs: {flops.total_float_ops} FLOPs")
    
    # Example: Define a sample model
    model = tf.keras.applications.MobileNetV2(weights=None, input_shape=(224, 224, 3))

    # Calculate FLOPs
    # flops = calculate_flops(model)
  
    
    # return flops.total_float_ops  # Returns total FLOPs

   

@cli.command('memory')
@click.argument('batch_size', type=int)
def get_model_memory_usage(batch_size):
    model_arch_file = "/home/mpaul/projects/entadev_mn/platform/files/testing/enta_v0.4.5/data/cnn_model.json"
    with open(model_arch_file) as f:
        model_arch = json.load(f)
    model = tf.keras.models.model_from_json(model_arch)

    print(model.summary())
    
    features_mem = 0
    float_bytes = 4.0
    for layer in model.layers:
        
        output_shape = layer.output_shape
        # print(layer.name, output_shape, type(output_shape))
        if type(output_shape) is list:
            output_shape = output_shape[0]
            # print(output_shape)
        elif type(output_shape) is tuple:
            output_shape = output_shape
            # print(output_shape)
            
        single_layer_mem = 1
        for s in output_shape:
            # print(s)
            if s is None:
                continue
            single_layer_mem *= s
        single_layer_mem_float = single_layer_mem * float_bytes
        single_layer_mem_MB = single_layer_mem_float / (1024 ** 2)
        print(f"Memory for {output_shape} layer in MB is ->: {single_layer_mem_MB}")
        features_mem += single_layer_mem_MB
        
    # Calcualte Parameters memory
    trainable_wts = np.sum([k.count_params(p) for p in model.trainable_weights])
    non_trainable_wts = np.sum([k.count_params(p) for p in model.non_trainable_weights])
    parameters_mem_Mb = ((trainable_wts + non_trainable_wts) * float_bytes) / (1024 ** 2)
    print("=======================================================")
    print(f"Memory for featrues in MB is ->: {features_mem * batch_size} MB")
    print(f"Memory for parameters in MB is ->: {parameters_mem_Mb} MB")
    
    total_memory_MB = (batch_size * features_mem) + parameters_mem_Mb
    total_memory_GB = total_memory_MB / 1024
    print("Minimum memory required for the model is ->: ", total_memory_GB, "GB")
    return total_memory_GB
    
# mem_for_my_model = get_model_memory_usage(16, model)
# print("====================================================")
# print("Minimum memory required for my model is: ", mem_for_my_model, "GB")

if __name__ == '__main__':
    cli()