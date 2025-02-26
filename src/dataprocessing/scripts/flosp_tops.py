import tensorflow as tf
import numpy as np
import time
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2

def get_flops(model):
    """
    Calculate FLOPS for tensorflow model
    Args:
        model: tensorflow model instance
    Returns:
        flops: number of float operations
    """
    concrete = tf.function(lambda inputs: model(inputs))
    concrete_func = concrete.get_concrete_function(
        [tf.TensorSpec([1, *inputs.shape[1:]]) for inputs in model.inputs])
    frozen_func = convert_variables_to_constants_v2(concrete_func)
    with tf.Graph().as_default() as graph:
        tf.graph_util.import_graph_def(frozen_func.graph.as_graph_def(), name='')
        run_meta = tf.compat.v1.RunMetadata()
        opts = tf.compat.v1.profiler.ProfileOptionBuilder.float_operation()
        flops = tf.compat.v1.profiler.profile(graph=graph, run_meta=run_meta, cmd='op', options=opts)
        print(f"Total FLOPs: {flops.total_float_ops} FLOPs")
        return flops.total_float_ops

def measure_inference_time(model, input_data, num_iterations=100):
    """
    Measure average inference time
    Args:
        model: tensorflow model instance
        input_data: sample input data
        num_iterations: number of iterations to average over
    Returns:
        avg_time: average inference time in milliseconds
    """
    times = []
    
    # Warm-up run
    _ = model.predict(input_data)
    
    # Measure inference time
    for _ in range(num_iterations):
        start_time = time.time()
        _ = model.predict(input_data)
        end_time = time.time()
        times.append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    avg_time = np.mean(times)
    return avg_time

def calculate_tops(flops, inference_time_ms):
    """
    Calculate TOPS (Tera Operations Per Second)
    Args:
        flops: number of floating point operations
        inference_time_ms: inference time in milliseconds
    Returns:
        tops: Tera Operations Per Second
    """
    seconds = inference_time_ms / 1000
    tops = (flops / seconds) / 1e12  # Convert to tera
    return tops

def main():
    # Load your model (example)
    # Replace this with your actual model loading code
    # model = tf.keras.applications.ResNet50(weights='imagenet')
    model = tf.keras.models.load_model("/home/mpaul/projects/mpaul/mai2/models/models_dec05/mlp_20241205124515.h5")
    
    # custom_objects={
    #     "PositionalEncoding": PositionalEncoding,
    #     "objectosphere_loss": create_objectosphere_loss(),
    #     "OpensetModel": OpensetModel,
    #     "DirectionMaskLayer": DirectionMaskLayer,
    #     "OpensetUnknownLayer": OpensetUnknownLayer,
    # }
    
    # model = tf.keras.models.load_model("/home/mpaul/Downloads/pcaps/40app_models_1-6-0-24_v4_live/threehead_v4_checkpoint.h5")
    
    # Create sample input data
    # Modify this according to your model's input shape
    input_shape = (1, 224, 224, 3)
    sample_input = np.random.random(input_shape)
    
    # Calculate FLOPs
    flops = get_flops(model)
    # print(f"FLOPs: {flops:,}")
    
    # # Measure inference time
    # avg_inference_time = measure_inference_time(model, sample_input)
    # print(f"Average Inference Time: {avg_inference_time:.2f} ms")
    
    # # Calculate TOPS
    # tops = calculate_tops(flops, avg_inference_time)
    # print(f"TOPS: {tops:.2f}")

if __name__ == "__main__":
    main()
