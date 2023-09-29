import csv
from Calculator import Calculator
class CSVCalculatorHandler:
    def __init__(self):
        self.history = []

    def process_csvs(self, filenames, output_prefix="output"):
        for id, filename in enumerate(filenames):
            output_filename = f"{output_prefix}_{id}.csv"
            with open(filename, 'r') as csv_file, open(output_filename, 'w', newline='') as output_csv_file:
                csv_reader = csv.reader(csv_file)
                csv_writer = csv.writer(output_csv_file)
                calculator = Calculator()
                for row in csv_reader:
                    result = None  # Initialize result to None
                    try:
                        operands = [float(val) for val in row[:-1]]
                        operation = row[-1].strip()
                        if operation not in ('add', 'subtract', 'multiply', 'divide', 'exponentiate'):
                            raise ValueError("Unknown Operator")
                        if len(operands) < 2:
                            raise ValueError("Not enough operands")
                        op_function = getattr(calculator, operation)
                        result = op_function(*operands)
                        csv_writer.writerow([result, 0])
                    except ZeroDivisionError:
                        csv_writer.writerow([None, 1])
                    except (ValueError, TypeError):
                        csv_writer.writerow([None, 3])
                    except Exception as e:
                        csv_writer.writerow([None, 4])
                    finally:
                        self.save_to_history(filename, row, result, 0 if result is not None else 2)

    def save_to_history(self, filename, operation, result, error_code):
        self.history.append([filename, ",".join(map(str, operation)), result, error_code])

    def history_export(self, export_filename):
        with open(export_filename, 'w', newline='') as history_file:
            history_writer = csv.writer(history_file)
            history_writer.writerow(['input_file', 'operation', 'result', 'error'])
            history_writer.writerows(self.history)

if __name__ == '__main__':
        handler = CSVCalculatorHandler()
        handler.process_csvs(['input.csv'])
        handler.history_export('history.txt')