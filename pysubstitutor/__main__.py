import argparse
import logging
import zipfile
from pysubstitutor.plist_to_gboard import AppleToGboardConverter
from pysubstitutor.zip_util import zip_file


def main():
    # Initialize logger
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Convert text substitutions files.")
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Path to the input file."
    )
    parser.add_argument(
        "-o", "--output", type=str, required=True, help="Path to the output file."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging."
    )
    parser.add_argument(
        "--zip",
        type=str,
        required=False,
        help="Path to the zip file to create after exporting the output file.",
    )

    args = parser.parse_args()

    # Set logging level based on verbose argument
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)

    logger.info(
        f"Starting conversion: Input file: {args.input}, Output file: {args.output}"
    )

    # Use the AppleToGboardConverter
    converter = AppleToGboardConverter(logger=logger)
    converter.read_file(args.input)
    converter.export_file(args.output)

    logger.info("Conversion completed successfully.")

    # Zip the output file if the --zip argument is provided
    if args.zip:
        zip_file(args.output, args.zip, logger)


if __name__ == "__main__":
    main()
