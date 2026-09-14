def calculate_priority_score(job):
    score = job['wait_time'] * 1.0 + job['ncpus'] * 0.5
    if(job['priority_user']):
        score += 20
    return score

def highest_priority_job(df):
    top_row = df.loc[df['priority_score'].idxmax()]
    return top_row['job_id'], top_row['priority_score']