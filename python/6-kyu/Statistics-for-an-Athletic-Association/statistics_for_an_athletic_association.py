from statistics import median, mean


def get_formatted_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}|{int(minutes):02}|{int(seconds):02}"

def stat(strg):
    if not strg:
        return ''

    runs = strg.split(', ')

    runs_seconds = []
    for run in runs:
        hours, minutes, seconds = run.split('|')
        runs_seconds.append(int(hours)*3600 + int(minutes)*60 + int(seconds))

    result_median = median(runs_seconds)
    result_average = mean(runs_seconds)
    result_range = max(runs_seconds) - min(runs_seconds)

    result = (
        f"Range: {get_formatted_time(result_range)}"
        f" Average: {get_formatted_time(result_average)}"
        f" Median: {get_formatted_time(result_median)}"
    )

    return result
