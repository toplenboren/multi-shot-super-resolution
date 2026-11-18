import argparse
import main
import time

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Input directory containing images")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    args = parser.parse_args()
    
    now = time.time()

    images = main.load_images_from_dir(args.input)
    upscaled = main.upscale(images)
    
    main.save_image(upscaled, args.output)

    print(f"Done! Upscaled image saved to {args.output}. Elapsed {time.time() - now} seconds")

if __name__ == "__main__":
    __main__()
