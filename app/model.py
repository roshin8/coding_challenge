class StatsModel:

    def __init__(self, source, original_repos, forked_repos, watchers, languages, topics):
        self.source = source
        self.total_public_repos_original = original_repos
        self.total_public_repos_forked = forked_repos
        self.total_watchers = watchers
        self.languages = languages
        self.languages_count = len(languages) if languages != None else 0
        self.repo_topics = topics
        self.repo_topics_count = len(topics) if topics != None else 0

    # JSON format serializer
    def serialize(self):
        return {"source": self.source,
                "total_public_repos_original": self.total_public_repos_original,
                "total_public_repos_forked": self.total_public_repos_forked,
                "total_watchers": self.total_watchers,
                "languages": self.languages,
                "languages_count": self.languages_count,
                "repo_topics": self.repo_topics,
                "repo_topics_count": self.repo_topics_count }
