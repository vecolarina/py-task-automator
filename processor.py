import pandas as pd
import os
from datetime import datetime

def process_csv(filepath):
    """
    Process a CSV file and return a summary report.
    - Reads the CSV
    - Cleans the data (strips whitespace, drops empty rows)
    - Generates a summary (row count, column info, basic stats)
    """
    try:
        print(f"📂 Processing file: {filepath}")

        # Read CSV
        df = pd.read_csv(filepath)

        # Basic cleaning
        df = df.dropna(how='all')  # Drop fully empty rows
        df.columns = df.columns.str.strip()  # Strip column name whitespace
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Strip cell whitespace

        # Generate summary
        summary = {
            "file": os.path.basename(filepath),
            "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "columns": list(df.columns),
            "null_counts": df.isnull().sum().to_dict(),
            "stats": df.describe(include='all').to_string()
        }

        print(f"✅ Processed successfully — {summary['total_rows']} rows, {summary['total_columns']} columns")
        return df, summary

    except Exception as e:
        print(f"❌ Error processing file: {e}")
        return None, None


def save_processed_file(df, original_filepath, output_folder):
    """
    Save the cleaned DataFrame as a new CSV in the output folder.
    """
    try:
        filename = os.path.basename(original_filepath)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"processed_{timestamp}_{filename}"
        output_path = os.path.join(output_folder, output_filename)

        os.makedirs(output_folder, exist_ok=True)
        df.to_csv(output_path, index=False)

        print(f"💾 Saved processed file to: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error saving processed file: {e}")
        return None