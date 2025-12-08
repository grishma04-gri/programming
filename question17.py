applicant={
    "name":"Priya",
    "skills":["Java","SQl"],
    "experience_years":1
}
required_skills={"Python","Java"}
name=applicant["name"]
skills=applicant["skills"]
experience=applicant["experience_years"]
has_required_skills=any(skill in required_skills for skill in skills)
if has_required_skills and experience>=2:
    print(f"{name} qualifies.")
else:
    print(f"{name} does not qualify.")