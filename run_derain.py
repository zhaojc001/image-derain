from test_model import *

if __name__ == '__main__':
    # init args
    args = init_args()

    # test model
    test_model(args.image_path, args.weights_path, args.output_path)

