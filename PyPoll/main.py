import os
import csv
from collections import defaultdict

poll_data_path = os.path.join("Resources", "election_data.csv")

total_votes = 0
vote_tallies = defaultdict(int)


with open(poll_data_path, newline="") as poll_data_file:
    poll_data_reader = csv.reader(poll_data_file)
    header = next(poll_data_reader)
    candidate_index = 2

    for vote_record in poll_data_reader:
        total_votes += 1
        candidate = vote_record[candidate_index]
        vote_tallies[candidate] += 1

vote_result_texts = [
    f"{candidate}: {round(votes / total_votes * 100, 3)}% ({votes})"
    for candidate, votes in vote_tallies.items()
]
winner = max(vote_tallies.items(), key=lambda tally: tally[1])
winner = winner[0]

output_text_rows = [
    "Election Results",
    "----------------------------",
    f"Total Votes: {total_votes}",
    "----------------------------",
    *vote_result_texts,
    "----------------------------",
    f"Winner: {winner}",
    "----------------------------",
]
output_text = "\n".join(output_text_rows)

output_file_path = os.path.join("output.txt")

with open(output_file_path, "w") as output_file:
    output_file.write(output_text)

print(output_text)
