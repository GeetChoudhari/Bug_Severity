import xml.etree.ElementTree as ET
from datetime import datetime
import csv


def convert_xml_to_csv(xml_file_path, csv_file_path):
    """
    Converts an XML file to a CSV format. Assumes the XML file has a structure with 'report' elements,
    each containing multiple 'update' elements with 'when' and 'what' sub-elements.

    :param xml_file_path: Path to the input XML file.
    :param csv_file_path: Path to the output CSV file.
    """
    try:
        # Load and parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Open a CSV file for writing
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)

            # Writing the header of CSV file
            header = ['Bug_id', 'Timestamp', 'Assignee']
            csvwriter.writerow(header)

            # Iterating through each report in the XML
            # for report in root:
            #     report_id = report.get('id')
            for report in root.findall('report'):
                report_id = report.get('id')  # Get the 'id' attribute of the report

                # Iterating through each update in the report
                # for update in report:
                #     when = update.find('when').text
                # Iterate over each update in the report
                for update in report.findall('update'):
                    unix_timestamp = update.find('when').text  # Get the Unix timestamp
                    # Convert to human-readable date and time
                    Timestamp = datetime.utcfromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')

                    Status = update.find('what').text

                    # Writing the report data to the CSV file
                    csvwriter.writerow([report_id, Timestamp, Status])

        return "Conversion successful. CSV file created at: " + csv_file_path
    except Exception as e:
        return "An error occurred during conversion: " + str(e)

# Example usage of the function
convert_xml_to_csv('E:/Project Dataset/Data/mozilla/Thunderbird/assigned_to.xml', 'E:/Project Dataset/UpdatedData/mozilla/Thunderbird/Assigned.csv')

