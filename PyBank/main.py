import os
import csv

def headerIndices(header):
    return {header_column: header_index for header_index, header_column in enumerate(header)}

def recordDateToOutputDate(recordDate):
    return f"{recordDate[:-2]}20{recordDate[-2:]}"

budget_data_path = os.path.join("Resources", "budget_data.csv")

months = 0
net_profit = 0
greatest_profit = {
    "date": "",
    "profit": None
}
least_profit = {
    "date": "",
    "profit": None
}
average_change = {
    "last_profit": None,
    "net_changes": 0
}

with open(budget_data_path, newline="") as budget_data_file:
    budget_data_reader = csv.reader(budget_data_file)
    header = next(budget_data_reader)
    header_indices = headerIndices(header)
    date_index = header_indices["Date"]
    profit_index = header_indices["Profit/Losses"]

    for budget_record in budget_data_reader:
        # Total Months
        months += 1

        # Net Profit/Losses
        current_profit = int(budget_record[profit_index])
        net_profit += current_profit

        # Average Change
        if (average_change["last_profit"] is not None):
            average_change["net_changes"] += current_profit - average_change["last_profit"]
        average_change["last_profit"] = current_profit


        # Greatest Increase in Profit (Date and Amount)
        if ((greatest_profit["profit"] is None) or current_profit > greatest_profit["profit"]):
            greatest_profit["date"] = budget_record[date_index]
            greatest_profit["profit"] = current_profit

        # Greatest Decrease in Profit (Date and Amount)
        if ((least_profit["profit"] is None) or current_profit < least_profit["profit"]):
            least_profit["date"] = budget_record[date_index]
            least_profit["profit"] = current_profit
    
average_change = average_change["net_changes"] / (months - 1)
greatest_profit_date = greatest_profit["date"]
greatest_profit_amount = greatest_profit["profit"]
least_profit_date = least_profit["date"]
least_profit_amount = least_profit["profit"]

output_text_rows= [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {months}",
    f"Total: ${net_profit}",
    f"Average  Change: ${round(average_change, 2)}",
    f"Greatest Increase in Profits: {recordDateToOutputDate(greatest_profit_date)} (${greatest_profit_amount})",
    f"Greatest Decrease in Profits: {recordDateToOutputDate(least_profit_date)} (${least_profit_amount})",
]

output_text = "\n".join(output_text_rows)

output_file_path = os.path.join("output.txt")

with open(output_file_path, "w") as output_file:
    output_file.write(output_text)

print(output_text)