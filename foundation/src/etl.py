import csv
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ETLProcessor:
    def __init__(self, source_folder, destination_folder):
        self.source_folder = Path(source_folder)
        self.destination_folder = Path(destination_folder)

    def discover_files(self):
        """
        Discover all CSV files in the source folder and subfolders.
        """
        return list(self.source_folder.rglob("*.csv"))

    def detect_encoding(self, file_path):
        """
        Detect the file encoding by trying common encodings.
        """
        encodings = [
            "utf-8",
            "utf-8-sig",
            "cp1252",
            "latin1"
        ]

        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    f.read(4096)

                logging.info(f"Detected encoding: {encoding}")
                return encoding

            except UnicodeDecodeError:
                continue

        raise UnicodeError(f"Could not determine encoding for {file_path}")

    def detect_delimiter(self, file_path, encoding):
        """
        Detect the delimiter used in the CSV file.
        """

        delimiters = [",", ";", "|", "\t"]

        try:
            with open(file_path, "r", encoding=encoding, newline="") as f:
                sample = f.read(4096)

            delimiter = csv.Sniffer().sniff(
                sample,
                delimiters=delimiters
            ).delimiter

            logging.info(f"Detected delimiter: {repr(delimiter)}")

            return delimiter

        except csv.Error:

            logging.warning(
                "Delimiter could not be detected automatically."
            )

            best_delimiter = ","
            best_columns = 0

            for delimiter in delimiters:
                try:
                    df = pd.read_csv(
                        file_path,
                        sep=delimiter,
                        encoding=encoding,
                        nrows=5
                    )

                    if len(df.columns) > best_columns:
                        best_columns = len(df.columns)
                        best_delimiter = delimiter

                except Exception:
                    pass

            logging.info(
                f"Using fallback delimiter: {repr(best_delimiter)}"
            )

            return best_delimiter

    def extract_data(self, file_path):
        """
        Extract data from a CSV file.
        """

        if file_path.suffix.lower() != ".csv":
            raise ValueError(
                f"Unsupported file format: {file_path.suffix}"
            )

        logging.info(f"Extracting data from {file_path}")

        encoding = self.detect_encoding(file_path)
        delimiter = self.detect_delimiter(file_path, encoding)

        return pd.read_csv(
            file_path,
            sep=delimiter,
            encoding=encoding
        )

    def transform_data(self, data):
        """
        Clean and transform extracted data.
        """

        logging.info(
            f"Initial data shape: {data.shape[0]} rows, {data.shape[1]} columns"
        )

        rows_before = len(data)

        data = data.dropna(how="all")
        data = data.drop_duplicates()

        rows_after = len(data)
        rows_dropped = rows_before - rows_after

        logging.info(
            f"Rows in: {rows_before}; "
            f"Rows out: {rows_after}; "
            f"Rows dropped: {rows_dropped}"
        )

        logging.info(
            f"Final data shape: {data.shape[0]} rows, {data.shape[1]} columns"
        )

        return data

    def load_data(self, data, source_file):
        """
        Save transformed data.
        """

        self.destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = (
            self.destination_folder /
            f"{source_file.stem}_processed.csv"
        )

        data.to_csv(
            output_file,
            index=False
        )

        logging.info(f"Saved to {output_file}")

    def run_processor(self):
        """
        Run the ETL process.
        """

        files = self.discover_files()

        if not files:
            logging.warning("No CSV files found.")
            return

        logging.info(f"Found {len(files)} CSV file(s).")

        for file in files:

            try:

                logging.info("=" * 70)
                logging.info(f"Processing {file.name}")

                data = self.extract_data(file)

                transformed_data = self.transform_data(data)

                self.load_data(
                    transformed_data,
                    file
                )

                logging.info(f"Finished processing {file.name}")

            except Exception as e:

                logging.exception(
                    f"Failed processing {file.name}: {e}"
                )

                continue


def main():

    source = (
        "C:/Users/User/Documents/"
        "AADE-assistant-analyst-data-engine/test_data"
    )

    destination = (
        "C:/Users/User/Documents/"
        "AADE-assistant-analyst-data-engine/test_data/processed_data"
    )

    processor = ETLProcessor(
        source,
        destination
    )

    processor.run_processor()


if __name__ == "__main__":
    main()