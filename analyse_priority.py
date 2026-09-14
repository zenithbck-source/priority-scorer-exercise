""" === Imports === """
from priority_utils import calculate_priority_score, highest_priority_job
import pandas as pd
import matplotlib.pyplot as plt


""" === Data === """
jobs = [
    {"job_id": "J001", "wait_time": 5, "ncpus": 4, "priority_user": False},
    {"job_id": "J002", "wait_time": 28, "ncpus": 16, "priority_user": True},
    {"job_id": "J003", "wait_time": 2, "ncpus": 2, "priority_user": False},
    {"job_id": "J004", "wait_time": 75, "ncpus": 64, "priority_user": False},
    {"job_id": "J005", "wait_time": 5, "ncpus": 8, "priority_user": True},
    {"job_id": "J006", "wait_time": 40, "ncpus": 32, "priority_user": False},
]


""" === Program === """
df = pd.DataFrame(jobs)
df['priority_score'] = df.apply(calculate_priority_score, axis=1)
df = df.sort_values(by='priority_score', ascending=False)
print(df)
print()
print(df.head(2))

plt.bar(df['job_id'], df['priority_score'], data=df['priority_score'])
plt.xlabel("Job ID")
plt.ylabel("Priority Score")
plt.title("Job Priority Score")
plt.savefig("priority_scores.png")
plt.show()

print()
highest_priority_id, highest_priority_score = highest_priority_job(df)
print(f"Note: {highest_priority_id} has the highest priority score of {highest_priority_score}.")
print(f"This means that {highest_priority_id} will be the first job to be queued.")