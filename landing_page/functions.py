from team_members.models import Member


def get_team_members_data():
    """
    Function to get team members data from db for meet the team page
    :return:
    """
    team_members_data = Member.objects.select_related("job_role").filter(status=True)
    response = []
    for member in team_members_data:
        response.append({
            "id": member.id,
            "full_name": member.full_name,
            "profile_image_url": member.profile_image.url,
            "description": member.description,
            "job_role_code": member.job_role.code,
            "job_role_name": member.job_role.name.code,

        })
    return response
