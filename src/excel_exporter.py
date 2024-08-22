import pandas as pd
import os

class ExcelExporter:
    def export_to_excel(self, stories, output_path):
        try:
            df = pd.DataFrame(stories)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            df.to_excel(output_path, index=False, engine='openpyxl')
            print(f"Excel file created successfully at {output_path}")
        except Exception as e:
            print(f"Failed to export stories to Excel: {str(e)}")