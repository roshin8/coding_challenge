import requests
import logging
import app.model
from flask.wrappers import Response


def get_github_stats(org):
    """
    Function that collects stats from Github organisation.
        - Number of Public repos
        - Number of Forked repos
        - Count of total watchers on all repos
        - Count of languages used across all repos
        - Count of topics used across all repos

    :param org: Name of the organisation to collect stats from
    :returns: Serializable JSON data of the stats
    """
    logging.info(f"Fetching Github API for org: {org}")
    response = requests.get(f'https://api.github.com/orgs/{org}/repos')
    repos = response.json()
    if response.status_code != 200:
        raise ConnectionError(f"Failed to recieve data from GitHub for Org: {org}")

    public_repos = 0
    forked_repos = 0
    total_watchers = 0
    languages = set()
    topics = set()

    for repo in repos:
        if not repo.get('private'):
            if repo.get('fork'):
                forked_repos += 1
            else: 
                public_repos += 1

        languages.add(repo['language'])
        total_watchers += repo['watchers_count']

        # Get topic by calling the repo api
        headers = {"Accept": "application/vnd.github.mercy-preview+json"}
        topic_response = requests.get(f"https://api.github.com/repos/{org}/{repo['name']}/topics", headers=headers)
        if topic_response.status_code == 403:
            msg = "GitHub API rate limit exceeded"
            logging.error(msg)
            raise Exception(msg)

        topics.update([value.lower() for value in topic_response.json()['names']])

    return app.model.StatsModel("Github", public_repos, forked_repos, total_watchers, list(languages), list(topics))


def get_bitbucket_stats(team):
    """
    Function that collects stats from Bitbucket organisation.
        - Number of Public repos
        - Count of total watchers on all repos
        - Count of languages used across all repos
        - Count of topics used across all repos

    :param org: Name of the organisation to collect stats from
    :returns: Serializable JSON data of the stats
    """
    logging.info(f"Fetching Bitbucket API for team: {team}")
    response = requests.get(f'https://bitbucket.org/api/2.0/repositories/{team}')
    repos = response.json()['values']
    if response.status_code != 200:
        raise ConnectionError(f"Failed to recieve data from Bitbucket for Org: {team}")

    total_public_repos = 0
    total_watchers = 0
    languages = set()

    for repo in repos: 
        if not repo.get('is_private'):
            total_public_repos += 1
            
            # Get watchers info by calling the watchers api for each repo
            if repo.get('links'): 
                if repo['links'].get('watchers'):
                    if repo['links']['watchers'].get('href'):
                        total_watchers += requests.get(repo['links']['watchers']['href']).json().get('size', 0)

            if 'language' in repo:
                languages.add(repo['language'])
    
    return app.model.StatsModel("Bitbucket", total_public_repos, None, total_watchers, list(languages), None)
