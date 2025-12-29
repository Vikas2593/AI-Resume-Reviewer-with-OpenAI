def generate_html_report(data: dict) -> str:
    return f"""
    <h2>Resume Review Report</h2>

    <p><b>Name:</b> {data['candidate_name']}</p>
    <p><b>City:</b> {data['city']}</p>
    <p><b>Experience:</b> {data['total_experience']} years</p>
    <p><b>Suitability Score:</b> {data['suitability_score']}%</p>
    <p><b>Recommendation:</b> {data['recommendation']}</p>

    <h3>Matched Skills</h3>
    <ul>
        {''.join(f"<li>{s}</li>" for s in data['skill_matching'])}
    </ul>

    <h3>Missing Skills</h3>
    <ul>
        {''.join(f"<li>{s}</li>" for s in data['skill_unmatched'])}
    </ul>

    <h3>Summary</h3>
    <p>{data['short_summary']}</p>
    """
