def count_marketers(job_titles: list[str]) -> int | None:
    count = 0
    if not job_titles:
        return 0
    if job_titles[-1] == "marketer":
        count += 1
    return count + count_marketers(job_titles[: len(job_titles) - 1])

test = ["programmer", "marketer", "doctor", "marketer"]

print(count_marketers(test))


